from neo4j import GraphDatabase

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "bolt://localhost:7687"
AUTH = ("neo4j", "12341234")

# a mapping from direction string to cypher direction
direction_mapping = {
    "from": "<-[:{relation_name}]-",
    "to": "-[:{relation_name}]->",
    "bidirectional": "-[:{relation_name}]->",
}

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
    
def execute_cypher(cypher_script: str) -> tuple[list[dict], dict, list[str]]:
    try:
        with GraphDatabase.driver(URI, auth=AUTH) as driver:
            records, summary, keys = driver.execute_query(cypher_script)
        return records, summary, keys
    except Exception as e:
        print(f"Error: Failed to execute Cypher script: {e}")
        return None, None, None
    

def add_node(node_name: str, node_type: str, node_content: str):
    cypher_script = f"CREATE (n: {node_type} {{name: '{node_name}', content: '{node_content}'}}) RETURN n;"
    execute_cypher(cypher_script)

def add_relationship(source_node_name: str, source_node_type: str, target_node_name: str, target_node_type: str, relationship_name: str, direction: str):
    direction_string = direction_mapping[direction].format(relation_name=relationship_name)
    cypher_script = f"MATCH (n1: {source_node_type} {{name: '{source_node_name}'}}), (n2: {target_node_type} {{name: '{target_node_name}'}}) CREATE (n1){direction_string}(n2) RETURN n1, n2;"
    execute_cypher(cypher_script)
    
    if direction == "bidirectional":
        direction_string = direction_mapping["from"].format(relation_name=relationship_name)
        cypher_script = f"MATCH (n1: {source_node_type} {{name: '{source_node_name}'}}), (n2: {target_node_type} {{name: '{target_node_name}'}}) CREATE (n1){direction_string}(n2) RETURN n1, n2;"
        execute_cypher(cypher_script)

def check_node_exists(node_name: str, node_type: str):
    cypher_script = f"MATCH (n:{node_type}) WHERE toLower(n.name) = toLower('{node_name}') RETURN n;"
    # print(cypher_script)
    records, summary, keys = execute_cypher(cypher_script)
    found = len(records) > 0
    assert len(records) <= 1, f"Multiple nodes with name {node_name} and type {node_type} found"
    actual_node_name = records[0]['n']['name'] if found else None
    return found, actual_node_name

def check_relationship_exists(source_node_name: str, source_node_type: str, target_node_name: str, target_node_type: str, relationship_name: str):
    cypher_script = f"""
        MATCH (n1: {source_node_type} {{name: '{source_node_name}'}})-[r:{relationship_name}]-(n2: {target_node_type} {{name: '{target_node_name}'}})
        RETURN r;
    """
    records, summary, keys = execute_cypher(cypher_script)
    found = len(records) > 0
    print(f"Relationship {relationship_name} from {source_node_name} to {target_node_name} exists: {found}")
    return found


if __name__ == "__main__":
    add_node("test_name", "test_type", "test_content")
    check_node_exists("test_Name", "test_type")
    add_node("test_target_name", "test_target_type", "test_target_content")
    add_relationship("test_name", "test_type", "test_target_name", "test_target_type", "test_relationship_name", "to")
    check_relationship_exists("test_name", "test_type", "test_target_name", "test_target_type", "test_relationship_name")

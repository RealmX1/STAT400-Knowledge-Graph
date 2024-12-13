### **node-md2cypher_prompt.md**

You will be provided with information about node that need to be added to neo4j database. The information will be presented in json format. Additionally, you will be provided with a list of existing `node type;node name` pairs in the knowledge graph (for reference when creating the relationships). Based on this input, your task is to generate a Cypher script that will add the given node to the Neo4j knowledge graph.

- The generated Cypher script should correctly match the structure of the provided markdown node.
- Ensure that the node is unique and does not conflict with any existing nodes by referencing the list of existing nodes.
- Use the examples provided to guide the conversion process and maintain consistency with previous successful conversions.
- the relation endpoint from the markdown may not be exact. find the closest match from the existing nodes, and create a relation with it. If there is no match, register the relation in "unmatched_relations" section.
- the cypher should treat all input string as literal string, instead of interpreting escape sequence.


**Output:**  
A Cypher script that adds the given node to the Neo4j knowledge graph (just the node itself and its attributes, not including relationships), 
Relations with end node matching existing nodes, together with cypher script to add such relation
Relations without end node matching existing nodes

Input will be provided in following format:
**Input:**
<node_to_add>{node_to_add}</node_to_add>
<existing_nodes>{existing_nodes}</existing_nodes>
### **node-md2cypher_prompt.md**

You will be provided 
1. a (source) node name and its type, together with 
2. a list of relations, each with name and type of the node on the other side (the author doesn't know if this other node already exist or not)
3. a list of existing `node type;node name` pairs in the knowledge graph

For each relation, based on the constraint provided by the relations (on what name and type the other end of the relation should be), you should try match the entity mentioned in the relation with an existing node. You should allow match to aliases and ignore case difference. If there is no match, skip this relation; Else Register the node that is on the other side of the relation according to the schema provided.

Note that the same relation may have multiple target nodes, each representing an additional relation between the source node and the target node. Each such relation should be considered and registered (if matching) separately.

**Output:**
Matched relations from the start node that are matching with existing nodes

Input will be provided in following format:
**Input:**
<node_to_add>{node_to_add}</node_to_add>
<existing_nodes>{existing_nodes}</existing_nodes>
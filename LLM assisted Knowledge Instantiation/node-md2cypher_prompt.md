### **node-md2cypher_prompt.md**

You will be provided with a markdown-formatted node, a list of existing `node type;node name` pairs in the knowledge graph, and examples of successful markdown-to-Cypher conversions. Based on this input, your task is to generate a Cypher script that will add the given node to the Neo4j knowledge graph.

- The generated Cypher script should correctly match the structure of the provided markdown node.
- Ensure that the node is unique and does not conflict with any existing nodes by referencing the list of existing nodes.
- Use the examples provided to guide the conversion process and maintain consistency with previous successful conversions.
- the relation endpoint from the markdown may not be exact. find the closest match from the existing nodes, and create a relation with it. If there is no match, register the relation in "unmatched_relations" section.
- '←' or '<-' means the relation has this node as the target and the node following the symbol as source; '→' or '->' means the relation has this node as the source and the node following it is the target; '↔' or '<->' means the relation is bidirectional; '=' or '-' or '--' means the relation is undirected.


**Output:**  
A Cypher script that adds the given node to the Neo4j knowledge graph, together with a list of unmatched relations.

Input will be provided in following format:
**Input:**
- **Markdown Node:**
  `<node_markdown>{node_markdown}</node_markdown>`
- **Existing `node type;node name` Pairs in the Graph:**
  `<existing_nodes>{existing_nodes}</existing_nodes>`
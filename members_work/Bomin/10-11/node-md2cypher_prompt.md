### **node-md2cypher_prompt.md**

You will be provided with a markdown-formatted node, a list of existing `node_name:node_type` pairs in the knowledge graph, and examples of successful markdown-to-Cypher conversions. Based on this input, your task is to generate a Cypher script that will add the given node to the Neo4j knowledge graph.

- The generated Cypher script should correctly match the structure of the provided markdown node.
- Ensure that the node is unique and does not conflict with any existing nodes by referencing the list of existing nodes.
- Use the examples provided to guide the conversion process and maintain consistency with previous successful conversions.

**Input:**
- **Markdown Node:**  
  `<node_markdown></node_markdown>`  
- **Existing `node_name:node_type` Pairs in the Graph:**  
  `<existing_nodes></existing_nodes>`  
- **Examples of Successful Conversion:**  
  `<example>  
     <input></input>  
     <reply></reply>  
  </example>`

---

**Output:**  
A Cypher script that adds the given node to the Neo4j knowledge graph.

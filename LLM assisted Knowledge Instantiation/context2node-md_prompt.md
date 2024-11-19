You will be given the content of a chapter in a book for statistics, a schema for the respective node type, a list of existing `node type;node name` pairs in the graph, and the specific node name. Based on this information, you should generate a markdown-formatted node for the given `node-name` according to the node-type-schema provided.

- Use the content provided to fill out the schema on {topic}.
- For any relevant information that isn't part of the context but is important for the schema, add it in italics (*additional information*).
- Leave blank any parts of the schema that are neither covered in the context nor have additional important information.
- Ensure that the output follows the markdown format for the node, structured in a way that will be useful for later conversion into a Neo4j-compatible format.
- If some information doesn't fit into the schema or doesn't correspond to the node, note it down separately in a markdown file.
- When Creating Relationship, refer to the existing nodes in the graph, and use the node name from existing nodes list.


Input will be provided in following format:
<div class="input">
  <div class="existing-nodes">{existing_nodes}</div>
  <div class="node-name">{node_name}</div>
  <div class="node-type">{node_type}</div>
  <div class="chapter-content">{chapter_content}</div>
  <div class="additional-context">{additional_context}</div>
  <div class="node-type-schema">{node_type_schema}</div>
</div>
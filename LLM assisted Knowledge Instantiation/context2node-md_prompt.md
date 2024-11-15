You will be given the content of the chapter (or whole book) for the topic "{topic}" in "{chapter_name}" of a textbook, a schema for the respective node type, a list of existing `node_type;node_name` pairs in the graph, and the specific node name. Based on this information, you should generate a markdown-formatted node for the given `node_name` according to the schema provided.

- Use the content provided to fill out the schema on {topic}.
- For any relevant information that isn't part of the context but is important for the schema, add it in italics (*additional information*).
- Leave blank any parts of the schema that are neither covered in the context nor have additional important information.
- Ensure that the output follows the markdown format for the node, structured in a way that will be useful for later conversion into a Neo4j-compatible format.
- If some information doesn't fit into the schema or doesn't correspond to the node, note it down separately in a markdown file.



Now provide your reply for the following input:
<Input>
- **Chapter Content:** {Chapter Content}
- **Node Type Schema:** {Node Schema}
- **Existing `node_type;node_name` Pairs in the Graph:** {List of Existing Nodes}
- **Node Name:** {Node Name}
</Input>





<!-- Here is an example of prompt and reply:
<Example>
    <Input>
    </Input>
    <Reply>
    </Reply>
</Example> --> ignore this when copying the prompt
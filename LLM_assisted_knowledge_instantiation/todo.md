## 2024-12-13 
### how to avoid inherited relation from being logged down in the graph directly?
It is relatively easy to check the relation using neo4j query; is it necessary, and if so possible to avoid such relation from being generated during LLM query time?
I'd say it isn't.

### try RAG + entry-wise generation
directly performing entry-wise generation would result in too many tokens. Using RAG to filter content about a node first might help with this.

### Maintaining consistency between previously generated nodes...
generation of template for node type


### major halucination issue regarding existing nodes.
maybe making the task more atomic might help. again, RAG would be helpful.

### relation direction - extraction difficulty vs. graph representation intuitiveness
there is a trade-off here. Maybe separating the two and having a conversion table in the cypher generation step might help.

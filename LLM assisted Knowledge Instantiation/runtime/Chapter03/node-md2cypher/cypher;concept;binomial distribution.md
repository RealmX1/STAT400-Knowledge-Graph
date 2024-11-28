```cypher
// Add the node itself
CREATE (n:Concept {name: "Binomial Distribution", description: "The Binomial distribution models the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success. It is commonly used in situations where the outcomes of interest are categorical, typically with binary outcomes such as success/failure or yes/no.", 
notation: "X \\sim \\text{Binomial}(n, p)", 
explanation: [
  {part: "n", range: "n \\in \\mathbb{N}", description: "Number of trials"}, 
  {part: "p", range: "p \\in (0,1)", description: "Probability of success in each trial"}
]
});

// Add relationships with existing nodes
MATCH (n:Concept {name: "Binomial Distribution"})
MATCH (m:Concept {name: "Discrete Distribution"})
MERGE (n)-[:RELATED_TO]-(m);

// Unmatched relations
// has_subconcept -> Bernoulli Distribution
// is_prerequisite_of -> Geometric Distribution
```
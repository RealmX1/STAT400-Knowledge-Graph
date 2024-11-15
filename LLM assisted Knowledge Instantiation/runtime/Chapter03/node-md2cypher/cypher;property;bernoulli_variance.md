To generate a Cypher script based on the provided markdown node, we'll create a new node for the "variance of bernoulli Distribution" with its attributes and establish the relationships as described.

First, we start by creating the main node, including its name, definition, and proof as properties. Then, we will create relationships to other nodes like "Bernoulli Distribution", "variance of random variable", and "expected value of bernoulli distribution". Since there are no existing nodes listed, we assume these related nodes need to be created as well without duplicates.

Here’s the Cypher script that matches the markdown node structure:

```cypher
// Create the main node for 'variance of bernoulli Distribution'
MERGE (vbd:PropertyNode {
  name: 'variance of bernoulli Distribution', 
  definition: 'X ~ Bernoulli(p) where: X is a random variable following the Bernoulli distribution. Then we will have Var(X) = p(1 - p)',
  proof: 'Let X be a random variable that follows a Bernoulli distribution with probability p: X ~ Bernoulli(p) where: P(X = 1) = p (probability of success) P(X = 0) = 1 - p (probability of failure) The variance of X, denoted Var(X), is defined as: Var(X) = E[X^2] - (E[X])^2 We already know that E[X] = p. Now, let\'s find E[X^2]. Since X can only be 0 or 1, we have X^2 = X. Thus: E[X^2] = E[X] = p Now we can substitute into the formula for variance: Var(X) = E[X^2] - (E[X])^2 Var(X) = p - p^2 Var(X) = p(1 - p) Therefore, the variance of a Bernoulli distribution is: Var(X) = p(1 - p) From Stat400 teaching material - Jonathan Fernandez'
})

// Create related nodes if not existing and relationships
MERGE (bd:Distribution {name: 'Bernoulli Distribution'})
MERGE (vrv:Concept {name: 'variance of random variable'})
MERGE (evbd:Property {name: 'expected value of bernoulli distribution'})

// Create relationships between the nodes
MERGE (vbd)-[:IS_PROPERTY_OF]->(bd)
MERGE (vbd)-[:IS_CHILD_CONCEPT_OF]->(vrv)
MERGE (vbd)-[:DEPENDS_ON]->(evbd)
```

This script assumes that related nodes do not already exist, and uses `MERGE` which will create the node or relationship only if it doesn't exist, thereby avoiding duplicates. Customize node types and properties as per your knowledge graph’s schema if necessary.
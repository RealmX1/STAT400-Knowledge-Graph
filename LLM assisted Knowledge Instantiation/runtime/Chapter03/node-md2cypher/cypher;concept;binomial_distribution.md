```cypher
// Create a node for the concept of "Binomial Distribution"
MERGE (n:ConceptNode {
    name: "binomial distribution", 
    notation: "X ~ Binomial(n, p)",
    description: "Suppose now that n independent trials, each of which results in a probability p of success and 1 - p of failure. Then X is said to be a binomial random variable with parameter (n, p) if X represents the number of successes that occurred in n trials. The PMF of such a binomial random variable is given by p(X = i) = (n choose i) * p^i * (1 - p)^(n - i), i = 0, 1, ..., n.", 
    source: "Stat400 teaching material - Jonathan Fernandez"
})
RETURN n
```

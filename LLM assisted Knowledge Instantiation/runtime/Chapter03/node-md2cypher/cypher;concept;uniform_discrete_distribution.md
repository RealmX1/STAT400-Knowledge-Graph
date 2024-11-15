```cypher
// Create the Concept Node for "uniform discrete distribution"
MERGE (n:ConceptNode {
  name: "uniform discrete distribution",
  definition: "Let $X$ be a random variable that can take on one of $n$ distinct values, $x_1, x_2, \\ldots, x_n$, with each value having the same probability of occurring. Then $X$ is said to be a Uniform discrete random variable. The probability mass function (PMF) of $X$ is given by $p(X = x_i) = \\frac{1}{n}, \\quad i = 1, 2, \\ldots, n$",
  notation: "X \\sim \\text{Unif}(a,b)",
  description: "In a discrete uniform distribution, every outcome is equally likely. From `Stat400 teaching material - Jonathan Fernandez`"
})
```

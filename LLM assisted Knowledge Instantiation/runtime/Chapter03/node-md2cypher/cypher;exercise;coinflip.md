```cypher
// Create the Exercise Node
CREATE (e:Exercise {
  name: "coin toss example",
  problem_statement: "Let the outcome of the coin flip be denoted as a random variable $X$. If the coin lands on heads, let $X = 1$. If the coin lands on tails, let $X = 0$. Assume that the probability of landing on heads (success) is $p$, which could be, for instance, 0.5 for a fair coin. Compute PMF of $X$",
  notation: "PMF",
  solution: "The probability mass function (PMF) of the Bernoulli distribution can be expressed as: P(X = x) = { p if x = 1; 1 - p if x = 0 }",
  difficulty_level: "1/5",
  source: "Stat400 teaching material - Jonathan Fernandez"
});

// Assume we need to relate this node to the discrete_bernoulli_concept node
MERGE (c:Concept { name: "discrete_bernoulli_concept" })

// Create the relationship
CREATE (e)-[:IS_EXERCISE_FOR]->(c);
```
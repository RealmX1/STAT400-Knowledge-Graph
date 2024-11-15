```cypher
// Create the Exercise Node
MERGE (exercise:Exercise {
  name: "coin toss example",
  problem_statement: "Find PMF of a fair six-sided die. Notation: PMF",
  solution: "Consider a fair six-sided die. When rolling the die, each side (1, 2, 3, 4, 5, and 6) has an equal probability of occurring. Since the die is fair, the probability of rolling any specific number is uniform. The probability mass function for this uniform discrete distribution can be defined as: P(X = x) = 1/6, where x ∈ {1, 2, 3, 4, 5, 6}. In this example, each number from 1 to 6 is equally likely, so the distribution of outcomes follows a discrete uniform distribution.",
  difficulty_level: 1,
  source: "Stat400 teaching material - Jonathan Fernandez"
})

// Assuming existence of 'Distribution' node for the uniform discrete distribution
MERGE (distribution:Distribution {type: "uniform discrete distribution"})

// Create Relationship from Exercise to Distribution
MERGE (exercise)-[:IS_EXERCISE_FOR]->(distribution)
```
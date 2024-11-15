```cypher
// Check if the Exercise Node already exists, if not, create it
MERGE (ex:Exercise {name: "widgets in a factory"})
ON CREATE SET 
    ex.problem_statement = "Imagine you are working at a factory that produces widgets. In a batch of 50 widgets, 10 are defective, and 40 are not. You randomly select 5 widgets for a quality check. You are interested in finding the probability that exactly 2 of the 5 widgets you selected are defective.",
    ex.notation = "PMF, probability",
    ex.solution = "Population size N = 50, n = 5, m = 10. Based on the distribution of a Hypergeometric random variable, p(x = 2) = (binom(10,2) binom(50 - 10,5 - 2))/(binom(50,5)) = (binom(10,2) binom(40,3))/(binom(50,5)) = 0.21.",
    ex.difficulty_level = "1/5",
    ex.source = "Stat400 teaching material - Jonathan Fernandez"

// As the existing nodes list is empty, create a new `hypergeometric distribution` node and relationship
MERGE (dist:Distribution {name: "hypergeometric distribution"})
MERGE (ex)-[:IS_EXERCISE_FOR]->(dist)
```
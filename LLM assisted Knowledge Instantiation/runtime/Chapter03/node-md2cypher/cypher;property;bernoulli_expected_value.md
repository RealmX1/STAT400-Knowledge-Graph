```cypher
// Create the "expected value of bernoulli distribution" node
MERGE (n:PropertyNode {
  name: "expected value of bernoulli distribution",
  aliases: ["mean of bernoulli Distribution"],
  definition: "given X ~ Bernoulli(p) where: X is a random variable following the Bernoulli distribution. Then we will have E[X] = p",
  proof: "Let X be a random variable that follows a Bernoulli distribution with probability p: X ~ Bernoulli(p) where: - P(X = 1) = p (probability of success) - P(X = 0) = 1 - p (probability of failure) The mean (or expected value) of X is defined as: E[X] = sum_x x P(X = x) Since X only takes the values 0 and 1, we can rewrite this as: E[X] = 0 P(X = 0) + 1 P(X = 1) Substitute the probabilities: E[X] = 0 (1 - p) + 1 p E[X] = 0 + p = p Thus, the mean of a Bernoulli distribution is: E[X] = p From Stat400 teaching material - Jonathan Fernandez"
})

// Create a node for "Bernoulli Distribution" if it doesn't exist
MERGE (bernoulli:Distribution {name: "Bernoulli Distribution"})

// Create a node for "expected value of random variable" if it doesn't exist
MERGE (expectedValue:Concept {name: "expected value of random variable"})

// Create the relationships
MERGE (n)<-[:is_property_of]-(bernoulli)
MERGE (n)<-[:is_child_concept_of]-(expectedValue)
```
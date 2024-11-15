```cypher
// Add the 'Property Node Schema' node with its attributes
MERGE (p:PropertyNodeSchema {name: 'expected value of binomial distribution'})
SET p.definition = 'X ~ Binomial(n, p) where: X is a random variable following the Binomial distribution. Then we will have E[X] = np',
    p.proof = 'The binomial distribution describes the number of successes in n independent trials, each with a success probability p. Let X ~ Binomial(n, p). Step 1: Define X as a Sum of Bernoulli Trials. Let X = X1 + X2 + ... + Xn, where each Xi is an independent Bernoulli random variable with: P(Xi = 1) = p and P(Xi = 0) = 1 - p. Then, X represents the number of successes in n trials. Step 2: Expected Value of X By the linearity of expectation, E(X) = E(X1 + X2 + ... + Xn) = E(X1) + E(X2) + ... + E(Xn). Since each Xi is Bernoulli with expected value E(Xi) = p, E(X) = np. Thus, the mean of a binomial distribution is: mu = np.',
    p.source = 'Stat400 teaching material - Jonathan Fernandez'

// Add the 'Binomial Distribution' node and create the relationship
MERGE (b:Concept {name: 'Binomial Distribution'})
MERGE (b)-[:HAS_PROPERTY]->(p)

// Add the 'Expected value of random variable' node and create the relationship
MERGE (e:Concept {name: 'expected value of random variable'})
MERGE (e)-[:HAS_CHILD_CONCEPT]->(p)
```

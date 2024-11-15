```cypher
// Creating a unique node for the property 'variance of Binomial Distribution'
CREATE (p:Property {
    name: "variance of Binomial Distribution", 
    definition: "given X ~ Binomial(n,p) where: X is a random variable following the Binomial distribution. Then we will have Var(X) = np(1 - p)"
}) 

// Adding a proof attribute
SET p.proof = "The binomial distribution describes the number of successes in n independent trials, each with a success probability p. Let X ~ Binomial(n, p). Step 1: Define X as a Sum of Bernoulli Trials Let X = X1 + X2 + ... + Xn, where each Xi is an independent Bernoulli random variable with: P(Xi = 1) = p and P(Xi = 0) = 1 - p. Then, X represents the number of successes in n trials. Step 2: Variance of X Since X = X1 + X2 + ... + Xn and each Xi is independent, we can use the property that the variance of the sum of independent variables is the sum of their variances: Var(X) = Var(X1 + X2 + ... + Xn) = Var(X1) + Var(X2) + ... + Var(Xn). Step 3: Variance of Each Xi Each Xi is a Bernoulli random variable with variance: Var(Xi) = p(1 - p). Step 4: Substitute into the Variance of X Since there are n identical terms, Var(X) = n * p(1 - p). Thus, the variance of a binomial distribution is: sigma^2 = np(1 - p). From Stat400 teaching material - Jonathan Fernandez"

// Creating relationships (edges) with the closest match from provided endpoints
MATCH (b:Concept {name: "Binomial Distribution"})
CREATE (p)-[:IS_PROPERTY_OF]->(b)

MATCH (v:Concept {name: "variance of random variable"})
CREATE (p)-[:IS_CHILD_CONCEPT_OF]->(v)

MATCH (e:Concept {name: "expected value of binomial distribution"})
CREATE (p)-[:DEPENDS_ON]->(e)
```
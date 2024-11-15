```cypher
MERGE (n:ConceptNode {
  name: "bernouli distribution",
  aliases: ["binary distribution", "bernoulli trial"],
  definition: "Let $X$ be a random variable that represents the outcome of a Bernoulli trial. Then $X$ is said to be a Bernoulli random variable with parameter $p$, where $p$ is the probability of success (i.e., the probability that $X = 1$) and $1 - p$ is the probability of failure (i.e., the probability that $X = 0$). The PMF of such a Bernoulli random variable is given by P(X = x) = { p if x = 1 \\ 1 - p if x = 0 }, Notation: X ~ Bernoulli(p) where: X is a random variable following the Bernoulli distribution. p is the probability of success (0 <= p <= 1).",
  description: "A Bernoulli trial is a random experiment that has exactly two possible outcomes: \"success\" and \"failure.\" Each trial is independent, meaning the outcome of one trial does not affect the outcome of another. The probability of success, denoted as $p$, which remains constant across all trials. From 'Stat400 teaching material - Jonathan Fernandez'"
})
```
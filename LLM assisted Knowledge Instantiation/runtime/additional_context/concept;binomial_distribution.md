# Concept Node Schema

## Attributes

- **Name**: binomial distribution

- **Definition**:
  - **Notation**: 
  $
  X \sim \text{Binomial}(n,p)
  $
  where:
  $X$ is a random variable following the Binomial distribution.
  $n$ defines the number of trials.
  $p$ is the probability of success ($0 \leq p \leq 1$). 
  - **Description**:
  Suppose now that $n$ independent trials, each of which results in a probability $p$ of success and $1 - p$ of failure. Then $X$ is said to be a binomial random variable with parameter $(n, p)$ if $X$ represents the number of successes that occurred in $n$ trials.
  The PMF of such a binomial random variable is given by
  $
  p(X = i) = \binom{n}{i} p^i (1 - p)^{n - i}, \quad i = 0, 1, \ldots, n.
  $

  From `Stat400 teaching material - Jonathan Fernandez`
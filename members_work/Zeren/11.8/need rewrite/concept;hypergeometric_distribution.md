# Concept Node Schema

## Attributes

- **Name**: hypergeometric distribution

- **Definition**:
  Let $X$ be a random variable representing the number of successes in a sample of size $n$ drawn without replacement from a population of size $N$ that contains $m$ successes. Then $X$ is said to be a Hypergeometric random variable with parameters $N$ (the population size), $m$ (the number of successes in the population), and $n$ (the sample size).

  The PMF of such a Hypergeometric random variable is given by
  $
  p(x = i) = \frac{\binom{m}{i} \binom{N - m}{n - i}}{\binom{N}{n}}, \quad i = 0, 1, \ldots, n.
  $

  - **Notation**: 
  $
  X \sim \text{hypergeometric}(n,N,m)
  $, where\
  $X$ is a random variable following the Binomial distribution ($\max(0, n - (N - m)) \leq X \leq \min(n, m)$).\
  $N$ is the population size($N > 1$).\
  $m$ is the the number of successes in the population ($0 \leq m \leq N$).\
  $n$ is the the sample size ($0 \leq n \leq N$).\
  From `Stat400 teaching material - Jonathan Fernandez`
  - **Description**: Proof of $\max(0, n - (N - m)) \leq X \leq \min(n, m)$:
  
  - **Upper Bound: $\min(n, m)$**
   - The maximum number of successes in the sample $X$ is limited by both the sample size $n$ and the total number of successes $m$ in the population.
   - If $n \leq m$, then at most $n$ successes can be drawn.
   - If $m \leq n$, then at most $m$ successes can be drawn.
   - Thus, the maximum possible value of $X$ is $\min(n, m)$.

  - **Lower Bound: $\max(0, n - (N - m))$**
   - The minimum number of successes in the sample $X$ is determined by the number of draws $n$ relative to the total population $N$ and the number of non-successes $N - m$.
   - If there are enough non-successes in the population, it’s possible to draw only non-successes, so the minimum possible $X$ would be 0.
   - However, if $n$ is large relative to the number of non-successes $N - m$, then we are guaranteed to draw at least $n - (N - m)$ successes. This is because if we exhaust all the non-successes, the remaining draws must be successes.
   - Thus, the minimum possible value of $X$ is $\max(0, n - (N - m))$.



# Property Node Schema

## Attributes

- **Name**:
  expected value of binomial distribution

- **Definition**:
  given
  $
  X \sim \text{Binomial}(n,p)
  $
  where:
  $X$ is a random variable following the Binomial distribution. Then we will have

  $
  \mathbb{E}[X] = np
  $

- **Proof**: 

  The **binomial distribution** describes the number of successes in $n$ independent trials, each with a success probability $p$. Let $X \sim \text{Binomial}(n, p)$.

  ### Step 1: Define $X$ as a Sum of Bernoulli Trials

  Let $X = X_1 + X_2 + \dots + X_n$, where each $X_i$ is an independent Bernoulli random variable with:

  $
  P(X_i = 1) = p \quad \text{and} \quad P(X_i = 0) = 1 - p.
  $

  Then, $X$ represents the number of successes in $n$ trials.

  ### Step 2: Expected Value of $X$

  By the **linearity of expectation**,

  $
  E(X) = E(X_1 + X_2 + \dots + X_n) = E(X_1) + E(X_2) + \dots + E(X_n).
  $

  Since each $X_i$ is Bernoulli with expected value $E(X_i) = p$,

  $
  E(X) = np.
  $

  Thus, the **mean of a binomial distribution** is:

  $
  \mu = np.
  $

    From `Stat400 teaching material - Jonathan Fernandez`

    
## Relationships (Edges)

- **is_property_of** ← *Binomial Distribution*
- **is_child_concept_of** ← *expected value of random variable*
# Property Node Schema

## Attributes

- **Name**:
  variance of Binomial Distribution

- **Definition**:
  given
  $
  X \sim \text{Binomial}(n,p)
  $
  where:
  $X$ is a random variable following the Binomial distribution. Then we will have
  $
  \text{Var}(X) = np(1 - p)
  $

- **Proof**: 

  The **binomial distribution** describes the number of successes in $n$ independent trials, each with a success probability $p$. Let $X \sim \text{Binomial}(n, p)$.

  ### Step 1: Define $X$ as a Sum of Bernoulli Trials

  Let $X = X_1 + X_2 + \dots + X_n$, where each $X_i$ is an independent Bernoulli random variable with:

  $
  P(X_i = 1) = p \quad \text{and} \quad P(X_i = 0) = 1 - p.
  $

  Then, $X$ represents the number of successes in $n$ trials.

  ### Step 2: Variance of $X$

  Since $X = X_1 + X_2 + \dots + X_n$ and each $X_i$ is independent, we can use the property that the **variance of the sum of independent variables is the sum of their variances**:

  $
  \text{Var}(X) = \text{Var}(X_1 + X_2 + \dots + X_n) = \text{Var}(X_1) + \text{Var}(X_2) + \dots + \text{Var}(X_n).
  $

  ### Step 3: Variance of Each $X_i$

  Each $X_i$ is a Bernoulli random variable with variance:

  $
  \text{Var}(X_i) = p(1 - p).
  $

  ### Step 4: Substitute into the Variance of $X$

  Since there are $n$ identical terms,

  $
  \text{Var}(X) = n \cdot p(1 - p).
  $

  Thus, the **variance of a binomial distribution** is:

  $
  \sigma^2 = np(1 - p).
  $


    From `Stat400 teaching material - Jonathan Fernandez`

  
## Relationships (Edges)

- **is_property_of** ← *Binomial Distribution*
- **is_child_concept_of** ← *variance of random variable*
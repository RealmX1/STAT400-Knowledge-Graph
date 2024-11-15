# Property Node Schema

## Attributes

- **Name**:
  variance of bernoulli Distribution

- **Definition**:
  given
  $
  X \sim \text{Bernoulli}(p)
  $
  where:
  $X$ is a random variable following the Bernoulli distribution. Then we will have
  $
  \text{Var}(X) = p(1 - p)
  $

- **Proof**: 
  
  Let $X$ be a random variable that follows a Bernoulli distribution with probability $p$:

  $
  X \sim \text{Bernoulli}(p)
  $

  where:
  - $P(X = 1) = p$ (probability of success)
  - $P(X = 0) = 1 - p$ (probability of failure)

  The variance of $X$, denoted $\text{Var}(X)$, is defined as:

  $
  \text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2
  $

  We already know that $\mathbb{E}[X] = p$. Now, let's find $\mathbb{E}[X^2]$.

  Since $X$ can only be 0 or 1, we have $X^2 = X$. Thus:

  $
  \mathbb{E}[X^2] = \mathbb{E}[X] = p
  $

  Now we can substitute into the formula for variance:

  $
  \text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2
  $
  
  $
  \text{Var}(X) = p - p^2
  $

  $
  \text{Var}(X) = p(1 - p)
  $

  Therefore, the **variance** of a Bernoulli distribution is:

  $
  \text{Var}(X) = p(1 - p)
  $

  From `Stat400 teaching material - Jonathan Fernandez`

  
## Relationships (Edges)

- **is_property_of** ← *Bernoulli Distribution*
- **is_child_concept_of** ← *variance of random variable*
- **depends_on** ← *expected value of bernoulli distribution*
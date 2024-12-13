# Property Node Schema

## Attributes

- **Name**: 
  expected value of bernoulli distribution
  - **Aliases**: 
    mean of bernoulli Distribution

- **Definition**: 
given
$
X \sim \text{Bernoulli}(p)
$
where:
$X$ is a random variable following the Bernoulli distribution. Then we will have
$
\mathbb{E}[X] = p
$

- **Proof**:

  Let $X$ be a random variable that follows a Bernoulli distribution with probability $p$:

  $
  X \sim \text{Bernoulli}(p)
  $

  where:
  - $P(X = 1) = p$ (probability of success)
  - $P(X = 0) = 1 - p$ (probability of failure)

  The mean (or expected value) of $X$ is defined as:

  $
  \mathbb{E}[X] = \sum_x x \cdot P(X = x)
  $

  Since $X$ only takes the values 0 and 1, we can rewrite this as:

  $
  \mathbb{E}[X] = 0 \cdot P(X = 0) + 1 \cdot P(X = 1)
  $

  Substitute the probabilities:

  $
  \mathbb{E}[X] = 0 \cdot (1 - p) + 1 \cdot p
  $
  $
  \mathbb{E}[X] = 0 + p = p
  $

  Thus, the **mean** of a Bernoulli distribution is:

  $
  \mathbb{E}[X] = p
  $

  From `Stat400 teaching material - Jonathan Fernandez`

  
## Relationships (Edges)

- **is_property_of** ← *Bernoulli Distribution*
- **is_child_concept_of** ← *expected value of random variable*
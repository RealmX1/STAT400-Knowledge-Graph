# Concept Node

## Attributes

- **Name**: Variance of Distribution
  - **Aliases**: *List of Strings*
    - Variance
  
- **Definition**:
  - **Notation**: $V(X)$
  - **Explanation**: 
    - $X$ 
      - Description: Represents the random variable associated with the distribution.
  - **Example**:
    - $V(X) = \frac{(N+1)(N-1)}{12}$ (for Uniform Distribution)
      - Description: The variance formula for a Uniform Distribution over a discrete space $\{1, 2, \ldots, N\}$.
    - $V(X) = p(1-p)$ (for Bernoulli Distribution)
      - Description: The variance formula for a Bernoulli Distribution, where $p$ is the probability of success.
    - $V(X) = np(1-p)$ (for Binomial Distribution)
      - Description: The variance formula for a Binomial Distribution with $n$ trials and probability of success $p$.
    - $V(X) = \left(\frac{N-n}{N-1} \right)\cdot n\cdot \left(\frac{M}{N}\right)\cdot \left(1-\frac{M}{N} \right)$ (for Hypergeometric Distribution)
      - Description: The variance formula for a Hypergeometric Distribution with parameters $N$, $M$, and $n$.
    - $V(X) = \frac{1-p}{p^2}$ (for Geometric Distribution)
      - Description: The variance formula for a Geometric Distribution where $p$ is the probability of success.
    - $V(X) = \frac{r(1-p)}{p^2}$ (for Negative Binomial Distribution)
      - Description: The variance formula for a Negative Binomial Distribution with $r$ successes and probability of success $p$.
    - $V(X) = \lambda$ (for Poisson Distribution)
      - Description: The variance formula for a Poisson Distribution with rate parameter $\lambda$.
  
- **Description**: Variance of a distribution quantifies its spread or dispersion, indicating how much the values of the random variable deviate from the expected value on average.

## Relationships

- **is_subconcept_of** <- *Concept* [Probability Distribution]
- **is_prerequisite_of** → *Concept* [Expected Value of Distribution]
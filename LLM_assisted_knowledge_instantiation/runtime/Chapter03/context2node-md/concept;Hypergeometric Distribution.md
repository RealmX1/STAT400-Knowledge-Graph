# Hypergeometric Distribution

## Attributes

- **Name**: Hypergeometric Distribution
  - **Aliases**: 
    - Hyper Dist

- **Definition**:
  - **Notation**: 
    - Raw LaTeX: `X \sim \text{Hyper}(N, M, n)`
    - Rendered: $X \sim \text{Hyper}(N, M, n)$
  - **Explanation**:
    - $N$
      - Range: $N \in \mathbb{N}$
      - Description: Total population size
    - $M$
      - Range: $M \in \mathbb{N}$
      - Description: Number of successes in the population
    - $n$
      - Range: $n \in \mathbb{N}$
      - Description: Number of individuals chosen from the population
  - **Example**:
    - $$p_X(x) = \frac{{M \choose x} {N-M \choose n-x}}{{N \choose n}}$$
      - Description: The pmf describes the probability of finding exactly $x$ successes in the sample when sampling without replacement.

- **Description**: 
  - The Hypergeometric Distribution models the number of successes in a sequence of $n$ draws from a finite population of size $N$ containing exactly $M$ successes, without replacement.

## Relationships

- **is_subconcept_of** => (i.e. **has_subconcept** <=) *Concept* [Discrete Distribution]
# Hypergeometric Distribution

## Attributes

- **Name**: Hypergeometric Distribution
  - **Aliases**: 
    - Hypergeometric distribution

- **Definition**:
  - **Notation**: $X \sim \text{Hyper}(N, M, n)$
  - **Explanation**: 
    - $N$
      - Range: $N \in \mathbb{N}$
      - Description: represents the population size.
    - $M$
      - Range: $M \in \mathbb{N}$
      - Description: represents the number of successes in the population.
    - $n$
      - Range: $n \in \mathbb{N}$
      - Description: represents the number of individuals chosen from the population.

  - **Example**:
    - $$p_X(x) = \frac{{N \choose x} {N-M \choose n-x}}{{N \choose n}}\quad \quad x\in \{0,1, 2, 3, \dots, \min(n, M)\}$$
      - Description: Represents the probability mass function of the hypergeometric distribution.

- **Description**: 
  - The hypergeometric distribution models the probability of obtaining a certain number of successes in a sequence of draws from a finite population without replacement. This distribution is useful in situations where each draw significantly changes the composition of the population, distinguishing it from the binomial distribution.

## Relationships

### Relation regarding concept

- **is_subconcept_of** <- *Concept* [Discrete Distribution]
  - The Hypergeometric Distribution is a type of discrete distribution.

- **is_prerequisite_of** → *Concept* [Binomial Distribution]
  - Understanding the Hypergeometric Distribution supports comprehension of the Binomial Distribution, especially in contexts involving sampling.
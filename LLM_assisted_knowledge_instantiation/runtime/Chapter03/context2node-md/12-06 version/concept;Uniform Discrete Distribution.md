# Concept Node: Uniform Discrete Distribution

## Attributes

- **Name**: Uniform Discrete Distribution
  - **Aliases**: 
    - Uniform Distribution

- **Definition**:
  - **Notation**: $X \sim \text{Uniform}(N)$
  - **Explanation**:
    - $X$
      - Description: Represents the random variable.
    - $N$
      - Range: $N \in \mathbb{N}$
      - Description: Represents the maximum value of the discrete set $\{1, 2, 3, \dots, N\}$ on which the uniform distribution is defined.

  - **Example**:
    - $p_X(x) = \frac{1}{N} \quad \text{for all } x \in \X = \{1, 2, 3, \dots, N\}$
      - Description: The probability mass function of a uniform discrete distribution where each value in the set has an equal probability of $\frac{1}{N}$.

- **Description**: 
  - "A uniform discrete distribution is a probability distribution that has constant probability. It is defined over a discrete set of equally-likely values such as $\{1, 2, 3, \cdots, N\}$."

## Relationships

- **is_subconcept_of** <- *Concept* [Discrete Distribution]
  - The uniform discrete distribution is a special case of a discrete distribution where each value has equal probability.

- **is_prerequisite_of** → *Concept* [Discrete Random Variable, Probability Mass Function (PMF)]
  - Understanding the uniform discrete distribution is essential for comprehending how discrete random variables and PMFs work, particularly in evenly distributed datasets.
# Concept Node: Discrete Uniform Distribution

## Attributes

- **Name**: Discrete Uniform Distribution
  - **Aliases**:
    - Uniform Discrete Distribution

- **Definition**:
  - **Notation**: `X \sim \text{Uniform}(\{1, 2, \ldots, N\})`
    - Rendered: \( X \sim \text{Uniform}(\{1, 2, \ldots, N\}) \)
  - **Explanation**:
    - \( X \)
      - Description: Represents a random variable with a discrete uniform distribution.
    - \( N \)
      - Range: \( N \in \mathbb{N} \)
      - Description: Number of distinct outcomes in the discrete set \(\{1, 2, \ldots, N\}\).
    - Other:
      - Range: \( x \in \{1, 2, \ldots, N\} \)
      - Description: Denotes the individual values that \( X \) can take.
  - **Example**:
    - $$p_X(x) = P(X=x) = \frac{1}{N} \quad \quad \text{for all } x \in \{1, 2, \ldots, N\}$$
      - Description: This represents the Probability Mass Function (PMF) of the discrete uniform distribution, where each outcome has an equal probability.

- **Description**: 
  - The discrete uniform distribution describes a situation where a discrete random variable equitably divides probabilities across all possible outcomes. This distribution is characterized by all outcomes being equally likely within its finite set of possibilities.

## Relationships

- **is_subconcept_of** => (i.e. **has_subconcept** <=) *Concept* [Discrete Distribution] 
  - Discrete Distribution has_subconcept Discrete Uniform Distribution

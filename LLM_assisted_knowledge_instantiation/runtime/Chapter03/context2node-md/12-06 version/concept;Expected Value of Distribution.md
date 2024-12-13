# Concept Node

## Attributes

- **Name**: Expected Value of Distribution
  - **Aliases**: 
    - Mean of Distribution
    - Average Value of Distribution

- **Definition**:
  - **Notation**: $E(X)$
  - **Explanation**:
    - $E(X)$
      - Description: Represents the expected value or mean of a random variable $X$. It is the long-run average value of repetitions of the experiment it represents.
  - **Example**:
    - $$E(X) = \frac{N+1}{2}$$
      - Description: This is the expected value for a Uniform Discrete Distribution on the set $\{1, 2, \ldots, N\}$.

- **Description**: 
  - The expected value, often called the mean, of a distribution is a measure of the "center" of the probability distribution. For discrete random variables, it is calculated as the sum of the products of the probabilities and their corresponding values.

## Relationships
### Relation regarding concept

- **is_subconcept_of** <- *Concept* [ProbabilityDistribution]
- **is_prerequisite_of** → *Concept* [Variance of Distribution, Probability Mass Function (PMF)]
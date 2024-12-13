# Property Node: Variance of Poisson Random Variable

## Attributes

- **Name**: Variance of Poisson Random Variable

- **Definition**: The variance of a Poisson random variable is the same as its rate parameter.
  - **Notation**: 
    - Rendered: $V[X \sim \text{Pois}(\lambda)] = \lambda$
    - LaTeX: `V[X \sim \text{Pois}(\lambda)] = \lambda`
    - **Range**: $V[X \sim \text{Pois}(\lambda)] \in \mathbb{R}_{0+}$

- **Description**: 
  - "Variance of Poisson Random Variable quantifies the spread or dispersion of a Poisson-distributed data set. In the Poisson distribution, this value is equal to the expected rate or the lambda parameter."

- **Proof**: 
  To prove that the variance of a Poisson random variable $X \sim \text{Pois}(\lambda)$ is $\lambda$, we can use the definition of variance, $V(X) = E[X^2] - (E[X])^2$. Since $E[X] = \lambda$ for a Poisson distribution, we need to derive $E[X^2]$. By utilizing moment generating functions or using the law of total probability with the fact that $X$ is equal to its expected value, $E[X^2] = \lambda^2 + \lambda$ can be calculated.

## Relationships

- **has_property** <= (i.e. **is_property_of** =>) *Concept*
  - Concept: "Poisson Distribution"; "Poisson Distribution" has_property current property.

- **has_subconcept** <= (i.e. **is_subconcept_of** =>) *Concept*
  - Concept: "Variance of Random Variable"; "Variance of Random Variable" has_subconcept current property.

- **is_prerequisite_of** <= (i.e. **depends_on** =>) *Property*
  - Property: "Expected Value of Poisson Distribution"; "Expected Value of Poisson Distribution" is a prerequisite of current property.
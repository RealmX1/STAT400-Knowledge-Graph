# Property Node

## Attributes

- **Name**: PMF of Discrete Uniform Random Variable
  - **Aliases**: ["Probability Mass Function of Discrete Uniform Distribution"]

- **Definition**: The probability mass function for a discrete uniform random variable is defined such that the probability of each outcome is equal.
  - **Notation**: 
    - LaTeX: `p_X(x) = P(X = x) = \frac{1}{N}, \quad \text{for all } x \in \mathcal{X}`
    - Rendered: \(p_X(x) = P(X = x) = \frac{1}{N}, \quad \text{for all } x \in \mathcal{X}\)
    - **Range**: \(\frac{1}{N}, \quad \forall x \in \{1, 2, 3, \cdots, N\}\)

- **Description**: The PMF of a discrete uniform random variable simplifies the computation since all outcomes are equally likely. Therefore, each individual probability is assigned an equal weight of $\frac{1}{N}$ where $N$ is the total number of discrete outcomes. 

## Relationships

- **has_property** <= (i.e. **is_property_of** =>) *Concept* MUST
  - Concept: Discrete Uniform Distribution

- **has_subconcept** <= (i.e. **is_subconcept_of** =>) *Concept* MUST
  - Concept: Probability Mass Function (PMF)

- **has_subproperty** => (i.e. **is_subproperty_of** <=) *Property*
  - Subproperty: *None explicitly listed*

- **is_prerequisite_of** <= (i.e. **depends_on** =>) *Property*
  - Depends on: *None explicitly listed*

> **Source**: Stat400 teaching material - Jonathan Fernandez
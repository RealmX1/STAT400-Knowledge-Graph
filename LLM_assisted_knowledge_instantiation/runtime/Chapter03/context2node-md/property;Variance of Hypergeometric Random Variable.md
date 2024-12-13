# Property Node

## Attributes

- **Name**: Variance of Hypergeometric Distribution

- **Definition**: For a hypergeometric random variable $X \sim \text{Hyper}(N, M, n)$.
  - **Notation**: 
    - Latex: `V[X] = \left(\frac{N-n}{N-1} \right)\cdot n\cdot \left(\frac{M}{N}\right)\cdot \left(1-\frac{M}{N} \right)`
    - Rendered: $V[X] = \left(\frac{N-n}{N-1} \right)\cdot n\cdot \left(\frac{M}{N}\right)\cdot \left(1-\frac{M}{N} \right)$
    - **Range**: \(V[X] \geq 0\)

- **Description**: Variance of the Hypergeometric Distribution measures the spread of the number of successes in the sampled group compared to what is expected on average. This is impacted by the distribution of successes in the overall population, the population size, and the sample size.

- **Proof**: *The variance is derived using the formula for variance of a discrete random variable.*

## Relationships

- **has_property** <= (i.e. **is_property_of** =>) *Concept*
  - **Target**: Hypergeometric Distribution

- **has_subconcept** <= (i.e. **is_subconcept_of** =>) *Concept*
  - **Target**: Variance of random variable
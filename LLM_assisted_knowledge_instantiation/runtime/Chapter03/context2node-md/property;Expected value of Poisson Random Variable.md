# Property Node

## Attributes

- **Name**: Expected value of Poisson Distribution
  - **Aliases**: ["Mean of Poisson Distribution"]

- **Definition**: The expected value of a Poisson distributed random variable
  - **Notation**:
    - Latex: `E(X) = \lambda`
    - Rendered: $E(X) = \lambda$
    - **Range**: $E(X) \in \{0, \infty\}$

- **Description**: The expected value of a Poisson distribution indicates the average number of events in the given interval. It is equal to the parameter $\lambda$ of the distribution which represents the rate at which events occur.

- **Proof**: The expected value of a Poisson random variable can be demonstrated by calculating the sum of $k \cdot P(X = k)$ for all $k$, which simplifies to $\lambda$. [Source: Stat400 teaching material - Jonathan Fernandez]

## Relationships

- **has_property** <= (i.e. **is_property_of** =>) *Concept*
  - Poisson Distribution
- **has_subconcept** <= (i.e. **is_subconcept_of** =>) *Concept*
  - Expected value of random variable
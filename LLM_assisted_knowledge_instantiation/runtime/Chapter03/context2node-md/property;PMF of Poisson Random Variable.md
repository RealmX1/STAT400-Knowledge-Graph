# Property Node: PMF of Poisson Distribution

## Attributes

- **Name**: PMF of Poisson Distribution
  - **Aliases**: ["Probability Mass Function of Poisson Distribution"]

- **Definition**: 
  - **Notation**: 
    - LaTeX: `p_X(x) = e^{-\lambda} \frac{\lambda^k}{k!}` 
    - Rendered: $p_X(x) = e^{-\lambda} \frac{\lambda^k}{k!}$
    - **Range**: $p_X(x) \in [0, 1]$ for $x \in \mathbb{N}$ or $x = 0, 1, 2, \dots$

- **Description**: The Probability Mass Function (PMF) of the Poisson Distribution gives the probability of observing exactly $k$ events in an interval, given the average or expected number of event occurrences $\lambda$.

- **Proof**: *The validation of this as a probability mass function can be seen via the series expansion of the exponential function:*

  $$e^\lambda = \sum_{k=0}^\infty \frac{\lambda^k}{k!}$$

  *Thus, the sum of probabilities over all possible $k$ equals 1.*

## Relationships

- **has_property** <= (i.e. **is_property_of** =>) *Concept*
  - Poisson Distribution

- **has_subconcept** <= (i.e. **is_subconcept_of** =>) *Concept*
  - Probability Mass Function (PMF)
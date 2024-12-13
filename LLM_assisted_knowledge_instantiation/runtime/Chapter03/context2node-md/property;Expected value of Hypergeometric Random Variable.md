# Property Node: Expected value of Hypergeometric Distribution

## Attributes

- **Name**: Expected Value of Hypergeometric Distribution
  - **Aliases**: ["Mean of Hypergeometric Distribution"]

- **Definition**: 
  Let $X \sim \text{Hyper}(N, M, n)$, where $N$ is the population size, $M$ is the number of successes in the population, and $n$ is the number of individuals chosen from the population.
  - **Notation**: 
    - Raw LaTeX: `E[Hyper(N, M, n)] = n \left(\frac{M}{N}\right)`
    - Rendered: $E[Hyper(N, M, n)] = n \left(\frac{M}{N}\right)$
  - **Range**: 
    - Raw LaTeX: `E[Hyper(N, M, n)] \in [0, min(n, M)]`
    - Rendered: $E[Hyper(N, M, n)] \in [0, \min(n, M)]$

- **Description**: 
  The expected value of the Hypergeometric Distribution is the average number of successes observed when $n$ individuals are chosen from a population of size $N$ containing $M$ successes without replacement. It captures the average outcome in terms of success count in simple random sampling from a finite population.

- **Proof**: 
  > NEED TO mark SOURCE for the information used here. By default we will use `Stat400 teaching material - Jonathan Fernandez`
  *Proof*: 
  The expectation of a Hypergeometric random variable can be derived using the linearity of expectation and considering it as a sum of indicators for success in each of the $n$ draws. Each draw has a probability of success $\frac{M}{N}$. Hence, the expected number of successes is the product of the number of draws and the probability of success in each draw: 
  \[
  E(X) = n \cdot \frac{M}{N}
  \]

## Relationships

- **has_property** <= (i.e. **is_property_of** =>) *Concept* MUST
  - Hypergeometric Distribution

- **has_subconcept** <= (i.e. **is_subconcept_of** =>) *Concept* MUST
  - Expected Value of Random Variable
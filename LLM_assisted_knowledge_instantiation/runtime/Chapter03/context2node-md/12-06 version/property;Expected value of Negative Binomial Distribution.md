# Property Node

## Attributes

- **Name**: Expected value of Negative Binomial Distribution
  - **Aliases**: ["Mean of Negative Binomial Distribution", "Expected Value"]

- **Definition**: 
  - **Notation**: 
    - Latex: `E[NegBinom(r, p)] = \frac{r(1-p)}{p}`
    - Rendered: $E[NegBinom(r, p)] = \frac{r(1-p)}{p}$
    - **Range**: N/A

- **Description**: The expected value of a Negative Binomial Distribution represents the average number of failures before achieving the $r^{th}$ success in a sequence of independent Bernoulli trials, where each trial has a probability $p$ of success.

- **Proof**: *The proof involves demonstrating that the expected number of failures before $r$ successes in a sequence of Bernoulli trials can be modeled with the given formula. This typically involves techniques such as generating functions or using properties of expectation derived from simpler distributions. Source: Stat400 teaching material - Jonathan Fernandez.*

## Relationships

- **is_property_of**: Negative Binomial Distribution
- **is_child_concept_of**: Expected Value of Distribution
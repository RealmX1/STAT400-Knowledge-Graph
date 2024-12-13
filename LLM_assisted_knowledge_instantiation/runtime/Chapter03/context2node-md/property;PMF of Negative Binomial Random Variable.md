# Property Node

## Attributes

- **Name**: PMF of Negative Binomial Distribution
  - **Aliases**: ["Probability Mass Function of Negative Binomial Distribution"]

- **Definition**: The PMF of the Negative Binomial Distribution, typically denoted by $X \sim \text{NegBinom}(r, p)$ is given by the formula:
  - **Notation**:
    - Latex: `p_X(x) = {x+r-1 \choose x}p^r(1-p)^x` 
    - Rendered: $p_X(x) = {x+r-1 \choose x}p^r(1-p)^x$
    - **Range**: $x\in \{0,1, 2, 3, \dots \}$
  
- **Description**: The probability mass function for a Negative Binomial distribution gives the probability of $X$ number of failures before achieving $r$ successes in a series of independent Bernoulli trials, where each trial has a probability $p$ of success.

- **Proof**:
  To determine the PMF, consider the sample space consisting of all possible sequences of failures and successes, stopping at exactly the $r$th success. The binomial coefficient counts the number of ways to arrange $x$ failures among the trials needed to achieve $r$ successes. This PMF thus embodies both the sequence's ordering and the fixed number of successes needed.
  > *SOURCE: Stat400 teaching material - Jonathan Fernandez*

## Relationships

- **has_property** <= (i.e. **is_property_of** =>) *Concept* Negative Binomial Distribution
  - The **Negative Binomial Distribution** has_property the current property.

- **has_subconcept** <= (i.e. **is_subconcept_of** =>) *Concept* Probability Mass Function (PMF)
  - The current property "PMF of Negative Binomial Distribution" is a subconcept of "Probability Mass Function"; "Probability Mass Function" has_subconcept the current property.
# Property Node: Expected value of Binomial Random Variable

## Attributes

- **Name**: Expected value of Binomial Random Variable
  - **Aliases**: ["Expected Value", "Mean of Binomial Distribution"]

- **Definition**: The expected value of a Binomial random variable quantifies the average number of successful outcomes for a given number of trials.
  - **Notation**: 
    - Latex: `E[X] = np` 
    - Rendered: $E[X] = np$
    - **Range**: $E[X] \in \{0, n\}$

- **Description**: The expected value for a Binomial random variable $X$, which is represented as $X \sim \text{Binomial}(n, p)$, is determined by multiplying the number of trials $n$ by the probability $p$ of success in each trial. It represents the average number of successes in $n$ trials when each trial has an identical probability of success.

- **Proof**: The expectation of a Binomial Random Variable $X \sim \text{Binomial}(n, p)$ can be derived using the linearity of expectation. For each of the $n$ trials, the expected value of getting a success is $p$, hence the total expectation across all trials is $n \cdot p$.
  > SOURCE: Stat400 teaching material - Jonathan Fernandez

## Relationships

- **has_property** <= (i.e. **is_property_of** =>) *Concept*
  - Binomial Distribution

- **has_subconcept** <= (i.e. **is_subconcept_of** =>) *Concept*
  - Expected Value of Random Variable
# Negative Binomial Distribution Node

## Attributes

- **Name**: Negative Binomial Distribution

- **Aliases**: 
  - NegBinom Distribution
  - Pascal Distribution

- **Definition**:
  - **Notation**: 
    - Latex: `NegBinom(r, p)` 
    - Rendered: $X \sim \text{NegBinom}(r, p)$
  - **Explanation**: 
    - $r$
      - Range: $r \in \mathbb{N}$
      - Description: The number of successes we are waiting for.
    - $p$
      - Range: $p \in (0, 1)$
      - Description: The probability of a success in each trial.
  - **Example**:
    - $$p_X(x) = {x+r-1 \choose x}p^r(1-p)^x\quad \quad x\in \{0,1, 2, 3, \dots, \}$$
      - Description: The probability mass function (pmf) of the negative binomial distribution, representing the probability of observing $x$ failures before achieving $r$ successes.

- **Description**: 
  - The Negative Binomial Distribution models phenomena that involve "waiting" for a specified number of successes in a sequence of independent and identically distributed Bernoulli trials. It calculates probabilities in terms of counting the number of failures preceding these successes. 

## Relationships

- **is_subconcept_of** => (i.e. **has_subconcept** <=) *Concept* [Discrete Distribution] 
  - A parent concept "Discrete Distribution" has current concept "Negative Binomial Distribution" as a subconcept.
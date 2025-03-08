# Concept Node: Bernoulli Distribution

## Attributes

- **Name**: Bernoulli Distribution
  - **Aliases**: 
    - Bernoulli Trial
- **Definition**:
  - **Notation**: 
    - Latex: `Bernoulli(p)`
    - Rendered: $X \sim \text{Bernoulli}(p)$ 
  - **Explanation**:
    - $X$
      - Description: A random variable representing the outcome of a Bernoulli trial.
    - $p$
      - Range: $p \in (0,1)$
      - Description: The probability of success in the trial.
  - **Example**:
    - $$p_X(x) = p^x(1-p)^{(1-x)}\quad \quad x\in \{0,1\}$$
      - Description: The probability mass function of a Bernoulli random variable, where $x = 0$ indicates a failure and $x = 1$ indicates a success.

- **Description**: 
  - The Bernoulli distribution models a single trial experiment that has exactly two possible outcomes: success and failure. It is often used to model scenarios where you are interested in the probability of success in a single binary event.

## Relationships

- **is_subconcept_of** => Discrete Distribution, Bernoulli Trial

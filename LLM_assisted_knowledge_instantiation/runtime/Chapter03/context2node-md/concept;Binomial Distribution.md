# Binomial Distribution

## Attributes

- **Name**: Binomial Distribution
  - **Aliases**: 
    - *None*

- **Definition**:
  - **Notation**: 
    - Rendered: $X \sim \text{Binomial}(n, p)$
    - Latex: `X \sim \text{Binomial}(n, p)` 
  - **Explanation**:
    - $n$
      - Range: $n \in \mathbb{N}$
      - Description: The number of trials.
    - $p$
      - Range: $p \in (0,1)$
      - Description: The probability of success in each trial.
  - **Example**:
    - $$p_X(x) = {n \choose x} p^x(1-p)^{(n-x)}$$
      - Description: Represents the probability of having exactly $x$ successes in $n$ independent $\text{Bernoulli}(p)$ trials.

- **Description**: 
  - The Binomial Distribution models the number of successes in a fixed number of independent trials of a binary experiment. Each trial is assumed to have the same probability of success. It is used to solve problems involving scenarios with a fixed number of trials or observations and binary outcomes.

## Relationships

- **is_subconcept_of** => (i.e. **has_subconcept** <=) *Concept* "Discrete Distribution" 
  - "Binomial Distribution" is a subconcept of "Discrete Distribution"
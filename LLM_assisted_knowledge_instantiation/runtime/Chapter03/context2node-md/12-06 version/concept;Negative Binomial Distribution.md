# Negative Binomial Distribution

## Attributes

- **Name**: Negative Binomial Distribution
  - **Aliases**: 
    - *No specific aliases noted for Negative Binomial Distribution in the context.*

- **Definition**:
  - **Notation**: $NegBinom(r, p)$
  - **Explanation**:
    - $r$ 
      - Range: $r \in \mathbb{N}$
      - Description: Number of successes we are waiting for.
    - $p$
      - Range: $p\in (0,1)$
      - Description: Probability of a success.
    - $p_X(x) = {x+r-1 \choose x}p^r(1-p)^x$
      - Description: Probability mass function for a negative binomial distribution representing the probability of $x$ failures before $r$ successes.
  - **Example**:
    - $$X \sim NegBinom(r, p)$$
      - Description: Denotes a random variable $X$ following a negative binomial distribution with $r$ successes and probability $p$ for a success.

- **Description**: 
  - The Negative Binomial Distribution models phenomena where the outcome is the number of failures before a specified number of successes in a series of independent Bernoulli trials. This distribution is applicable in scenarios involving waiting for a predetermined number of successes.

## Relationships

### Relation regarding concept

- **is_subconcept_of** <- *Concept* Discrete Distribution
- **is_prerequisite_of** → *Concept* Bernoulli Trial
  - Indicates that understanding Bernoulli Trials is a prerequisite for understanding the Negative Binomial Distribution.
# Concept Node: Bernoulli Distribution

## Attributes

- **Name**: Bernoulli Distribution
  - **Aliases**:
    - Bernoulli trial distribution

- **Definition**:
  - **Notation**: $X \sim \text{Bernoulli}(p)$
  - **Explanation**:
    - $X$
      - Description: Random variable representing the outcome of a single Bernoulli trial.
    - $p$
      - Range: $p \in (0,1)$
      - Description: The probability of a success in a Bernoulli trial.
  - **Example**:
    - $$p_X(x) = \begin{cases}
        1-p \quad \text{if $x=0$}\\
        p \quad \text{if $x=1$}
    \end{cases}$$
      - Description: The probability mass function (PMF) for a Bernoulli distribution representing the probabilities of a single trial resulting in success or failure.

- **Description**: 
  The Bernoulli distribution simulates a single "trial" with two possible outcomes: success or failure. The Bernoulli distribution is characterized by the parameter $p$, which represents the probability of success. It is the simplest form of a discrete probability distribution and a foundational building block for other distributions, such as the Binomial distribution.

## Relationships

- **is_subconcept_of** <- *Concept* [Discrete Distribution]
- **is_prerequisite_of** → *Concept* [Binomial Distribution, Geometric Distribution, Negative Binomial Distribution]
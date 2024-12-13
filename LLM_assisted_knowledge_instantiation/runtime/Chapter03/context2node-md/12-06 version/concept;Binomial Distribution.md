# Binomial Distribution

## Attributes

- **Name**: Binomial Distribution
  - **Aliases**: 
    - Binomial RV
    - Binomial Random Variable

- **Definition**:
  - **Notation**: 
    - $X \sim \text{Binomial}(n, p)$
  - **Explanation**: 
    - $n$
      - Range: $n \in \mathbb{N}$
      - Description: Number of independent Bernoulli trials
    - $p$ 
      - Range: $p \in (0,1)$
      - Description: Probability of success in each trial
  - **Example**:
    - $$p_X(x) = {n \choose x} p^x(1-p)^{(n-x)}\quad \quad x\in \{0,1, 2, 3, \dots, n\}$$
      - Description: Probability mass function of the number of successes in $n$ trials.

- **Description**: 
  - The Binomial Distribution models the number of successes in a sequence of $n$ independent experiments (Bernoulli trials), where each experiment results in a success with probability $p$. This distribution is commonly used in scenarios such as quality testing, genetics, and operational research where binary outcomes are involved. It is characterized by the parameters $n$, the number of trials, and $p$, the probability of success.

## Relationships

### Relation regarding concept

- **is_subconcept_of** <- *Concept* [Discrete Distribution]
  - The Binomial Distribution is a type of discrete distribution.

- **is_prerequisite_of** → *Concept* [Poisson Distribution, Hypergeometric Distribution]
  - Understanding the Binomial Distribution is beneficial for comprehending related distributions like the Poisson and Hypergeometric distributions, especially in contexts involving approximations and inferences related to independent trials.
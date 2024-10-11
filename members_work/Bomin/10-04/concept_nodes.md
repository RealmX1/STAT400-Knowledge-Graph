
# Uniform Discrete Distribution

**Aliases**: ["Discrete Uniform Distribution"]


## Definition

The **Uniform Discrete Distribution** is a probability distribution where a discrete random variable \( X \) takes on a finite number of equally spaced values, each with equal probability.

**Notation**:

- LaTeX code: `X \sim \text{Uniform}(1, N)`
- Rendered: \( X \sim \text{Uniform}(1, N) \)

**Probability Mass Function (PMF)**:

- LaTeX code: `p_X(x) = \frac{1}{N}, \quad x \in \{1, 2, \dots, N\}`
- Rendered: \( p_X(x) = \frac{1}{N}, \quad x \in \{1, 2, \dots, N\} \)

**Description**:

A random variable \( X \) has a Uniform Discrete Distribution with parameter \( N \in \mathbb{N} \) if it is supported on \( \mathcal{X} = \{1, 2, 3, \dots, N\} \) and each outcome is equally likely. This implies that the probability mass function (PMF) is constant over its support.

**Source**: Stat400 teaching material - Jonathan Fernandez


## Tags/Categories

- Probability Theory
- Statistics
- Discrete Distribution
- Uniform Distribution


## Properties

- **Expected Value**:
  - Formula: \( E(X) = \frac{N + 1}{2} \)
- **Variance**:
  - Formula: \( V(X) = \frac{(N + 1)(N - 1)}{12} \)


## Relationships

- **has_property**:
  - Expected Value
  - Variance
- **related_to**:
  - Continuous Uniform Distribution
- **involved_in_theorem**:
  - Parameters associated with the Uniform Distribution


# Bernoulli Distribution

**Aliases**: None


## Definition

The **Bernoulli Distribution** models a random experiment with exactly two outcomes: success (1) and failure (0).

**Notation**:

- LaTeX code: `X \sim \text{Bernoulli}(p)`
- Rendered: \( X \sim \text{Bernoulli}(p) \)

**Probability Mass Function (PMF)**:

- LaTeX code:
  ```latex
  p_X(x) = \begin{cases}
    1 - p & \text{if } x = 0, \\
    p & \text{if } x = 1.
  \end{cases}
  ```
- Rendered:
  \[
  p_X(x) = \begin{cases}
    1 - p & \text{if } x = 0, \\
    p & \text{if } x = 1.
  \end{cases}
  \]

Alternative form:

- LaTeX code: `p_X(x) = p^x (1 - p)^{1 - x}, \quad x \in \{0, 1\}`
- Rendered: \( p_X(x) = p^x (1 - p)^{1 - x}, \quad x \in \{0, 1\} \)

**Description**:

A random variable \( X \) has the Bernoulli Distribution with parameter \( p \in (0, 1) \) if it represents the outcome of a single Bernoulli trial, where \( p \) is the probability of success. It is the simplest discrete distribution and forms the building block for the Binomial Distribution.

**Source**: Stat400 teaching material - Jonathan Fernandez


## Tags/Categories

- Probability Theory
- Statistics
- Discrete Distribution
- Bernoulli Trial


## Properties

- **Expected Value**:
  - Formula: \( E(X) = p \)
- **Variance**:
  - Formula: \( V(X) = p(1 - p) \)


## Relationships

- **has_property**:
  - Expected Value
  - Variance
- **related_to**:
  - Binomial Distribution
- **involved_in_theorem**:
  - Parameters associated with the Bernoulli Distribution
- **has_application**:
  - Modeling success/failure experiments like coin tosses, quality control tests, and yes/no surveys.


# Binomial Distribution

**Aliases**: None


## Definition

The **Binomial Distribution** models the number of successes in a fixed number of independent Bernoulli trials.

**Notation**:

- LaTeX code: `X \sim \text{Binomial}(n, p)`
- Rendered: \( X \sim \text{Binomial}(n, p) \)

**Probability Mass Function (PMF)**:

- LaTeX code: `p_X(x) = \binom{n}{x} p^x (1 - p)^{n - x}, \quad x = 0, 1, \dots, n`
- Rendered: \( p_X(x) = \binom{n}{x} p^x (1 - p)^{n - x}, \quad x = 0, 1, \dots, n \)

**Description**:

A random variable \( X \) has the Binomial Distribution with parameters \( n \in \mathbb{N} \) and \( p \in (0, 1) \) if it represents the number of successes in \( n \) independent Bernoulli trials each with success probability \( p \).

**Source**: Stat400 teaching material - Jonathan Fernandez


## Tags/Categories

- Probability Theory
- Statistics
- Discrete Distribution
- Bernoulli Trials


## Properties

- **Expected Value**:
  - Formula: \( E(X) = np \)
- **Variance**:
  - Formula: \( V(X) = np(1 - p) \)


## Relationships

- **has_property**:
  - Expected Value
  - Variance
- **related_to**:
  - Bernoulli Distribution
  - Poisson Distribution (as an approximation)
- **involved_in_theorem**:
  - Parameters associated with the Binomial Distribution
- **has_application**:
  - Used in scenarios like quality control, clinical trials, and survey sampling where the outcome is the number of successes in a series of independent trials.


# Hypergeometric Distribution

**Aliases**: None


## Definition

The **Hypergeometric Distribution** models the number of successes in a sequence of draws from a finite population without replacement.

**Notation**:

- LaTeX code: `X \sim \text{Hypergeometric}(N, M, n)`
- Rendered: \( X \sim \text{Hypergeometric}(N, M, n) \)

**Probability Mass Function (PMF)**:

- LaTeX code: `p_X(x) = \frac{\binom{M}{x} \binom{N - M}{n - x}}{\binom{N}{n}}, \quad x = 0, 1, \dots, \min(n, M)`
- Rendered: \( p_X(x) = \frac{\binom{M}{x} \binom{N - M}{n - x}}{\binom{N}{n}}, \quad x = 0, 1, \dots, \min(n, M) \)

**Description**:

A random variable \( X \) has the Hypergeometric Distribution with parameters \( N \) (population size), \( M \) (number of successes in the population), and \( n \) (number of draws) when sampling is done without replacement. Unlike the Binomial Distribution, trials are not independent.

**Source**: Stat400 teaching material - Jonathan Fernandez


## Tags/Categories

- Probability Theory
- Statistics
- Discrete Distribution
- Sampling Without Replacement


## Properties

- **Expected Value**:
  - Formula: \( E(X) = n \left( \dfrac{M}{N} \right) \)
- **Variance**:
  - Formula: \( V(X) = n \left( \dfrac{M}{N} \right) \left( 1 - \dfrac{M}{N} \right) \left( \dfrac{N - n}{N - 1} \right) \)


## Relationships

- **has_property**:
  - Expected Value
  - Variance
- **related_to**:
  - Binomial Distribution (approximates Binomial when \( N \) is large)
- **involved_in_theorem**:
  - Parameters associated with the Hypergeometric Distribution
- **has_application**:
  - Used in quality control and lotteries where sampling is without replacement.


# Geometric Distribution

**Aliases**: None


## Definition

The **Geometric Distribution** models the number of trials needed to get the first success in repeated independent Bernoulli trials.

**Notation**:

- LaTeX code: `X \sim \text{Geom}(p)`
- Rendered: \( X \sim \text{Geom}(p) \)

**Probability Mass Function (PMF)**:

- LaTeX code: `p_X(x) = p(1 - p)^{x - 1}, \quad x = 1, 2, 3, \dots`
- Rendered: \( p_X(x) = p(1 - p)^{x - 1}, \quad x = 1, 2, 3, \dots \)

**Description**:

A random variable \( X \) has the Geometric Distribution with parameter \( p \in (0, 1) \) if it represents the number of trials required to achieve the first success in independent Bernoulli trials.

**Source**: Stat400 teaching material - Jonathan Fernandez


## Tags/Categories

- Probability Theory
- Statistics
- Discrete Distribution
- Waiting Time


## Properties

- **Expected Value**:
  - Formula: \( E(X) = \dfrac{1}{p} \)
- **Variance**:
  - Formula: \( V(X) = \dfrac{1 - p}{p^2} \)


## Relationships

- **has_property**:
  - Expected Value
  - Variance
- **related_to**:
  - Negative Binomial Distribution
- **involved_in_theorem**:
  - Parameters associated with the Geometric Distribution
- **has_application**:
  - Used in modeling the number of trials until first success in scenarios like quality control testing and reliability analysis.


# Negative Binomial Distribution

**Aliases**: None


## Definition

The **Negative Binomial Distribution** generalizes the Geometric Distribution by modeling the number of failures before achieving a specified number of successes.

**Notation**:

- LaTeX code: `X \sim \text{NegBinomial}(r, p)`
- Rendered: \( X \sim \text{NegBinomial}(r, p) \)

**Probability Mass Function (PMF)**:

- LaTeX code: `p_X(x) = \binom{x + r - 1}{x} p^r (1 - p)^x, \quad x = 0, 1, 2, \dots`
- Rendered: \( p_X(x) = \binom{x + r - 1}{x} p^r (1 - p)^x, \quad x = 0, 1, 2, \dots \)

**Description**:

A random variable \( X \) has the Negative Binomial Distribution with parameters \( r \in \mathbb{N} \) and \( p \in (0, 1) \) if it represents the number of failures before achieving \( r \) successes in independent Bernoulli trials.

**Source**: Stat400 teaching material - Jonathan Fernandez


## Tags/Categories

- Probability Theory
- Statistics
- Discrete Distribution
- Waiting Time


## Properties

- **Expected Value**:
  - Formula: \( E(X) = \dfrac{r(1 - p)}{p} \)
- **Variance**:
  - Formula: \( V(X) = \dfrac{r(1 - p)}{p^2} \)


## Relationships

- **has_property**:
  - Expected Value
  - Variance
- **related_to**:
  - Geometric Distribution (special case when \( r = 1 \))
- **involved_in_theorem**:
  - Parameters associated with the Negative Binomial Distribution
- **has_application**:
  - Used in modeling the number of trials required to achieve a specified number of successes, such as in insurance claims or equipment failure.


# Poisson Distribution

**Aliases**: None


## Definition

The **Poisson Distribution** models the number of events occurring in a fixed interval of time or space when events occur independently and at a constant average rate.

**Notation**:

- LaTeX code: `X \sim \text{Poisson}(\lambda)`
- Rendered: \( X \sim \text{Poisson}(\lambda) \)

**Probability Mass Function (PMF)**:

- LaTeX code: `p_X(x) = e^{-\lambda} \dfrac{\lambda^x}{x!}, \quad x = 0, 1, 2, \dots`
- Rendered: \( p_X(x) = e^{-\lambda} \dfrac{\lambda^x}{x!}, \quad x = 0, 1, 2, \dots \)

**Description**:

A random variable \( X \) has the Poisson Distribution with parameter \( \lambda > 0 \) if it represents the number of events occurring in a fixed period of time or space, with the events happening independently and at a constant rate.

**Source**: Stat400 teaching material - Jonathan Fernandez


## Tags/Categories

- Probability Theory
- Statistics
- Discrete Distribution
- Poisson Process


## Properties

- **Expected Value**:
  - Formula: \( E(X) = \lambda \)
- **Variance**:
  - Formula: \( V(X) = \lambda \)


## Relationships

- **has_property**:
  - Expected Value
  - Variance
- **related_to**:
  - Binomial Distribution (Poisson approximation to the Binomial)
- **involved_in_theorem**:
  - Parameters associated with the Poisson Distribution
- **has_application**:
  - Used in modeling the number of occurrences of rare events in fields like telecommunications (number of calls), astronomy (number of meteors), and finance (number of defaults).


# Relationships Between Distributions

While not a separate concept node, it's important to note the relationships between these distributions:

- **Binomial and Hypergeometric**: When the population size \( N \) is large compared to the sample size \( n \), the Hypergeometric Distribution approximates the Binomial Distribution.
- **Binomial and Poisson**: For large \( n \) and small \( p \) such that \( np = \lambda \), the Binomial Distribution approximates the Poisson Distribution.

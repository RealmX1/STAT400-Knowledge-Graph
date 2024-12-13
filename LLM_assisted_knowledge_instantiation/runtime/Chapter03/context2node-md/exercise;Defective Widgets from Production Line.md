# Exercise Node

## Attributes

- **Name**: Defective Widgets from Production Line

- **Problem Statement**: 
  A production line produces widgets. The probability of a widget being defective is 0.05. Assuming independence, and that 20 widgets are checked, what is the probability that exactly 2 widgets are defective? What is the variance and expected value of the number of defective widgets?

  - **Notation**:
    - "Probability of a widget being defective: \( p = 0.05 \)"
    - "Number of widgets checked: \( n = 20 \)"
    - "Probability of exactly 2 defective widgets, \( P(X = 2) \), where \( X \sim \text{Binomial}(n = 20, p = 0.05) \)"
    - "Expected value, \( E(X) = np \)"
    - "Variance, \( V(X) = np(1-p) \)"

- **Solution**: 
  To solve this problem, we model the situation using the Binomial distribution with parameters \( n = 20 \) and \( p = 0.05 \).

  **Step-by-Step Explanation**:
  1. Identify the distribution parameters: \( n = 20 \), \( p = 0.05 \).
  2. Calculate the probability of exactly 2 defective widgets using the binomial probability mass function:
     \[
     P(X = 2) = \binom{20}{2} (0.05)^2 (0.95)^{18}
     \]
  3. Compute the expected value and variance:
     \[
     E(X) = np = 20 \times 0.05 = 1
     \]
     \[
     V(X) = np(1-p) = 20 \times 0.05 \times 0.95 = 0.95
     \]

- **Hints**:
  - Recall the Binomial distribution formula \( P(X = k) = \binom{n}{k} p^k (1-p)^{n-k} \).
  - The expected value of a binomially distributed variable is \( E(X) = np \).
  - The variance of a binomially distributed variable is \( V(X) = np(1-p) \).

- **Difficulty Level**: Beginner

## Relationships

- **has_exercise** <= (i.e. **is_exercise_for** =>) *Concept* [Binomial Distribution]

- **involved_in_exercise** <= (i.e. **involves_xxx** =>) *Concept* [Probability Mass Function, Expected Value, Variance]
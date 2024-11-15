# Property Node Schema

## Attributes

- **Name**:
  expectation and variance of hypergeometric Distribution

- **Definition**:
  given
  $
  X \sim \text{hypergeometric}(n,N,m)
  $
  where:
  $X$ is a random variable following the hypergeometric distribution. Letting $p=\frac{m}{N}$, then we will have

  $
  \mathbb{E}[X] = np
  $



- **Proof**: 

 Here is the proof for the **expected value** and **variance** of a random variable \( X \) following the **hypergeometric distribution** \( X \sim \text{hypergeometric}(n, N, m) \), where:

- \( N \): Total population size,
- \( m \): Number of successes in the population,
- \( n \): Number of draws,
- \( X \): Number of successes in \( n \) draws.

---

## 1. **Expected Value of \( X \)**

The probability mass function of the hypergeometric distribution is:

\[
P(X = k) = \frac{\binom{m}{k} \binom{N-m}{n-k}}{\binom{N}{n}}, \quad \text{for } \max(0, n - (N - m)) \leq k \leq \min(n, m).
\]

The expected value of \( X \) is given by:

\[
E[X] = \sum_{k} k \cdot P(X = k).
\]

Instead of calculating this sum directly, we use the fact that \( X \sim \text{hypergeometric}(n, N, m) \) is equivalent to the number of successes in \( n \) draws without replacement. The expected value can be derived intuitively as the proportion of successes in the population multiplied by the number of draws:

\[
E[X] = n \cdot \frac{m}{N}.
\]

### Proof:
Each draw is a Bernoulli random variable with success probability \( \frac{m}{N} \), and there are \( n \) draws. By the **linearity of expectation**, the expected number of successes is:

\[
E[X] = n \cdot \frac{m}{N}.
\]

---

## 2. **Variance of \( X \)**

The variance of \( X \) for a hypergeometric distribution is:



### Proof:
The hypergeometric distribution is similar to a binomial distribution but with sampling without replacement. The variance is reduced by the finite population correction factor \( \frac{N - n}{N - 1} \), compared to a binomial distribution. The components of the variance are:

1. \( n \): Number of draws,
2. \( \frac{m}{N} \): Proportion of successes in the population,
3. \( 1 - \frac{m}{N} \): Proportion of failures,
4. \( \frac{N - n}{N - 1} \): Correction factor for sampling without replacement.

By combining these components, we obtain:

\[
\text{Var}(X) = n \cdot \frac{m}{N} \cdot \left(1 - \frac{m}{N}\right) \cdot \frac{N - n}{N - 1}.
\]

---

### Summary of Results:

- **Expected Value**:
  \[
  E[X] = n \cdot \frac{m}{N}.
  \]

- **Variance**:
  \[
  \text{Var}(X) = n \cdot \frac{m}{N} \cdot \left(1 - \frac{m}{N}\right) \cdot \frac{N - n}{N - 1}.
  \]

  

## Relationships (Edges)

- **is_property_of** ← *hypergeometric Distribution*
- **is_child_concept_of** ← *mean and/or variance of random variable*
# Exercise Node: Coin Flip

## Attributes

- **Name**: Coin Flip

- **Problem Statement**: Consider a single flip of a fair coin. Determine the probability distribution of this experiment using a Bernoulli distribution. Calculate the expected value and variance for the distribution.

  - **Notation**: "$X \sim \text{Bernoulli}(p)$" denotes the Bernoulli distribution, where $X$ represents the outcome of the coin flip.

- **Solution**: 

  For a fair coin flip, the probability of getting heads (success) is $p = \frac{1}{2}$. The Bernoulli distribution for this experiment is:

  $$p_X(x) = \begin{cases}
      1-p = \frac{1}{2} \quad \text{if $x=0$ (failure)}\\
      p = \frac{1}{2} \quad \text{if $x=1$ (success)}
  \end{cases}$$

  Using the parameters associated with the Bernoulli distribution:

  - **Expected Value**: The expected value $E(X)$ is given by $E(X) = p = \frac{1}{2}$.

  - **Variance**: The variance $V(X)$ is given by $V(X) = p(1-p) = \frac{1}{2}(\frac{1}{2}) = \frac{1}{4}$.

  - **Step-by-Step Explanation**:
    - Step 1: Recognize the coin flip as a Bernoulli trial with $p = \frac{1}{2}$.
    - Step 2: Use the Bernoulli distribution probability mass function formula.
    - Step 3: Calculate the expected value $E(X) = p$.
    - Step 4: Calculate the variance $V(X) = p(1-p)$.

- **Hints**:
  - Recall that a fair coin implies that the probability of success and failure is equal.
  - Use the Bernoulli distribution formula to determine the probability mass function.

*Knowledge*: *Refer to Bernoulli Distribution section in discrete random variables.*

**Difficulty Level**: Beginner

## Relationships (Edges)

- **has_exercise** <= (i.e. **is_exercise_for** =>) *Concept* [Bernoulli Distribution]
- **involved_in_exercise** <= (i.e. **involves_xxx** =>) *Concept* [Discrete Random Variable]
  
**SOURCE**: Stat400 teaching material - Jonathan Fernandez
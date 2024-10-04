Chapter3:{Discrete Random Variable}
Section:{Uniform Discrete Distribution}

## Properties (Attributes)

- **Name**: Expected Value and Variance of Uniform Distribution

- **Statement**:

  > **Theorem**: Suppose $X$ has the Uniform distribution on $\{1, 2, 3, \dots, N\}$. Then:
  > 
  > 1. The expected value of $X$ is given by:
  >    $$E(X) = \frac{N+1}{2}$$
  > 2. The variance of $X$ is given by:
  >    $$V(X) = \frac{(N+1)(N-1)}{12}$$
  
  *Source*: Stat400 teaching material - Jonathan Fernandez

- **Hypotheses/Assumptions**:

  - $X$ is a discrete random variable uniformly distributed over the set $\{1, 2, 3, \dots, N\}$.
  - $N$ is a positive integer ($N \in \mathbb{N}$).

- **Proof**:
> put proof/computation as a separate node type

  **Proof of Expected Value**:
  
  The expected value of $X$ is calculated as:
  \[
  E(X) = \sum_{k=1}^{N} k \cdot \frac{1}{N} = \frac{1}{N} \sum_{k=1}^{N} k = \frac{1}{N} \cdot \frac{N(N+1)}{2} = \frac{N+1}{2}
  \]
  
  **Proof of Variance**:
  
  First, compute $E(X^2)$:
  \[
  E(X^2) = \sum_{k=1}^{N} k^2 \cdot \frac{1}{N} = \frac{1}{N} \sum_{k=1}^{N} k^2 = \frac{1}{N} \cdot \frac{N(N+1)(2N+1)}{6} = \frac{(N+1)(2N+1)}{6}
  \]
  
  Then, the variance is:
  \[
  V(X) = E(X^2) - [E(X)]^2 = \frac{(N+1)(2N+1)}{6} - \left( \frac{N+1}{2} \right)^2 = \frac{(N+1)(N-1)}{12}
  \]

- **Aliases**:

  - "Uniform Discrete Distribution Parameters"
  - "Expected Value and Variance of Uniform Distribution"

- **Description**:

  This theorem provides formulas to compute the expected value and variance of a discrete random variable uniformly distributed over the integers from $1$ to $N$. In such a distribution, each integer within the set $\{1, 2, \dots, N\}$ has an equal probability of $\frac{1}{N}$. These parameters are essential for summarizing the central tendency and dispersion of the distribution.

- **Tags/Categories**: ["Probability Theorems", "Statistics", "Discrete Distributions", "Uniform Distribution"]

## Relationships (Edges)

- **involves_concept** → **Uniform Discrete Distribution**, **Expected Value**, **Variance**

- **uses_theorem** → **Formulas for Sum of Integers and Squares**:
  
  - Sum of the first $N$ positive integers:
    \[
    \sum_{k=1}^{N} k = \frac{N(N+1)}{2}
    \]
  - Sum of the squares of the first $N$ positive integers:
    \[
    \sum_{k=1}^{N} k^2 = \frac{N(N+1)(2N+1)}{6}
    \]

- **is_corollary_of** → *Not applicable*

- **is_generalization_of** → *Not applicable*

- **has_application** → **Random Number Generation**, **Simulation**, **Statistical Modeling**

- **implies_property** → **Mean and Variance of Discrete Uniform Distribution**

---

*Note*: Understanding these parameters helps in analyzing and interpreting data modeled by a uniform discrete distribution, which is common in simulations and randomized algorithms where each outcome is equally likely.
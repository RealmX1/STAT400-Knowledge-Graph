# Property Node: Variance of Bernoulli Random Variable

## Attributes

- **Name**: Variance of Bernoulli Random Variable

- **Definition**: 
  - **Notation**: 
    - Latex: `V(X) = p(1-p)`
    - Rendered: $V(X) = p(1-p)$
    - **Range**: $V(X) \in [0, \frac{1}{4}]$

- **Description**: 
  - The variance of a Bernoulli random variable quantifies the spread of the possible outcomes around the expected value. It reflects the uncertainty or variability in the outcome when the probability of success ($p$) changes. 

- **Proof**: 
  > **SOURCE**: Stat400 teaching material - Jonathan Fernandez
  - To calculate the variance of a Bernoulli random variable $X$, consider that $X$ takes values 0 or 1 with probabilities $1-p$ and $p$, respectively. The variance is calculated as:
  \[
  V(X) = E(X^2) - (E(X))^2
  \]
  Since $X^2 = X$ for a Bernoulli variable:
  \[
  E(X^2) = E(X) = p
  \]
  Thus:
  \[
  V(X) = p - p^2 = p(1-p)
  \]

## Relationships

- **has_property** <= (i.e. **is_property_of** =>) Bernoulli Distribution
- **has_subconcept** <= (i.e. **is_subconcept_of** =>) Variance of Random Variable
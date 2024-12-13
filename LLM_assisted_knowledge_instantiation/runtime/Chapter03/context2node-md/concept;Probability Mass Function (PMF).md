# Concept Node: Probability Mass Function (PMF)

## Attributes

- **Name**: Probability Mass Function (PMF)
- **Aliases**: 
  - *None defined in the context*

- **Definition**:
  - **Notation**: 
    - Latex: `p_X(x)`
    - Rendered: $p_X(x)$
  - **Explanation**:
    - $X$: 
      - Description: Denotes the random variable for which the probability is assigned.
    - $x$: 
      - Description: Represents a specific value that the discrete random variable $X$ can take.
    - $p_X(x)$:
      - Description: The probability that the discrete random variable $X$ takes the value $x$.
  - **Example**:
    - $$p_X(x) = \begin{cases}
        1-p \quad \text{if $x=0$}\\
        p \quad \text{if $x=1$}
    \end{cases}$$
      - Description: This example uses the Bernoulli random variable to illustrate the specific probabilities assigned to the possible values of a discrete random variable.

- **Description**: 
  - The Probability Mass Function (PMF) is a function that provides the probability that a discrete random variable is exactly equal to some value. It serves as a foundation for working with discrete random variables by associating probabilities with individual outcomes within a discrete sample space.

## Relationships

- **is_subconcept_of** => (i.e. **has_subconcept** <=) *Concept* [Discrete Random Variable]
# Concept Node: Probability Mass Function (PMF)

## Attributes

- **Name**: Probability Mass Function (PMF)
  - **Aliases**: 
    - PMF
    - Probability Mass Function

- **Definition**:
  - **Notation**: $p_X(x)$
    - **Explanation**:
      - $X$
        - Description: A discrete random variable.
      - $x$
        - Description: Values that the random variable $X$ can assume.
      - Probability
        - Description: Probability value of the random variable taking a specific value.
  - **Example**:
    - $$p_X(x) = \begin{cases}
        1-p \quad \text{if $x=0$}\\
        p \quad \text{if $x=1$}
    \end{cases}$$ (this example is for the concept node "Probability Mass Function (PMF)"; using bernoulli distribution as an example)
      - Description: Represents a discrete random variable, which is a function that maps each outcome of a random experiment to a real number.

- **Description**: 
  - A probability mass function (PMF) gives the probability of discrete random variables exactly equaling some value. It is used to define discrete random variables, where the set of possible outcomes is discrete as opposed to continuous.
  
## Relationships

### Relation regarding concept

- **is_subconcept_of** <- *Concept* [Discrete Random Variable]
  - The PMF is a fundamental concept within discrete random variables, highlighting how the probabilities are allocated over the possible values in the sample space of discrete values.

- **is_prerequisite_of** → *Concept* [Expected Value of Distribution, Variance of Distribution]
  - Understanding the PMF is necessary for calculating related statistics like expected value and variance for discrete distributions.
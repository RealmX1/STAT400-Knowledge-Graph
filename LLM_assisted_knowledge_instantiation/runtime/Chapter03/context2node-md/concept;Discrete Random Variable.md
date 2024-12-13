# Discrete Random Variable

## Attributes

- **Name**: Discrete Random Variable
  - **Aliases**: 
    - None

- **Definition**:
  - **Notation**: `X`
    - Rendered: $X$
  - **Explanation**:
    - $\mathcal{X}$:
      - Range: $\mathcal{X}$ is a discrete subset of $\mathbb{R}$
      - Description: Set of all possible discrete values that the random variable can take.
    - $F_X$:
      - Description: The cumulative distribution function, which is a step function for discrete random variables.

- **Example**:
    - $$p_X(x)=P(X=x)=\frac{1}{N} \quad \quad \text{for all $x\in \mathcal{X}$}$$
      - Description: Example of a probability mass function for a uniform discrete random variable.

- **Description**: 
  - A discrete random variable $X$ is one that has a countable number of possible values. This means that its cumulative distribution function is a step function, indicating that the set of values attainable by $X$ is discrete. Common examples include integers or a finite set of possible outcomes, typically observed in experiments or scenarios with countable outcomes like die tosses.

## Relationships

- **is_subconcept_of** => (i.e. **has_subconcept** <=) *Concept* [Discrete Distribution, Random Variable]
  - The concept "Discrete Random Variable" helps form the foundation for understanding discrete distributions.
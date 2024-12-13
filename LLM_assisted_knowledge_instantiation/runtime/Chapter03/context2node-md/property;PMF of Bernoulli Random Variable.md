# PMF of Bernoulli Random Variable

## Attributes

- **Name**: PMF of Bernoulli Random Variable
  - **Aliases**: ["Probability Mass Function of Bernoulli Distribution"]

- **Definition**: The probability mass function (PMF) of a Bernoulli random variable $X$ with parameter $p\in (0,1)$ is defined as:
  - **Notation**: 
    - Latex: 
      ```latex
      p_X(x) = \begin{cases}
        1-p \quad \text{if $x=0$}\\
        p \quad \text{if $x=1$}
      \end{cases}
      ```
      Rendered: 
      $$p_X(x) = \begin{cases}
        1-p \quad \text{if $x=0$}\\
        p \quad \text{if $x=1$}
      \end{cases}$$
  - Another equivalent form of the PMF is:
    - Latex: 
      ```latex
      p_X(x) = p^x(1-p)^{(1-x)} \quad \quad x \in \{0, 1\}
      ```
      Rendered: 
      $$p_X(x) = p^x(1-p)^{(1-x)} \quad \quad x \in \{0, 1\}$$

- **Description**: The probability mass function for a Bernoulli random variable represents the probability of achieving either a success or a failure in a Bernoulli trial, which consists of a single experiment with two possible outcomes.

## Relationships

- **has_property** <= (i.e. **is_property_of** =>) *Concept*
  - *Bernoulli Distribution*

- **has_subconcept** <= (i.e. **is_subconcept_of** =>) *Concept*
  - *Probability Mass Function (PMF)*

- **has_subproperty** => (i.e. **is_subproperty_of** <=) *Property*

- **is_prerequisite_of** <= (i.e. **depends_on** =>) *Property*
```
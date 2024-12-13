# Property Node - PMF of Bernoulli Distribution

## Attributes

- **Name**: PMF of Bernoulli Distribution
  - **Aliases**: ["Probability Mass Function of Bernoulli Distribution", "PMF", "Probability Distribution"]

- **Definition**: 
  - **Notation**: 
    - Latex: `p_X(x) = \begin{cases} 1-p & \text{if } x=0\\ p & \text{if } x=1 \end{cases}`
    - Rendered: 
      $$
      p_X(x) = \begin{cases} 
        1-p & \text{if } x=0\\ 
        p & \text{if } x=1 
      \end{cases}
      $$

    - Latex: `p_X(x) = p^x(1-p)^{(1-x)}`
    - Rendered:
      $$
      p_X(x) = p^x(1-p)^{(1-x)},\ x \in \{0,1\}
      $$

    - **Range**: $p_X(x) \in [0, 1]$

- **Description**: 
  - "The probability mass function of the Bernoulli Distribution specifies the probabilities of observing a success (1) or a failure (0) in a single trial that involves a binary outcome."

## Relationships

- **is_property_of** ← Bernoulli Distribution
- **is_child_concept_of** ← Probability Mass Function (PMF)

> SOURCE: Stat400 teaching material - Jonathan Fernandez
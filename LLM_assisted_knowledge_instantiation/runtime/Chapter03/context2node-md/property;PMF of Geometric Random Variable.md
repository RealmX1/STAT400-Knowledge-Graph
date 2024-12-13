# Property Node: PMF of Geometric Distribution

## Attributes

- **Name**: PMF of Geometric Distribution
  - **Aliases**: Probability Mass Function of Geometric Distribution

- **Definition**: 
  - **Notation**:
    - Latex: `p_X(x) = p^x(1-p)^{(x-1)}`
    - Rendered: $p_X(x) = p^x(1-p)^{(x-1)}$
    - **Range**: $x \in \{1, 2, 3, \dots\}$

- **Description**: 
  The PMF of a Geometric distribution represents the probability of observing the first success on the $x$th trial in a series of independent Bernoulli trials, each of which has a probability of success $p$. The distribution models waiting times until the first success.

- **Proof**: 
  The proof involves calculating the probability that the first $x-1$ trials are failures and the $x$-th trial is a success. Hence, the probability is given by $p_X(x) = (1-p)^{x-1}p$. This can be shown by considering the sample space for the geometric experiment, which involves independent Bernoulli trials, with trials succeeding after $x-1$ failures. 
  > SOURCE: Stat400 teaching material - Jonathan Fernandez

## Relationships

- **has_property** <= (i.e. **is_property_of** =>) *Concept* MUST
  - Geometric Distribution

- **has_subconcept** <= (i.e. **is_subconcept_of** =>) *Concept* MUST
  - Probability Mass Function (PMF)

- **has_subproperty** => (i.e. **is_subproperty_of** <=) *Property*

- **is_prerequisite_of** <= (i.e. **depends_on** =>) *Property*
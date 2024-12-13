# Property Node

## Attributes

- **Name**: PMF of Binomial Random Variable
  - **Aliases**: ["Probability Mass Function of Binomial Distribution", "Binomial PMF"]

- **Definition**: 
  - **Notation**: 
    - Latex: `p_X(x) = {n \choose x} p^x(1-p)^{(n-x)}`
    - Rendered: $p_X(x) = {n \choose x} p^x(1-p)^{(n-x)}$
    - **Range**: Dual interpretation as it covers $x \in \{0, 1, 2, \dots, n\}$.

- **Description**: 
  The probability mass function (PMF) of a Binomial random variable, $X \sim \text{Binomial}(n, p)$, gives the probability of obtaining exactly $x$ successes in $n$ independent Bernoulli trials, each with a probability of success $p$.

- **Proof**: 
  The proof involves explicitly calculating the PMF of $X$ by considering all possible sequences of successes and failures and summing their respective probabilities.

## Relationships

- **has_property** <= (i.e. **is_property_of** =>) *Concept* 
  - Binomial Distribution

- **has_subconcept** <= (i.e. **is_subconcept_of** =>) *Concept* 
  - Probability Mass Function (PMF)

- **has_subproperty** => (i.e. **is_subproperty_of** <=) *Property*

- **is_prerequisite_of** <= (i.e. **depends_on** =>) *Property*

> NEED TO mark SOURCE for the information used here. By default we will use `Stat400 teaching material - Jonathan Fernandez`
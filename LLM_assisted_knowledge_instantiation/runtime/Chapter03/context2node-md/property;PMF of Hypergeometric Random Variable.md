# PMF of Hypergeometric Distribution

## Attributes

- **Name**: PMF of Hypergeometric Distribution
  - **Aliases**: Probability Mass Function of Hypergeometric Distribution

- **Definition**: 
  - **Notation**: 
    - Rendered: \( p_X(x) = \frac{{N \choose x} {N-M \choose n-x}}{{N \choose n}} \)
    - Latex: `p_X(x) = \frac{{N \choose x} {N-M \choose n-x}}{{N \choose n}}` 
    - **Range**: \( x \in \{0, 1, 2, \dots, \min(n, M)\} \)

- **Description**: 
  The probability mass function (PMF) of the Hypergeometric Distribution gives the probability of observing exactly \(x\) successes in \(n\) draws from a population of size \(N\) containing exactly \(M\) successes, where the draws are made without replacement.

- **Proof**: 
  Refer to `Stat400 teaching material - Jonathan Fernandez`. Proof involves understanding the calculation of combinations for successful and unsuccessful outcomes, dividing by the total combinations for drawing \(n\) items from \(N\).

## Relationships

- **has_property** <= (i.e. **is_property_of** =>) *Concept*: Hypergeometric Distribution
- **has_subconcept** <= (i.e. **is_subconcept_of** =>) *Concept*: Probability Mass Function (PMF)
- **has_subproperty** => (i.e. **is_subproperty_of** <=) *Property*: N/A
- **is_prerequisite_of** <= (i.e. **depends_on** =>) *Property*: N/A

---

*Additional Notes:* 
- The PMF of the Hypergeometric Distribution is crucial for understanding events that involve sampling without replacement.
- This conceptual understanding also highlights the differences from similar discrete distributions like the Binomial Distribution, which assumes replacement.
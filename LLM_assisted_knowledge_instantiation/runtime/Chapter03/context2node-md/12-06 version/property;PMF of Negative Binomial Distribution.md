# PMF of Negative Binomial Distribution

## Attributes

- **Name**: PMF of Negative Binomial Distribution
  - **Aliases**: ["Probability Mass Function of Negative Binomial Distribution"]

- **Definition**: 
  - **Notation**: 
    - Rendered: $p_X(x) = \binom{x+r-1}{x} p^r (1-p)^x$
    - Latex: `p_X(x) = \binom{x+r-1}{x} p^r (1-p)^x`
  - **Range**: $p_X(x) \in [0, 1]$ for $x \in \{0, 1, 2, 3, \ldots\}$

- **Description**: 
  The probability mass function (PMF) of the Negative Binomial Distribution quantifies the likelihood of observing exactly \(x\) failures before achieving \(r\) successes in a series of independent Bernoulli trials, each with success probability \(p\).

- **Proof**: 
  *The proof involves explicitly counting the outcomes in the set* $$\{X = k\} = \{\text{exactly } k \text{ failures observed before the } r\text{th success}\}$$ *and using this to calculate the pmf of \(X\), and showing that it is the same as the pmf of the Negative Binomial distribution with parameters \(r\) and \(p\). We leave this as an exercise for the reader.*

## Relationships

- **is_property_of** ← Negative Binomial Distribution
- **is_child_concept_of** ← Probability Mass Function (PMF)
- **depends_on** ← *additional information*
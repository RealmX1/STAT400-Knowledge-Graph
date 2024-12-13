# Property Node: Expected Value of Geometric Distribution

## Attributes

- **Name**: Expected Value of Geometric Distribution
  - **Aliases**: ["Mean of Geometric Distribution"]

- **Definition**: 
  - **Notation**: 
    - Latex: `E[Geom(p)] = \frac{1}{p}`
    - Rendered: \(E[Geom(p)] = \frac{1}{p}\)
    - **Range**: 
      - Latex: `E[Geom(p)] \in [1, \infty)`
      - Rendered: \(E[Geom(p)] \in [1, \infty)\)

- **Description**: 
  The expected value of a geometric distribution represents the average number of trials needed to obtain the first success in a series of Bernoulli trials. It depends on the probability of success \(p\).

- **Proof**: 
  To find the expected value, consider the series of Bernoulli trials where the first success comes with probability \(p\) on the \(k\)-th trial. Therefore, the probability of failure in the previous trials is \((1-p)^{k-1}\).
  Using the equation for expected value of a random variable, and solving the geometric series, we obtain the expected value as \(\frac{1}{p}\).

## Relationships

- **has_property** <= (i.e. **is_property_of** =>) *Concept*: Geometric Distribution
- **has_subconcept** <= (i.e. **is_subconcept_of** =>) *Concept*: Expected Value of Random Variable
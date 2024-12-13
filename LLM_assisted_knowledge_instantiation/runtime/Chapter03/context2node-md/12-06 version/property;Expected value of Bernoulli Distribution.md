# Expected value of Bernoulli Distribution

## Attributes

- **Name**: "Expected value of Bernoulli Distribution"
  - **Aliases**: ["Expected Value", "Mean of Bernoulli Distribution"]

- **Definition**: 
  - **Notation**: 
    - Symbols or mathematical notation associated with the property: 
      - "\(E(X) = p\)" \(E(X) = p\)
  - **Range**: 
    - The range of the property:
      - \(p \in (0, 1)\)

- **Description**: 
  The expected value of a Bernoulli distribution is the probability \(p\) of success in a Bernoulli trial. The Bernoulli distribution is a discrete distribution with only two possible outcomes, usually termed "success" and "failure". This value represents the average outcome, which in the case of a Bernoulli distribution corresponds directly to the probability of success.

- **Proof**: 
  The expected value of a Bernoulli distribution, \(E(X)\), can be derived as follows:
  - Given the Bernoulli random variable \(X\) with \(P(X=1) = p\) and \(P(X=0) = 1-p\),
  - The expected value is calculated as: 
    \[
    E(X) = 0 \cdot (1-p) + 1 \cdot p = p.
    \]

 > NEED TO mark SOURCE for the information used here. By default we will use `Stat400 teaching material - Jonathan Fernandez`

## Relationships

- **is_property_of** ← "Bernoulli Distribution"
- **is_child_concept_of** ← "Expected Value of Distribution"
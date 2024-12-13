# Variance of Binomial Random Variable

## Attributes

- **Name**: Variance of Binomial Random Variable
  - **Aliases**: ["Variance of Binomial Distribution", "Var(Binomial)"]

- **Definition**:
  - **Notation**: 
    - Latex: `V(Binom(n, p)) = np(1-p)`
    - Rendered: $V(Binom(n, p)) = np(1-p)$
    - **Range**: $V(Binom(n, p)) \in [0, n]$

- **Description**: 
  The variance of a binomial random variable expresses the spread or variability of the number of successes in a fixed number of Bernoulli trials. It is a measure of how much the number of successes deviates from the expected value over repeated experiments.

- **Proof**: 
  The variance of a binomial distribution can be derived by using the formula for variance of a sum of independent random variables. Each trial in the binomial distribution is independent, and the trials can be considered as Bernoulli trials with variance $p(1-p)$. The variance of the binomial distribution is $np(1-p)$ since it is the sum of variances from these $n$ independent trials.
  > NEED TO mark SOURCE for the information used here. By default we will use `Stat400 teaching material - Jonathan Fernandez`

## Relationships

- **has_property** <= (i.e. **is_property_of** =>) *Concept*
  - Binomial Distribution

- **has_subconcept** <= (i.e. **is_subconcept_of** =>) *Concept*
  - Variance of Random Variable

- **has_subproperty** => (i.e. **is_subproperty_of** <=) *Property*
  - None relevant subproperties found within context and existing nodes.

- **is_prerequisite_of** <= (i.e. **depends_on** =>) *Property*
  - None relevant prerequisite properties found within context and existing nodes.
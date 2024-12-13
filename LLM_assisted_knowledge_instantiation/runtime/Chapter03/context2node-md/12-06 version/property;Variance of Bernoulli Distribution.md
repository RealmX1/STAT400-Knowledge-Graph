# Property Node: Variance of Bernoulli Distribution

## Attributes

- **Name**: Variance of Bernoulli Distribution
  - **Aliases**: ["Variance of Bernoulli Random Variable", "Bernoulli Variability"]

- **Definition**: 
  The variance of a Bernoulli distribution is a measure of the dispersion of the distribution around its mean.
  - **Notation**: 
    - LaTeX: "$V(X) = p(1-p)$"
    - Rendered: $V(X) = p(1-p)$
  - **Range**: $0 \leq V(X) \leq \frac{1}{4}$

- **Description**: 
  The variance of a Bernoulli distribution describes how spread out the successes and failures (0 and 1) are around the expected value. It indicates the degree of uncertainty in predicting the outcome of a Bernoulli trial.

- **Proof**: 
  - Source: Stat400 teaching material - Jonathan Fernandez
  The variance of a Bernoulli random variable $X \sim \text{Bernoulli}(p)$ is calculated as follows:
  
  Given: 
  \[ E(X) = p \]
  
  The variance $V(X)$ for a Bernoulli distribution is:
  \[ V(X) = E(X^2) - (E(X))^2 \]
  
  Since $X^2 = X$ for a Bernoulli random variable (as $X$ is either 0 or 1), we get:
  \[ V(X) = E(X) - p^2 = p - p^2 = p(1-p) \]

## Relationships

- **is_property_of**: 
  - Bernoulli Distribution

- **is_child_concept_of**: 
  - Variance of a distribution

- **depends_on**: 
  - Expected value of Bernoulli Distribution
# Variance of Geometric Distribution

## Attributes

- **Name**: Variance of Geometric Distribution
  - **Aliases**: ["Variance", "Variance of Geom(p) distribution"]

- **Definition**:
  - **Notation**: 
    - Rendered: $V(X) = \frac{1-p}{p^2}$
    - Latex: `V(X) = \frac{1-p}{p^2}`
  - **Range**: $V(X) \in [0, \infty)$

- **Description**: 
  The variance of a geometric distribution with parameter $p$, denoted as $X \sim \text{Geom}(p)$, measures the dispersion of trials it takes to achieve the first success. The variance formula $\frac{1-p}{p^2}$ reflects the spread of the distribution around its mean.

- **Proof**: 
  Check the detailed proof in Stat400 teaching material by Jonathan Fernandez which involves computing $E[X^2]$ and using $V(X) = E[X^2] - (E[X])^2$ with $E[X] = \frac{1}{p}$.

## Relationships

- **is_property_of**: Geometric Distribution
- **is_child_concept_of**: Variance of Distribution
- **depends_on**: Expected Value of Geometric Distribution
# Variance of Hypergeometric Distribution

## Attributes

- **Name**: Variance of Hypergeometric Distribution
  - **Aliases**: ["Hypergeometric Variance", "Variance"]

- **Definition**: 
  - **Notation**: 
    - Latex: `V(X) = \left(\frac{N-n}{N-1} \right)\cdot n\cdot \left(\frac{M}{N}\right)\cdot \left(1-\frac{M}{N} \right)`
    - Rendered: $V(X) = \left(\frac{N-n}{N-1} \right)\cdot n\cdot \left(\frac{M}{N}\right)\cdot \left(1-\frac{M}{N} \right)$

- **Description**: 
  - The variance of the Hypergeometric Distribution describes the spread of the number of successes in $n$ draws, out of a population of $N$, where $M$ are successes. The formula accounts for the lack of replacement in sampling, differentiating it from the binomial distribution.

- **Proof**: *The variance calculation involves counting the outcomes and considering the non-independence of selection due to lack of replacement. This uses combinatorial analysis and properties of expectation.*

> SOURCE: Stat400 teaching material - Jonathan Fernandez

## Relationships

- **is_property_of** ← Hypergeometric Distribution
- **is_child_concept_of** ← Variance of random variable
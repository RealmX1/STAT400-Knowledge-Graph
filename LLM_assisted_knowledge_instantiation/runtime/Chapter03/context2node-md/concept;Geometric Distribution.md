# Concept Node: Geometric Distribution

## Attributes

- **Name**: Geometric Distribution

- **Definition**:
  - **Notation**: 
    - Latex: `Geom(p)`
    - Rendered: $Geom(p)$
  - **Explanation**:
    - $p$
      - Range: $p \in (0, 1)$
      - Description: Represents the probability of success in a Bernoulli trial.

  - **Example**:
    - $p_X(x) = p^x(1-p)^{(x-1)} \quad \quad x\in \{1, 2, 3, \dots, \}$
    - Description: This is the probability mass function for the Geometric distribution, which describes the probability of observing the first success on the $x$-th trial.

- **Description**: The geometric distribution models phenomena involving "waiting" for the first success in a sequence of independent Bernoulli trials. It is the discrete probability distribution of the number of trials needed to get one success. The geometric distribution assumes that each trial is an independent Bernoulli trial with the same probability of success.

## Relationships

- **is_subconcept_of** => Discrete Distribution
# Bernoulli Trial

## Attributes

- **Name**: Bernoulli Trial
  - **Aliases**: 
    - Bernoulli Experiment
    - Binary Experiment

- **Definition**:
  - **Notation**: 
    - Latex: `BerExp(\text{Success}, \text{Failure})`
    - Rendered: $BerExp(\text{Success}, \text{Failure})$
  - **Explanation**: 
    - $\text{Success}$
      - Description: Outcome labeled as success in the experiment.
    - $\text{Failure}$
      - Description: Outcome labeled as failure in the experiment.

  - **Example**:
    - $$p_X(x) = \begin{cases}
        1-p \quad \text{if $x=0$}\\
        p \quad \text{if $x=1$}
      \end{cases}$$
      - Description: Each trial results in either success or failure.

- **Description**: 
  A Bernoulli trial is a random experiment where there are exactly two possible outcomes, usually labeled "success" and "failure". The trial is named after Jacob Bernoulli, a Swiss mathematician. Bernoulli trials are the building blocks for more complex distributions like the Binomial distribution.

## Relationships
# Geometric Distribution

## Attributes

- **Name**: Geometric Distribution
  - **Aliases**: 
    - *Geometric Random Variable*

- **Definition**:
  - **Notation**: $Geom(p)$
  - **Explanation**: 
    - $p$
      - Range: $p \in (0, 1)$
      - Description: Represents the probability of success in a Bernoulli trial.

  - **Example**:
    - $$p_X(x) = p^x(1-p)^{(x-1)} \quad \quad x \in \{1, 2, 3, \dots \}$$
      - Description: This is the probability mass function for a Geometric distribution, modeling the probability of $x$ number of trials to get the first success.

- **Description**: 
  - The Geometric Distribution is a discrete probability distribution that models the number of trials needed to achieve the first success in a sequence of independent and identically distributed Bernoulli trials. The trials continue until the first success is observed.

## Relationships

- **is_subconcept_of** <- *Concept* [Discrete Distribution]

- **is_prerequisite_of** → *Concept* [Bernoulli Distribution]
  - The concept rests on understanding Bernoulli trials, as each trial is modeled as a success or failure event.
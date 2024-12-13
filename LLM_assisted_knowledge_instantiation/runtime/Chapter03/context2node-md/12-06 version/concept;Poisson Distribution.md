# Concept Node

## Attributes

- **Name**: Poisson Distribution
  - **Aliases**: 
    - Poisson Process

- **Definition**:
  - **Notation**: $X \sim \text{Pois}(\lambda)$
  - **Explanation**:
    - $\lambda$
      - Range: $\lambda \in \mathbb{R}_{+}$
      - Description: Represents the average rate or mean number of occurrences of the event being modeled.
  - **Example**:
    - $$p_X(x) = e^{-\lambda} \frac{\lambda^x}{x!}$$
      - Description: The probability mass function of the Poisson distribution, which gives the probability of a given number of events happening in a fixed interval of time or space.

- **Description**: 
  - The Poisson distribution provides a model for events that occur independently in a given time interval or space area with a known constant mean rate. It is especially useful for modeling rare events and is related to the Poisson process.

## Relationships

### Relation regarding concept

- **is_subconcept_of** <- *Concept* [Discrete Distribution] 

- **is_prerequisite_of** → *Concept* [None]
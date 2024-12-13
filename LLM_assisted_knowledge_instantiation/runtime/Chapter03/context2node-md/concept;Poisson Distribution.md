# Poisson Distribution Node

## Attributes

- **Name**: Poisson Distribution

- **Definition**:
  - **Notation**: 
    - Latex: `Pois(\lambda)`
    - Rendered: $Pois(\lambda)$
  - **Explanation**: 
    - $\lambda$
      - Range: $\lambda \in \mathbb{R}_{+}$
      - Description: Represents the rate parameter, average rate, or mean number of occurrences of the event per unit time.

  - **Example**:
    - $$p_X(x) = e^{-\lambda} \frac{\lambda^x}{x!}$$
      - Description: The probability mass function (PMF) provides the probability that a given number of events occurs in a fixed interval of time or space.

- **Description**: 
  - Poisson Distribution is a discrete probability distribution that describes the number of events occurring within a fixed interval of time or space. It is applicable when events occur independently, with a known constant mean rate.


## Relationships

- **is_subconcept_of** => (i.e. **has_subconcept** <=) *Concept* [Discrete Distribution]
  - Explanation: The Poisson Distribution is a type of discrete random variable distribution used to model the probability of a number of events occurring within a specific timeframe.

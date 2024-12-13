# Property Node: Expected value of Uniform Distribution

## Attributes

- **Name**: Expected value of Uniform Distribution
  - **Aliases**: ["Expected Value", "Mean of Uniform Distribution"]

- **Definition**: 
  - **Notation**: 
    - LaTeX code: `E(X) = \frac{N+1}{2}` 
    - Rendered: \(E(X) = \frac{N+1}{2}\)
    - **Range**: \(E(X) \in \mathbb{R}\) (*since it is calculated over the natural numbers from 1 to N*)

- **Description**: 
  - The Expected value of a Uniform Discrete Distribution is the central measure representing the average or mean of all possible outcomes for a discrete uniform distribution when each outcome is equally likely. For a Uniform distribution over a range {1, 2, ..., N}, the expected value can be interpreted graphically as the midpoint of this range.

- **Proof**: *Source: Stat400 teaching material - Jonathan Fernandez*
  - When \(X\) is uniformly distributed on {1, 2, ..., N}, the expected value is derived by summing all values in the range and dividing by the number of values. Calculating \(E(X) = \frac{1 + 2 + ... + N}{N}\), we can use the formula for the sum of the first N natural numbers: \(\frac{N(N+1)}{2}\). This gives us \(\frac{N+1}{2}\).

## Relationships

- **is_property_of** ← *Concept*
  - Uniform Discrete Distribution

- **is_child_concept_of** ← *Concept*
  - Expected Value of Distribution

- **depends_on** ← *Property* 
  - *None specific prerequisites are required for this property.*

- **has_subproperty** → *Property*
  - *None specific subproperties are known for this property.*
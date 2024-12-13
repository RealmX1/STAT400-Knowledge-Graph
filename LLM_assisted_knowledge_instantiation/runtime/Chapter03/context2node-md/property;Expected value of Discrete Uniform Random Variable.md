## Property Node: Expected value of Uniform Random Variable

### Attributes

- **Name**: Expected value of Uniform Random Variable
  - **Aliases**: ["Mean of Uniform Distribution", "Expected Value of Uniform Distribution"]

- **Definition**:
  - **Notation**:
    - Latex: `E(\text{Uniform}(N)) = \frac{N+1}{2}`
    - Rendered: $E(\text{Uniform}(N)) = \frac{N+1}{2}$
  - **Range**: $E(\text{Uniform}(N)) \in \{1, N\}$

- **Description**: 
  - The expected value of a Uniform distribution on $\{1, 2, 3, \dots, N\}$ signifies the average or mean value of the random variable, calculated as the middle point of its range.

- **Proof**: 
  - The expected value of a discrete uniform random variable is derived by taking the average of all possible values. Given a uniform distribution over $\{1, 2, \dots, N\}$, each value has a probability of $1/N$. Therefore, the expected value is calculated as:
  
    - $$E(X) = \sum_{x=1}^{N} x \cdot \frac{1}{N} = \frac{1}{N} \sum_{x=1}^{N} x = \frac{1}{N} \cdot \frac{N(N+1)}{2} = \frac{N+1}{2}$$

  - *Source*: Stat400 teaching material - Jonathan Fernandez


### Relationships

- **has_property** <= (i.e. **is_property_of** =>) *Concept*
  - Discrete Uniform Distribution
- **has_subconcept** <= (i.e. **is_subconcept_of** =>) *Concept*
  - Expected Value of Random Variable
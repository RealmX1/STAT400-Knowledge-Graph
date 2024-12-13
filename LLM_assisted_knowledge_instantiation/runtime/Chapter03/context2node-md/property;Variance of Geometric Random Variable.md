# Variance of Geometric Distribution

## Attributes

- **Name**: Variance of Geometric Distribution

- **Definition**: 
  - **Notation**: 
    - Latex: `V(X) = \frac{1-p}{p^2}`
    - Rendered: $V(X) = \frac{1-p}{p^2}$
    - **Range**: $V(X) \geq 0$

- **Description**: This property describes the variance of a geometric distribution, which represents the variability or spread in the number of trials needed to get the first success, with each trial being independent and having a probability of success $p$.

- **Proof**: *Step by step proof of this property would involve calculating $V(X) = E(X^2) - [E(X)]^2$, starting by deriving expressions for $E(X)$ and $E(X^2)$ for the geometric distribution.*

## Relationships

- **has_property** <= (i.e. **is_property_of** =>) 
  - *Geometric Distribution*

- **has_subconcept** <= (i.e. **is_subconcept_of** =>) 
  - *Variance of Random Variable*

- **has_subproperty** => (i.e. **is_subproperty_of** <=)

- **is_prerequisite_of** <= (i.e. **depends_on** =>) 
  - *Expected Value of Geometric Distribution*

## Additional Information

- **Source**: Information pertaining to the variance of the geometric distribution is based on standard statistical teaching materials like `Stat400 teaching material - Jonathan Fernandez`. 

*Note*: The proof generally requires showing that the variance formula arises from the geometric series calculations for expectations in the geometric distribution context.
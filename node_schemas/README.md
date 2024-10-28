## Node Types
**There are 5 types of nodes - Concept Node, Property Node, Theorem Node, Exercise Node, and Application Example Node.**
- **Concept Node** 
  - self-explanatory
  - Examples: 
    - "Poisson Distribution"
    - "Variance of Distribution"
    - "Random Variable
- **Property Node** 
  - Property of a concept A that is instantiation of a concept node B.
  - Two types of properties: Essential and Accidental
    - (?) The properties modeled in KG should all be essential properties. 
    - Essential properties are defining, unchanging, and necessary for a concept to be what it is. (or strictly derived from other essential properties)
      - Variance function of Poisson Distribution
    - Accidental properties are contextual, variable, and non-essential to the identity of the concept.
      - Variance value of an arbitrary Poisson Distribution (is accidental in context of the concept "Poisson Distribution")
  - Examples: 
    - "Variance (function) of Poisson Distribution" is a property of concept "Poisson Distribution", and this property is an instantiation of concept "Variance of Distribution".
    - "PDF of Exponential Distribution" is a property of concept "Exponential Distribution", and this property is an instantiation of concept "Probability Density Function (PDF)".
  - Note:
    - What distinguish "property of a node" and "child concept" is that, 
      - a child concept is only at the begining of a "is-a" relationship, 
      - the property is both at the beginning of a "is-a" relation, and also at the end of a "has-a"/"is" relationship.
        - ? What about difference between "has-a" and "is" relationship?
          - Example of "has-a" relationship: "Poisson Distribution" has a property "Variance of Poisson Distribution"
          - Example of "is" relationship: "Raven" is "Black"
      - I've thought through the question "whether there exist situation where a node with "has-a"/"is" relationship also serve major unambiguous functionality as a "concept" node; I couldn't find any. IF there exist a large amount of such node, then it would be a good idea to model "property" not as parallel node type of "concept" but solely model it as concept receiving "has-a"/"is" relationship.
      - The "Raven" is "Black" seem to be a good example of the opposite; black is a concept, and it doesn't make much sense to create a "black of raven" property specifically for this (i.e., "black" itself is also acting as a property of raven)
- **Theorem Node**:
  - self-explanatory
- **Exercise Node**:
  - self-explanatory
- **Application Example Node**:
  - self-explanatory



## Description used in Prompting

**There are 5 types of nodes - Concept Node, Property Node, Theorem Node, Exercise Node, and Application Example Node.**
## Node Types

- **Concept Node** 
  - self-explanatory
  - Examples: 
    - "Poisson Distribution"
    - "Variance of Distribution"
    - "Random Variable
- **Property Node** 
  - Property of a concept A that is instantiation of a concept node B.
  - Two types of properties: Essential and Accidental
    - (?) The properties modeled in KG should all be essential properties. 
    - Essential properties are defining, unchanging, and necessary for a concept to be what it is. (or strictly derived from other essential properties)
      - Variance function of Poisson Distribution
    - Accidental properties are contextual, variable, and non-essential to the identity of the concept.
      - Variance value of an arbitrary Poisson Distribution (is accidental in context of the concept "Poisson Distribution")
  - Examples: 
    - "Variance (function) of Poisson Distribution" is a property of concept "Poisson Distribution", and this property is an instantiation of concept "Variance of Distribution".
    - "PDF of Exponential Distribution" is a property of concept "Exponential Distribution", and this property is an instantiation of concept "Probability Density Function (PDF)".
  - Note:
    - What distinguish "property of a node" and "child concept" is that, 
      - a child concept is only at the begining of a "is-a" relationship, it is a binary relationship (between parent concept and child concept)
      - the property is both at the beginning of a "is-a" relation, and also at the end of a "has-a"/"is" relationship. it is a ternary relationship (between parent concept, owner concept, and property concept)
- **Theorem Node**:
  - self-explanatory
- **Exercise Node**:
  - self-explanatory
- **Application Example Node**:
  - self-explanatory


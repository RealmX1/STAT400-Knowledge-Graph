# Property Node Schema

## Attributes

- **Name**: *String*
  - The official name of the property.
  - *Example*: "Expected Value of Poisson Distribution"
  - **Aliases**: *List of Strings* (optional)
    - Alternative names or synonyms for the property.
    - *Example*: ["Expected Value", "Mean of Poisson Distribution"]

- **Definition**: *Text*
  - **Notation**: *String/Text* (LaTeX)
    - Symbols or mathematical notation associated with the property. Show LaTeX code and rendered LaTeX side by side.
    - *Example*: "\lambda" $\lambda$
    - **Range**: *String/Text* (LaTeX) (?)
      - The range of the property.
      - *Example*: $\lambda \in \{0, \infty\}$
  - **Description**: *Text*
    - Additional explanations, background information, or context about the property.
    - *Example*: "Expected Value of Poisson Distribution is the average number of times an event occurs within a fixed interval of time or space. It is the same as the lambda parameter of the Poisson Distribution."

- **Proof**: *Text* (optional)
  - Step by step proof of the property. #TODO: Provide concrete example for sake of more consistenet LLM output
  > NEED TO mark SOURCE for the information used here. By default we will use `Stat400 teaching material - Jonathan Fernandez`

  
## Relationships (Edges)
- **is_property_of** ← *Concept*/*Theorem* (the reverse of **has_property**)
  - Concepts or theorems that possess this property.
  - *Example*: "Expected Value of Poisson Distribution" is a property of "Poisson Distribution"
- **is_child_concept_of** ← *Concept* (the reverse of **is_parent_concept_of**)
  - Properties that are derived from the concept.
  - *Example*: "Variance of Poisson Distribution" is a child concept of "Variance of random variable"

- **related_to** → *Concept*/*Theorem* (the reverse of **is_related_to**)
  - used in theorem, but isn't part of axioms or conclusions.
  - *Example*: "Non-negativity" related to "Probability Distribution"
- **is_prerequisite_of** → *Theorem* (the reverse of **depends_on**)
  - used to create hypothesis or proof of theorem
- **conclude_from** ← *Theorem* (the reverse of **concludes**)
  - Theorems that imply this property.
  - *Example*: "Kolmogorov's Axioms" imply "Non-negativity"

- **has_application** → *Application Example* (the reverse of **is_application_of**)
  - Real-world applications where the property is relevant.
  - *Example*: "Ensuring probabilities in a probabilistic model are non-negative"
- **has_exercise** → *Exercise* (the reverse of **is_exercise_for**)
  - Exercises that involve the property.
  - *Example*: "Exercise 2.1.5"



- **has_subproperty** → *Property* (the reverse of **is_subproperty_of**) (likely won't encounter, optional)
  - More specific properties derived from the current property.
  - *Example*: "Strict Positivity" is a subproperty of "Non-negativity"
  - SAME AS IMPLIES

## Information to be additionally Rendered When Student Zooms In on Node
Hiearchical inheritance, from "parent concept" -- both directly from the concept node, and indirectly from the property of the concepet nodes.
For example, "PMF" has a property "Non-negativity". At the same time, "PMF of Poisson Distribution" is a child concept of "PMF". Then "PMF of Poisson Distribution" inherits the property "Non-negativity" from "PMF".


For the sake of maintaining only one copy of any information, info related to other nodes would be presented with a reference link that only gets rendered out when the user zooms in to the node in the interface.

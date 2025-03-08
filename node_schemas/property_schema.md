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
    - Symbols or mathematical notations associated with the property in latex format. First present raw latex code, then present the rendered latex code.
    - *Example*: 
      - Rendered: $E[Pois(\lambda)] = \lambda$
      - Latex: `E[Pois(\lambda)] = \lambda` 
    - **Range**: *String/Text* (LaTeX) (?)
      - The range of the property.
      - *Example*: $E[Pois(\lambda)] \in \{0, \infty\}$
<ignore>
A Type property under notation maybe should be taken into consideration.
    - **Type**: *Enum*
      - One of ["Boolean", "Number"...]
      - *Example*: "Boolean"
</ignore>

- **Description**: *Text* (optional)
  - Additional explanations, background information, or context about the property.
  - *Example*: "Expected Value of Poisson Distribution is the average number of times an event occurs within a fixed interval of time or space. It is the same as the lambda parameter of the Poisson Distribution."

- **Proof**: *Text* (optional)
  - Step by step proof of the property. #TODO: Provide concrete example for sake of more consistenet LLM output
  > NEED TO mark SOURCE for the information used here. By default we will use `Stat400 teaching material - Jonathan Fernandez`

  
## Relationships

- **has_property** <= (i.e. **is_property_of** =>) *Concept* MUST
  - Concepts or theorems that possess this property.
  - *Example*: Current Property "Expected Value of Poisson Distribution" is a property of "Poisson Distribution"; "Poisson Distribution" has_property current property.
- **has_subconcept** <= (i.e. **is_subconcept_of** =>) *Concept* MUST
  - The concept that this property is derived from/is a subset of.
  - *Example*: Current Property "Variance of Poisson Distribution" is a child concept of "Variance of random variable"; "Variance of Random Variable" has_subconcept current property.
- **has_subproperty** => (i.e. **is_subproperty_of** <=) *Property*
  - More specific properties derived from the current property. The target property (subproperty) implies the current property.
  - *Example*: "Strict Positivity" (current property) has "Non-negativity" (target property) as a subproperty
- **is_prerequisite_of** <= (i.e. **depends_on** =>) *Property*
  - Properties that are prerequisites for this property.
  - *Example*: Current Property "Variance of Poisson Distribution" depends on "Expected Value of Poisson Distribution"; "Expected Value of Poisson Distribution" is a prerequisite of current property.

<ignore>
<deprecated>
- **related_to** → *Concept*/*Theorem* [list of concept/theorem names] (the reverse of **is_related_to**)
  - used in theorem, but isn't part of axioms or conclusions. Only apply when there doesn't exist a more specific relationship with the said related concept/theorem.
  <!-- - *Example*: "Expected Value of Poisson Distribution" related to "Law of Large Numbers"; This is not a good example. law of large numbers is already related indirectly through "expected value" -->
</deprecated>
> LOG IN THE OTHER SIDE OF ALL FOLLOWING RELATIONSHIPS
- **is_prerequisite_of** → *Theorem* [list of theorem names] (the reverse of **depends_on**)
  - used to create hypothesis or proof of theorem
- **conclude_from** ← *Theorem* [list of theorem names] (the reverse of **concludes**)
  - Theorems that imply this property.
  - *Example*: "Kolmogorov's Axioms" imply "Non-negativity"

- **has_application** → *Application Example* [list of application names] (the reverse of **is_application_of**)
  - Real-world applications where the property is relevant.
  - *Example*: "Ensuring probabilities in a probabilistic model are non-negative"
- **has_exercise** → *Exercise* [list of exercise names] (the reverse of **is_exercise_for**)
  - Exercises that involve the property.
  - *Example*: "Exercise 2.1.5"

## Information to be additionally Rendered When Student Zooms In on Node
Hiearchical inheritance, from "parent concept" -- both directly from the concept node, and indirectly from the property of the concepet nodes.
For example, "PMF" has a property "Non-negativity". At the same time, "PMF of Poisson Distribution" is a child concept of "PMF". Then "PMF of Poisson Distribution" inherits the property "Non-negativity" from "PMF".


For the sake of maintaining only one copy of any information, info related to other nodes would be presented with a reference link that only gets rendered out when the user zooms in to the node in the interface.
</ignore>
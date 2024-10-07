# Property Node Schema

## Properties (Attributes)

- **Name**: *String*
  - The official name of the property.
  - *Example*: "Non-negativity"
  - **Aliases**: *List of Strings*
    - Alternative names or synonyms for the property.
    - *Example*: ["Positivity", "Non-negative Function"]

- **Definition**: *Text*
  - A precise and formal definition of the property.
  - *Example*: "A function \( f \) is non-negative if \( f(x) \geq 0 \) for all \( x \) in its domain."
  - **Notation**: *String/Text* (LaTeX)
    - Symbols or mathematical notation associated with the property. Show LaTeX code and rendered LaTeX side by side.
    - *Example*: "f(x) ≥ 0" $f(x) \geq 0$
  - **Alias Notation**: *String/Text* (LaTeX)
    - Alternative notations for the property. Show LaTeX code and rendered LaTeX side by side.
    - *Example*: "f ≥ 0" $f \geq 0$
  - **Description**: *Text*
    - Additional explanations, background information, or context about the property.
    - *Example*: "Non-negativity ensures that certain quantities, like probabilities or variances, are always zero or positive."
  > NEED TO mark SOURCE for the information used here. By default we will use `Stat400 teaching material - Jonathan Fernandez`

- **Tags/Categories**: *List of Strings*
  - Keywords that categorize the property.
  - *Example*: ["Probability", "Function Properties"]

- **Knowledge**
  - Specific or rare knowledge about the property that doesn't fit into other sections.
  - Will be represented in terms of properties with relation links.
  - This part might need further specification after labeling more nodes.

## Relationships (Edges)

- **is_property_of** → *Concept*/*Theorem* (the reverse of **has_property**)
  - Concepts or theorems that possess this property.
  - *Example*: "Non-negativity" is a property of "Probability Mass Function"

- **related_to** → *Property* (the reverse of **is_related_to**)
  - Properties that are related or frequently associated.
  - *Example*: "Non-negativity" is related to "Normalization"

- **implied_by** → *Theorem* (the reverse of **implies_property**)
  - Theorems that imply this property.
  - *Example*: "Kolmogorov's Axioms" imply "Non-negativity"

- **depends_on** → *Property* (the reverse of **is_prerequisite_of**)
  - Other properties that are prerequisites for understanding this property.
  - *Example*: "Non-negativity" depends on "Real-valued Functions"

- **has_subproperty** → *Property* (the reverse of **is_subproperty_of**)
  - More specific properties derived from the current property.
  - *Example*: "Strict Positivity" is a subproperty of "Non-negativity"

- **has_application** → *Application Example* (the reverse of **is_application_of**)
  - Real-world applications where the property is relevant.
  - *Example*: "Ensuring probabilities in a probabilistic model are non-negative"

- **has_exercise** → *Exercise* (the reverse of **is_exercise_for**)
  - Exercises that involve the property.
  - *Example*: "Exercise 2.1.5"

- **related_to** → *Concept*/*Theorem* (the reverse of **is_related_to**)
  - Non-hierarchical connections to concepts or theorems that are related.
  - *Example*: "Non-negativity" related to "Probability Distribution"

## Information to be additionally Rendered When Student Zooms In on Node

For the sake of maintaining only one copy of any information, info related to other nodes would be presented with a reference link that only gets rendered out when the user zooms in to the node in the interface.

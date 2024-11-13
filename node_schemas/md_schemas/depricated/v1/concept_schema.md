# Concept Node Schema

## Attributes

- **Name**: *String*
  - Uniform discrete distribution
  - **Aliases**: *List of Strings*
    - Synonyms or alternative names for the concept. 
    - *Example*: ["Marginal Probability", "Posterior Probability"]

- **Definition**: *Text*
  - A precise and formal definition of the concept.
  - *Example*: "The probability of an event occurring given that another event has already occurred."
  - **Notation**: *String/Text* (Latex)
    - Symbols or mathematical notation associated with the concept. Show latex code and rendered latex side by side.
    - *Example*: "P(A|B)" $P(A|B)$
  - **Alias Notation**: *String/Text* (Latex)
    - Alternative notations for the concept. Show latex code and rendered latex side by side. 
    - *Example*: "P(A|B)" $P(A|B)$
  - **Description**: *Text*
    - Additional explanations, background information, or context about the concept.
    - *Example*: "Conditional probability quantifies the likelihood of an event A occurring when event B is known."
  > NEED TO MARK SOURCE for the information used here. By default we will use `Stat400 teaching material - Jonathan Fernandez`

- **Tags/Categories**: *List of Strings*
  - Keywords that provide information other than dependency relation... may not be necessary.
  - *Example*: ["Probability Theory", "Statistics"]

- **Knowledge** (optional)
  - Knowledge that are so specific/rare as to no qualify the use of separate property/relation section.
  - Will be represetned in terms of properties with relation link.
  - This part might need to be further specified after labeling some nodes to create more generalized sections in schema.

## Relationships (Edges)
- **has_subconcept** → *Concept* (the reverse of **is_subconcept_of** ←)
  - Points to more specific or narrower concepts derived from the current concept.
  - *Example*: "Conditional Probability" has subconcepts like "Conditional Density Function"

- **is_prerequisite_of** → *Concept* (the reverse of **depends_on** ←)
  - Indicates prerequisite concepts required for understanding the current concept. (not as strong as "subconcept of")
  - *Example*: "Conditional Probability" depends on "Basic Probability Concepts"

- **has_property** → *Property* (the reverse of **is_property_of**)
  - Properties that describe attributes or characteristics of the concept.
  - *Example*: Links to properties like "Non-negativity" or "Normalization"

### Relation regarding theorem
- **involved_in** → *Theorem* (the reverse of **involves_concept**)
  - Theorems where the concept plays a crucial role as part of hypothesis/assumption, yet not as part of hypothesis/assumption.
  - *Example*: "Conditional Probability" is involved in "Bayes' Theorem"
#### More specific version of relation with theorem:
- **is_prerequisite_of** → *Theorem* (the reverse of **depends_on**)
  - Theorems that the concept is a prerequisite of.
  - *Example*: "Time" is a prerequisite of "Speed".
- **concludes_from** ← *Theorem* (the reverse of **concludes**)
  - Theorems that concludes with the concept as result.
  - *Example*: "Bayes' Theorem" concludes with "Bayes' Rule"

### Relation regarding exercise/application
- **involved_in** (optional) (less strict than **has_application/has_exercise**) → *Exercise/Application Example* (the reverse of **involves_concept**; Is less strict than other relation like **is_exercise_for** or **is_application_of**)
  - Exercises where the concept is involved as part of solving the exercise;
  - *Example*: "Conditional Probability" is involved in "Exercise 3.2.1" (not the main focus of the exercise, but it is used to solve it)
#### More specific version of relation with exercise:
- **has_application** → *Application Example* (the reverse of **is_application_of**)
  - Real-world applications, instances, or use-cases where the concept is applied.
  - *Example*: Applications in "Spam Filtering" or "Risk Assessment"
- **has_exercise** → *Exercise* (the reverse of **is_exercise_for**)
  - Exercises that require the concept.
  - *Example*: "Exercise 3.2.1"


- **related_to** → *Concept* (the reverse of **is_related_to**)
  - Non-hierarchical connections to concepts that are related or frequently associated.
  - Most general relation type for relations unclassifiable to above relation types.
  - *Example*: "Conditional Probability" related to "Bayes' Theorem"


## Additional information to render for Student who zoomin
For sake of maintaining only one copy of any information, info related to other nodes would be presented with reference link, that only get rendered out when user zoom in to the node in the interface.

> "Sibling of" relation; Look for hiearchical parent and mark siblings of current node on different axis. Rendered real time not stored in node. Or rerendered whenever db is changed after initialization.
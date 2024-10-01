# Concept Node Schema

## Properties (Attributes)

- **Name**: *String*
  - The primary name of the concept.
  - *Example*: "Conditional Probability"

- **Definition**: *Text*
  - A precise and formal definition of the concept.
  - *Example*: "The probability of an event occurring given that another event has already occurred."

- **Notation**: *String/Text* (Latex)
  - Symbols or mathematical notation associated with the concept.
  - *Example*: "P(A|B)" $P(A|B)$

- **Aliases**: *List of Strings*
  - Synonyms or alternative names for the concept. 
  - *Example*: ["Marginal Probability", "Posterior Probability"]

- **Description**: *Text*
  - Additional explanations, background information, or context about the concept.
  - *Example*: "Conditional probability quantifies the likelihood of an event A occurring when event B is known."

- **Tags/Categories**: *List of Strings*
  - Keywords for classification and easy retrieval.
  - *Example*: ["Probability Theory", "Statistics"]

- **Examples**: *List of References to Application Nodes*
  - Links to illustrative examples or use-cases that demonstrate the concept.
  - *Example*: References to application nodes like "Medical Diagnostic Testing"

## Relationships (Edges)

- **is_subconcept_of** → *Concept*
  - Hierarchical relationship pointing to a broader or parent concept.
  - *Example*: "Conditional Probability" is a subconcept of "Probability"

- **has_subconcept** → *Concept*
  - Points to more specific or narrower concepts derived from the current concept.
  - *Example*: "Conditional Probability" has subconcepts like "Conditional Density Function"

- **related_to** → *Concept*
  - Non-hierarchical connections to concepts that are related or frequently associated.
  - *Example*: "Conditional Probability" related to "Bayes' Theorem"

- **depends_on** → *Concept*
  - Indicates prerequisite concepts required for understanding the current concept.
  - *Example*: "Conditional Probability" depends on "Basic Probability Concepts"

- **has_property** → *Property*
  - Properties that describe attributes or characteristics of the concept.
  - *Example*: Links to properties like "Non-negativity" or "Normalization"

- **involves_in** → *Theorem*
  - Theorems where the concept plays a crucial role.
  - *Example*: "Conditional Probability" is involved in "Bayes' Theorem"

- **has_application** → *Application Example*
  - Real-world applications, instances, or use-cases where the concept is applied.
  - *Example*: Applications in "Spam Filtering" or "Risk Assessment"

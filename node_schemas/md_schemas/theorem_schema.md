# Theorem Node Schema

## Attributes

- **Name**: *String*
  - The official name of the theorem.
  - *Example*: "Bayes' Theorem"
  - **Aliases**: *List of Strings*
    - Alternative names or references for the theorem.
    - *Example*: ["Bayes' Rule", "Bayes' Law"]


- **Statement**: *Text*
  - The formal and precise statement of the theorem.
  - *Example*: "P(A|B) = [P(B|A) * P(A)] / P(B)"
  - **Axioms/Premises**: *List of Text*
    - Conditions or premises under which the theorem holds true.
    - *Example*: ["P(B) > 0", "All probabilities are defined over the same probability space"]  
  - **Conclusion**: *Text*
    - The result or conclusion of the theorem.
    - *Example*: "P(A|B) = [P(B|A) * P(A)] / P(B)"

- **Description**: *Text*
  - Additional context, such as historical background or significance.
  - *Example*: "Bayes' Theorem provides a way to update probabilities based on new evidence."

- **Proof**: *Text & Latex*
  - A logical argument establishing the truth of the theorem from the hypotheses, including step-by-step deductions.
  - *Example*: Detailed derivation using definitions of conditional probability

- **Tags/Categories**: *List of Strings*
  - Keywords that provide information other than dependency relation... may not be necessary.
  - *Example*: ["Probability Theory", "Statistics"]

- **Knowledge**
  - Knowledge that are so specific/rare as to no qualify the use of separate property/relation section.
  - Will be represetned in terms of properties with relation link.
  - This part might need to be further specified after labeling some nodes to create more generalized sections in schema.

## Relationships (Edges)
- **involves_concept** ← *Concept* (the reverse of **involved_in_theorem**)
  - Concepts not part of hypothesis/assumption, but used in proof.
  - *Example*: Links to "Conditional Probability", "Marginal Probability"
### Inbound Relations/Prerequisites (? a better name for this section?)
- **depends_on** ← *Concept* (the reverse of **is_prerequisite_of**)
- **needs_property** ← *Property* (the reverse of **has_property**)
  - Properties that are necessary for the theorem which doesn't fit in any concept involved in the theorem.
  - *Example*: (?) may not be necessary. can't quite think of any examples yet.

- **uses_theorem** ← *Theorem* (the reverse of **used_to_prove**)
  - Other theorems referenced or utilized within the proof, but not as part of hypothesis/assumption.
  - *Example*: 
- **is_corollary_of** ← *Theorem* (the reverse of **is_basis_for**, more specific than **uses_theorem**)
  - Indicates if the theorem is a corollary derived from another theorem.
  - *Example*: A corollary of "Bayes' Theorem" is "Law of Total Probability"

### Outbound Relations/Results
- **concludes** → *List ofProperty*/*Concept* (the reverse of **derived_from(theorem)**)
  - Concepts that are derived from the theorem.
  - *Example*: "Negative Binomial Distribution"

### Other Relations
- **is_generalization_of** → *Theorem* (the reverse of **is_specialization_of**)
  - Links to more specific cases or special instances of the theorem.
  - *Example*: Connecting "Bayes' Theorem for Continuous Variables"

- **has_application** → *Application Example* (the reverse of **is_application_of**)
  - Examples where the theorem is applied to solve problems.
  - *Example*: "Medical Diagnosis Probability Calculation"
- **has_exercise** → *Exercise* (the reverse of **is_exercise_for**)
  - Exercises that apply the theorem.
  - *Example*: "Exercise 3.2.1"

- **involved_in** → *Exercise/Application Example* (the reverse of **involves_theorem**; Is less strict than other relation like **is_exercise_for** or **is_application_of**)
  - Exercises where the concept is involved as part of solving the exercise.
  - *Example*: "Conditional Probability" is involved in "Exercise 3.2.1" (not the main focus of the exercise, but it is used to solve it)

- **non-directional relation** ←→ *Concept* (the reverse of **is_related_to**)
  - I can't think of any generalized non-directional relation yet, other than the one mentioned by Fernandez about the conversion between one probability distribution and another under certain conditions. But that is probably better of modeled by two theorems going from either side to the other.
  - Serve as a placeholder for general non-directional relation between concept and other nodes.
  - *Example*: "Conditional Probability" related to "Bayes' Theorem"
  - This part might need to be further specified after labeling some nodes; so as to create more generalized sections in schema.




## Additional information to render for Student who zoomin
For sake of maintaining only one copy of any information, info related to other nodes would be presented with reference link, that only get rendered out when user zoom in to the node in the interface.

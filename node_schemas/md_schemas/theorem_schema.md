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

- **Description**: *Text* (optional)
  - Additional context, such as historical background or significance.
  - *Example*: "Bayes' Theorem provides a way to update probabilities based on new evidence."

- **Proof**: *Text & Latex* (optional)
  - A logical argument establishing the truth of the theorem from the hypotheses, including step-by-step deductions.
  - *Example*: Detailed derivation using definitions of conditional probability



## Relationships (Edges)

### Inbound Relations/Prerequisites
- **is_prerequisite_of** <= (i.e. **depends_on** =>) *Concept/Theorem/Property* {concept_name/theorem_name/property_name}
  - Concepts/Theorems/Properties that are used in proving this theorem.
  - *Example*: "Conditional Probability" (concept) is a prerequisite of "Bayes' Theorem" (theorem); is a prerequisite of theory of "theory of large 

### Outbound Relations/Results
- **concludes** => (i.e. **derived_from(theorem)** <=) *List of Properties/Concepts* {property_name/concept_name}
  - Concepts/Properties that are derived from the theorem.
  - *Example*: "Negative Binomial Distribution"

<ignore>
!!! separate "used to prove" and "used to setup"? NO! a theorem isn't necessarily going from a set of fixed input to a set of fixed output.
Two types of theorems: One that is an equivalence that doens't have direction, and the other is a directional derivation;
Even for the directional derivation, the theorem doesn't necessarily have to have fixed input; input can be a mixture of different level in a proof; as long as the "tree" of theorem lead to the output.
"atomize" all theorems, where any more complex theorem should conditionally be atomized into sub theorems that have naive input and output;
"collectivize" some theorems for efficient query... need more discussion on this.

Proving of theorem vs. usage of theorem. The usage of theorem 
!!! **There should not be a single outbound; instead, the outbound should be the graph of theorem that is used in run-time.**


### Other Relations
- **is_corollary_of** ← *Theorem* {theorem_name} (the reverse of **is_basis_for**, more specific than **uses_theorem**)
  - Indicates if the current theorem is a corollary derived from another theorem.
  - *Example*: "Bayes' Theorem" is a corollary of "conditional Probability"

- **involved_in_theorem** ← *Concept* {concept_name} (the reverse of **involves_concept**)
  - Concepts not part of hypothesis/assumption, but used in proof.
  - *Example*: Links to "Conditional Probability", "Marginal Probability"




> LOG IN THE OTHER SIDE OF ALL FOLLOWING RELATIONSHIPS

- **has_application** → *Application Example* {application_name} (the reverse of **is_application_of**)
  - Examples where the theorem is applied to solve problems.
  - *Example*: "Medical Diagnosis Probability Calculation"
- **has_exercise** → *Exercise* {exercise_name} (the reverse of **is_exercise_for**)
  - Exercises that apply the theorem.
  - *Example*: "Exercise 3.2.1"

## Additional information to render for Student who zoomin
For sake of maintaining only one copy of any information, info related to other nodes would be presented with reference link, that only get rendered out when user zoom in to the node in the interface.
</ignore>

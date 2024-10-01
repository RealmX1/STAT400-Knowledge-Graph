# Theorem Node Schema

## Properties (Attributes)

- **Name**: *String*
  - The official name of the theorem.
  - *Example*: "Bayes' Theorem"

- **Statement**: *Text*
  - The formal and precise statement of the theorem.
  - *Example*: "P(A|B) = [P(B|A) * P(A)] / P(B)"

- **Hypotheses/Assumptions**: *List of Text*
  - Conditions or premises under which the theorem holds true.
  - *Example*: "P(B) > 0", "All probabilities are defined over the same probability space"

- **Proof**: *Text*
  - A logical argument establishing the truth of the theorem from the hypotheses, including step-by-step deductions.
  - *Example*: Detailed derivation using definitions of conditional probability

- **Aliases**: *List of Strings*
  - Alternative names or references for the theorem.
  - *Example*: ["Bayes' Rule", "Bayes' Law"]

- **Description**: *Text*
  - Additional context, such as historical background or significance.
  - *Example*: "Bayes' Theorem provides a way to update probabilities based on new evidence."

- **Tags/Categories**: *List of Strings*
  - Keywords for classification.
  - *Example*: ["Probability Theorems", "Statistics"]

## Relationships (Edges)

- **involves_concept** → *Concept*
  - Concepts that are essential components of the theorem.
  - *Example*: Links to "Conditional Probability", "Marginal Probability"

- **uses_theorem** → *Theorem*
  - Other theorems referenced or utilized within the proof.
  - *Example*: "Law of Total Probability"

- **is_corollary_of** → *Theorem*
  - Indicates if the theorem is a corollary derived from another theorem.
  - *Example*: A corollary of "Bayes' Theorem" might be linked here

- **is_generalization_of** → *Theorem*
  - Links to more specific cases or special instances of the theorem.
  - *Example*: Connecting "Bayes' Theorem for Continuous Variables"

- **has_application** → *Application Example*
  - Examples where the theorem is applied to solve problems.
  - *Example*: "Medical Diagnosis Probability Calculation"

- **implies_property** → *Property*
  - Properties or principles that are derived from the theorem.
  - *Example*: "Inverse Probability" property

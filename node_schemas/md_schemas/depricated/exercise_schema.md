# Exercise Node Schema

> 10/07 No need to look into this in detail for the moment;



## Attributes

- **Title**: *String*
  - A brief title or identifier for the exercise.
  - *Example*: "Exercise 3.2.1"

- **Problem Statement**: *Text*
  - The text of the exercise or problem.
  - *Example*: "Given events A and B, where P(A) = 0.3 and P(B) = 0.5, and P(A ∩ B) = 0.15, compute P(A|B)."
  - **Notation**: *String/Text* (LaTeX)
    - Mathematical notation used in the problem. Show LaTeX code and rendered LaTeX side by side.
    - *Example*: "P(A ∩ B)" $P(A \cap B)$
  - **Diagram/Illustration**: *Image*
    - Any visual aids that accompany the problem.
    - *Example*: Venn diagram illustrating events A and B.

- **Solution**: *Text*
  - A detailed solution to the exercise.
  - *Example*: "Using the definition of conditional probability, \( P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{0.15}{0.5} = 0.3 \)."
  - **Step-by-Step Explanation**: *List of Text*
    - Detailed steps explaining how the solution is obtained.
    - *Example*: ["Compute \( P(A \cap B) \)", "Use the formula for conditional probability", "Simplify the expression"]

- **Hints**: *List of Text*
  - Hints or guidance to help solve the exercise.
  - *Example*: ["Recall the definition of conditional probability", "Ensure that all probabilities are within [0,1]"]

- **Difficulty Level**: *String*
  - An indication of the difficulty level.
  - *Example*: "Beginner"

- **Tags/Categories**: *List of Strings*
  - Keywords that categorize the exercise.
  - *Example*: ["Conditional Probability", "Basic Probability"]

- **Knowledge**
  - Specific or rare knowledge about the exercise that doesn't fit into other sections.
  - Will be represented in terms of properties with relation links.
  - This part might need further specification after labeling more nodes.

> NEED TO mark SOURCE for the information used here. By default we will use `Stat400 teaching material - Jonathan Fernandez`

## Relationships (Edges)

- **is_exercise_for** → *Concept*/*Theorem*/*Property* (the reverse of **has_exercise**)
  - Concepts, theorems, or properties that the exercise is about.
  - *Example*: "Conditional Probability"

- **involves_concept** → *Concept* (the reverse of **involved_in_exercise**)
  - Concepts that are prerequisites for solving the exercise.
  - *Example*: "Joint Probability", "Marginal Probability"
- **involves_theorem** → *Theorem* (the reverse of **involved_in_exercise**)
  - Theorems that are prerequisites for solving the exercise.
  - *Example*: "Bayes' Theorem"

- **uses_theorem** → *Theorem* (the reverse of **used_in_exercise**)
  - Theorems needed to solve the exercise.
  - *Example*: "Definition of Conditional Probability"

- **related_to** → *Exercise* (the reverse of **is_related_to**)
  - Other exercises that are related.
  - *Example*: "Exercise 3.2.2"

- **is_exercise_for** → *Application Example* (the reverse of **derives_exercise**)
  - Application examples that the exercise is based on or related to.
  - *Example*: "Medical Diagnosis using Conditional Probability"

## Information to be additionally Rendered When Student Zooms In on Node

For the sake of maintaining only one copy of any information, info related to other nodes would be presented with a reference link that only gets rendered out when the user zooms in to the node in the interface.

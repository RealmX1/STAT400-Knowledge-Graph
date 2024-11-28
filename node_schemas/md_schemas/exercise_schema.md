# Exercise Node Schema

> 10/07 No need to look into this in detail for the moment;



## Attributes

- **Name**: *String*
  - A brief title or identifier for the exercise.
  - *Example*: "Exercise 3.2.1 Poisson Distribution Shopper Passing Through Store Front"

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

- **Hints**: *List of Text* (optional)
  - Hints or guidance to help solve the exercise.
  - *Example*: ["Recall the definition of conditional probability", "Ensure that all probabilities are within [0,1]"]

- **Difficulty Level**: *String* (optional)
  - An indication of the difficulty level.
  - *Example*: "Beginner"

- **Knowledge** (optional)
  - Specific or rare knowledge about the exercise that doesn't fit into other sections.
  - Will be represented in terms of properties with relation links.
  - This part might need further specification after labeling more nodes.

> NEED TO mark SOURCE for the information used here. By default we will use `Stat400 teaching material - Jonathan Fernandez`

## Relationships (Edges)

- **is_exercise_for** <= *Concept*/*Theorem*/*Property*/*Application Example* [list of concept/theorem/property/application names] (the reverse of **has_exercise**) 
  - A list of all nodes that the exercise is about. Concepts, theorems, properties, or application examples that the exercise is about.
  - *Example*: ["Conditional Probability",]

- **involves_concept** => *Concept*/*Theorem*/*Property* [list of concept/theorem/property names] (the reverse of **involved_in_exercise**)
  - Involves concept/theorem/property, but not as built as an exercise for it.
  - *Example*: ["Joint Probability", "Marginal Probability", "Bayes' Theorem", "Non-negativity"]

- **related_to** <=> *Exercise* [list of exercise names] (the reverse of **is_related_to**) (optional)
  - Other exercises that are related. For helping student get similar (but different) exercise.
  - *Example*: ["Exercise 3.2.2 asdf", "Exercise 3.2.3 asdf"]

## Information to be additionally Rendered When Student Zooms In on Node
### When rendering concept node, extract all "knowledge" section from its related exercises" and display them in a list in the attribute section of the concept node.
For the sake of maintaining only one copy of any information, info related to other nodes would be presented with a reference link that only gets rendered out when the user zooms in to the node in the interface.

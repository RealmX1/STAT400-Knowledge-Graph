# Application Example Node Schema

## Properties (Attributes)

- **Title**: *String*
  - The title or brief description of the application example.
  - *Example*: "Using Bayes' Theorem for Medical Diagnosis"

- **Description**: *Text*
  - A detailed explanation of the application example, including context and significance.
  - *Example*: "Calculating the probability that a patient has a disease given a positive test result using Bayes' Theorem."
  - **Procedure/Steps**: *List of Text*
    - Step-by-step procedure or methodology followed in the application.
    - *Example*: ["Determine prior probability of the disease", "Use test sensitivity and specificity", "Apply Bayes' Theorem to compute posterior probability"]
  - **Results**: *Text*
    - The outcome or results obtained from the application.
    - *Example*: "The posterior probability indicates that despite a positive test result, the patient has a low probability of having the disease due to its rarity."
  - **Conclusion**: *Text*
    - Any conclusions or implications drawn from the application.
    - *Example*: "Highlights the importance of considering base rates in diagnostic testing."
  > NEED TO mark SOURCE for the information used here. By default we will use `Stat400 teaching material - Jonathan Fernandez`

- **Tags/Categories**: *List of Strings*
  - Keywords that categorize the application example.
  - *Example*: ["Medical Statistics", "Bayesian Inference"]

- **Knowledge**
  - Specific or rare knowledge about the application that doesn't fit into other sections.
  - Will be represented in terms of properties with relation links.
  - This part might need further specification after labeling more nodes.

## Relationships (Edges)

- **is_application_of** → *Concept*/*Theorem*/*Property* (the reverse of **has_application**)
  - Concepts, theorems, or properties that are applied in this example.
  - *Example*: "Bayes' Theorem"

- **involves_concept** → *Concept* (the reverse of **involved_in_application**)
  - Concepts that are involved in the application.
  - *Example*: "Conditional Probability", "Prior Probability"

- **uses_theorem** → *Theorem* (the reverse of **used_in_application**)
  - Theorems used in the application.
  - *Example*: "Bayes' Theorem"

- **demonstrates_property** → *Property* (the reverse of **demonstrated_by**)
  - Properties that are illustrated through the application.
  - *Example*: "Law of Total Probability"

- **related_to** ←→ *Application Example* (the reverse of **is_related_to**)
  - Other application examples that are related.
  - *Example*: "Spam Filtering using Bayes' Theorem"

- **derives_exercise** → *Exercise* (the reverse of **is_exercise_for**)
  - Exercises derived from the application example.
  - *Example*: "Exercise 4.3.2"

## Information to be additionally Rendered When Student Zooms In on Node

For the sake of maintaining only one copy of any information, info related to other nodes would be presented with a reference link that only gets rendered out when the user zooms in to the node in the interface.

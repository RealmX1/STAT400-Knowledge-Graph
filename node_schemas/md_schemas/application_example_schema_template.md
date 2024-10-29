# Application Example Node Schema

## Properties (Attributes)

- **Name**: *String*
  - The title or brief description of the application example.
  - *Example*: "Using Bayes' Theorem for Medical Diagnosis"

- **Description**: *Text*
  - A detailed explanation of the scenario in which the concept/theorem/property is applied. 
  - *Example*: "
    - Given that the test has a 95% accuracy rate, and the disease is rare (only 1% of the population has it), Bayes' Theorem can be used to calculate the probability that the patient actually has the disease given the test result.
  - **Mapping from scenario to notation**:
    - Formalize/Symbalize the scenario by create a mapping from natural language description in the scenario to the notation of the concept/theorem/property. (Assumptions can be made if necessary for evaluation step)
    - *Example*:
      - "Test has a 95% accuracy rate" → $P(Positive Test|Disease) = 0.95$
      - "Disease is rare with only 1% of the population having it" → $P(Disease) = 0.01$
      - "Calculate the probability that the patient actually has the disease given the test result" → $P(Disease|Positive Test)$
  - **Deriving the result** (optional):
    - Derive the result given the formalized information about the scenario.
    - *Example*:
      - $P(Disease|Positive Test) = P(Positive Test|Disease) * P(Disease) / P(Positive Test)$
      - $P(Disease|Positive Test) = 0.95 * 0.01 / 0.0595$
      - $P(Disease|Positive Test) = 0.1597$
      - The probability that the patient actually has the disease given the test result is 15.97%."
  > NEED TO mark SOURCE for the information used here. By default we will use `Stat400 teaching material - Jonathan Fernandez`

## Relationships (Edges)

- **is_application_of** → *Concept*/*Theorem*/*Property* (the reverse of **has_application**)
  - Concepts, theorems, or properties that are applied in this example.
  - *Example*: "Bayes' Theorem"

- **involves** → *Concept*/*Theorem*/*Property* (the reverse of **involved_in_application**)
  - Concepts that are involved in the application.
  - *Example*: "Conditional Probability", "Prior Probability"

- **has_exercise** → *Exercise* (the reverse of **is_exercise_for**)
  - Exercises derived from the application example.
  - *Example*: "Exercise 4.3.2"

## Information to be additionally Rendered When Student Zooms In on Node

For the sake of maintaining only one copy of any information, info related to other nodes would be presented with a reference link that only gets rendered out when the user zooms in to the node in the interface.

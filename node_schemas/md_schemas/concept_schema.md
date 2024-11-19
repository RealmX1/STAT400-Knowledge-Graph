# Concept Node Schema

## Attributes

- **Name**: *String*
  - Uniform discrete distribution
  - **Aliases**: *List of Strings*
    - Synonyms or alternative names for the concept. 
    - *Example*: Poisson Distribution
- **Definition**:
  - **Notation**: *String* (Latex)
    - Symbols or mathematical notations associated with the concept in latex format.
    - *Example*: 
      - Pois(\lambda)
      - **Explanation**: *List of Objects*
        - Disect the notation and explain each part. Should have range (if applicable) and description for each respective part.
        - *Example*:
          - $\lambda$ 
            - Range: $\lambda \in \{0, \infty\}$
            - Description:represent average rate or mean number of occurrences of the event being modeled. 
  - **Description**: *Text*
    - Additional explanations, background information, or context about the concept.
    - *Example*: "Poisson Distribution is a discrete probability distribution that describes the number of times an event occurs within a fixed interval of time or space. It assumes that events occur with a constant mean rate and are independent of the time since the last event."



## Relationships
### Relation regarding concept

- **has_subconcept** → *Concept* (the reverse of **is_subconcept_of** ←)
  - Points to more specific or narrower concepts derived from the current concept.
  - *Example*: "Conditional Probability" has subconcepts like "Conditional Density Function"

- **is_prerequisite_of** → *Concept* (the reverse of **depends_on** ←)
  - Indicates prerequisite concepts required for understanding the current concept. (not as strong as "subconcept of")
  - *Example*: "Time" is a prerequisite of "Speed".

- **related_to** -- *Concept* (the reverse of **is_related_to**) (VERY OPTIONAL)
  - Most general (non-specific) relation type regarding other concept 
  - Non-hierarchical connections to concepts that are related or frequently associated.
  - Most general relation type for relations unclassifiable to above relation types.
  - If any more explicit relation already exist between current node and the end concept candidate for this one (either marked in current node or end concept), then do not create a new relation.
  - *Example*: ?


  > NEED TO MARK SOURCE for the information used here. By default we will use `Stat400 teaching material - Jonathan Fernandez`


> LOG IN THE OTHER SIDE OF ALL FOLLOWING RELATIONSHIPS
- **has_property** → *Property* (the reverse of **is_property_of**)
  - Properties that describe attributes or characteristics of the concept.
  - *Example*:"Poisson Random Variable" has property "Variance of Poisson Random Variable"; "Variance of Poisson Random Variable" is a child concept of "Variance of random variable" 

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



## Additional information to render for Student who zoomin
For sake of maintaining only one copy of any information, info related to other nodes would be presented with reference link, that only get rendered out when user zoom in to the node in the interface.

> "Sibling of" relation; Look for hiearchical parent and mark siblings of current node on different axis. Rendered real time not stored in node. Or rerendered whenever db is changed after initialization.
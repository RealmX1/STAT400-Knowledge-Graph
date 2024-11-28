create json schema from the following markdown. The schema will be used as schema for GPT4-o's formated output. Each bold section represent a new entry in the schema. Carefully encode the indentation as hiearchy in json.
In relation section, '←' or '<-' means the relation has this node as the target and the node following the symbol as source; '→' or '->' means the relation has this node as the source and the node following it is the target; '↔' or '<->' means the relation is bidirectional; '=' or '-' or '--' means the relation is undirected. So the direction of each type of relation should be one of ['to', 'from', 'bidirectional', 'undirected'].
Note that all fields must be required (and the model will return a value for each parameter)
emulate an optional parameter by using a union type with null: 
"unit": {
    "type": ["string", "null"],
    "description": "The unit to return the temperature in",
    "enum": ["F", "C"]
},
"required": ["unit"]
In the relationship section, each relation can have multiple instances -- there can be multiple target node that have each relationship with the current node.
Any information from input wrapped in <ignore> tag, or in markdown comment (<!--asdf-->) should not be taken into consideration.

Here is an example of successful conversion:
<conversion_example>
<input>
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

<ignore>
<!-- Information in ignore tag should not be taken into consideration by LLM -->
<depricated>
- **related_to** -- *Concept* (the reverse of **is_related_to**) (VERY OPTIONAL)
  - Most general (non-specific) relation type regarding other concept 
  - Non-hierarchical connections to concepts that are related or frequently associated.
  - Most general relation type for relations unclassifiable to above relation types.
  - If any more explicit relation already exist between current node and the end concept candidate for this one (either marked in current node or end concept), then do not create a new relation.
  - *Example*: ?
  <!-- This is depricated because, now that we only log the relation in one direction, relation not logged in current node can result in unwanted "related_to" relation -- for example, in the case of Poisson Distritubution, "Discrete Distrubution" has it as a subconcept, so there is no need for an "related_to" relation created on the Poisson Distrubution; yet LLM usually logs this relation. -->
</depricated>


  > NEED TO MARK SOURCE for the information used here. By default we will use `Stat400 teaching material - Jonathan Fernandez`


> LOG IN THE OTHER SIDE OF ALL FOLLOWING RELATIONSHIPS
- **has_property** → *Property* {property_name} (the reverse of **is_property_of**)
  - Properties that describe attributes or characteristics of the concept.
  - *Example*:"Poisson Random Variable" has property "Variance of Poisson Random Variable"; "Variance of Poisson Random Variable" is a child concept of "Variance of random variable" 

### Relation regarding theorem
- **involved_in** → *Theorem* {theorem_name} (the reverse of **involves_concept**) 
  - Theorems where the concept plays a crucial role as part of hypothesis/assumption, yet not as part of hypothesis/assumption.
  - *Example*: "Conditional Probability" is involved in "Bayes' Theorem"
#### More specific version of relation with theorem:
- **is_prerequisite_of** → *Theorem* {theorem_name} (the reverse of **depends_on**)
  - Theorems that the concept is a prerequisite of.
  - *Example*: "Time" is a prerequisite of "Speed".
- **concludes_from** ← *Theorem* {theorem_name} (the reverse of **concludes**)
  - Theorems that concludes with the concept as result.
  - *Example*: "Bayes' Theorem" concludes with "Bayes' Rule"

### Relation regarding exercise/application
- **involved_in** (optional) (less strict than **has_application/has_exercise**) → *Exercise/Application Example* {exercise_or_application_name} (the reverse of **involves_concept**; Is less strict than other relation like **is_exercise_for** or **is_application_of**)
  - Exercises where the concept is involved as part of solving the exercise;
  - *Example*: "Conditional Probability" is involved in "Exercise 3.2.1" (not the main focus of the exercise, but it is used to solve it)



## Additional information to render for Student who zoomin
For sake of maintaining only one copy of any information, info related to other nodes would be presented with reference link, that only get rendered out when user zoom in to the node in the interface.

> "Sibling of" relation; Look for hiearchical parent and mark siblings of current node on different axis. Rendered real time not stored in node. Or rerendered whenever db is changed after initialization.
</ignore>
</input>

<output>
{
  "name": "concept_node_schema",
  "strict": true,
  "schema": {
    "type": "object",
    "properties": {
      "node_type": {
        "type": "string",
        "enum": ["concept"]
      },
      "attributes": {
        "type": "object",
        "properties": {
          "name": {
            "type": "object",
            "properties": {
              "value": {
                "type": "string",
                "description": "Uniform discrete distribution"
              },
              "aliases": {
                "type": ["array", "null"],
                "items": {
                  "type": "string"
                },
                "description": "Synonyms or alternative names for the concept"
              }
            },
            "required": ["value", "aliases"],
            "additionalProperties": false
          },
          "definition": {
            "type": "object",
            "properties": {
              "notation": {
                "type": "string",
                "description": "Symbols or mathematical notations associated with the concept in latex format"
              },
              "explanation": {
                "type": ["array", "null"],
                "items": {
                  "type": "object",
                  "properties": {
                    "part": {
                      "type": "string"
                    },
                    "range": {
                      "type": ["string", "null"],
                      "description": "The range of the respective part, if applicable"
                    },
                    "description": {
                      "type": "string",
                      "description": "Description of the respective part"
                    }
                  },
                  "required": [
                    "part",
                    "range",
                    "description"
                  ],
                  "additionalProperties": false
                },
                "description": "Dissects the notation and explains each part"
              }
            },
            "required": [
              "notation",
              "explanation"
            ],
            "additionalProperties": false
          },
          "description": {
            "type": "string",
            "description": "Additional explanations, background information, or context about the concept"
          }
        },
        "required": [
          "name",
          "definition",
          "description"
        ],
        "additionalProperties": false
      },
      "relationships": {
        "type": "object",
        "properties": {
          "has_subconcept": {
            "type": ["object", "null"],
            "properties": {
              "target_node_type": {
                "type": "string",
                "enum": ["concept"],
                "description": "Type of the end nodes at the other end of the relationship."
              },
              "target_nodes": {
                "type": ["array", "null"],
                "items": {
                  "$ref": "#/$defs/target_node"
                },
                "description": "Names of end nodes that this concept is related to."
              },
              "direction": {
                "type": "string",
                "enum": ["to"],
                "description": "Direction of the relationship."
              }
            },
            "required": ["target_node_type", "target_nodes", "direction"],
            "additionalProperties": false,
            "description": "Points to more specific or narrower concepts derived from the current concept."
          },
          "is_prerequisite_of": {
            "type": ["object", "null"],
            "properties": {
              "target_node_type": {
                "type": "string",
                "enum": ["concept"],
                "description": "Type of the end nodes at the other end of the relationship."
              },
              "target_nodes": {
                "type": ["array", "null"],
                "items": {
                  "$ref": "#/$defs/target_node"
                },
                "description": "Names of end nodes that this concept is related to."
              },
              "direction": {
                "type": "string",
                "enum": ["to"],
                "description": "Direction of the relationship."
              }
            },
            "required": ["target_node_type", "target_nodes", "direction"],
            "additionalProperties": false,
            "description": "Indicates prerequisite concepts required for understanding the current concept."
          }
        },
        "required": ["has_subconcept", "is_prerequisite_of"],
        "additionalProperties": false
      }
    },
    "$defs" : {
      "target_node": {
        "type": "string",
        "description": "Name of end node that this concept has the relationship with."
      }
    },
    "required": [
      "node_type",
      "attributes",
      "relationships"
    ],
    "additionalProperties": false
  }
}
</output>
</conversion_example>

Here is the input for you to convert:
<input>
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

## Relationships (Edges)

- **is_application_of** → *Concept*/*Theorem*/*Property* (the reverse of **has_application**)
  - Concepts, theorems, or properties that are applied in this example.
  - *Example*: "Bayes' Theorem"

- **involves** → *Concept*/*Theorem*/*Property* (the reverse of **involved_in_application**)
  - Concepts that are involved in the application.
  - *Example*: "Conditional Probability", "Prior Probability"

<ignore>
> LOG IN THE OTHER SIDE OF ALL FOLLOWING RELATIONSHIPS
- **has_exercise** → *Exercise* (the reverse of **is_exercise_for**)
  - Exercises derived from the application example.
  - *Example*: "Exercise 4.3.2"

## Information to be additionally Rendered When Student Zooms In on Node

For the sake of maintaining only one copy of any information, info related to other nodes would be presented with a reference link that only gets rendered out when the user zooms in to the node in the interface.
</ignore>

</input>


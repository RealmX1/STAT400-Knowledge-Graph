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

<example json schema>
{
  "name": "math_response",
  "strict": true,
  "schema": {
    "type": "object",
    "properties": {
      "steps": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "explanation": {
              "type": "string"
            },
            "output": {
              "type": "string"
            }
          },
          "required": [
            "explanation",
            "output"
          ],
          "additionalProperties": false
        }
      },
      "final_answer": {
        "type": "string"
      }
    },
    "additionalProperties": false,
    "required": [
      "steps",
      "final_answer"
    ]
  }
}
<example json schema>

<example successful conversion>
<input markdown>
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
</input markdown>

<output json schema>
{
  "name": "concept_node_schema",
  "strict": true,
  "schema": {
    "type": "object",
    "properties": {
      "attributes": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Uniform discrete distribution"
          },
          "aliases": {
            "type": [
              "array",
              "null"
            ],
            "items": {
              "type": "string"
            },
            "description": "Synonyms or alternative names for the concept"
          },
          "definition": {
            "type": "object",
            "properties": {
              "notation": {
                "type": "string",
                "description": "Symbols or mathematical notations associated with the concept in latex format"
              },
              "explanation": {
                "type": [
                  "array",
                  "null"
                ],
                "items": {
                  "type": "object",
                  "properties": {
                    "part": {
                      "type": "string"
                    },
                    "range": {
                      "type": [
                        "string",
                        "null"
                      ],
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
              },
              "description": {
                "type": "string",
                "description": "Additional explanations, background information, or context about the concept"
              }
            },
            "required": [
              "notation",
              "explanation",
              "description"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "aliases",
          "definition"
        ],
        "additionalProperties": false
      },
      "relationships": {
        "type": "object",
        "properties": {
          "related_to": {
            "type": [
              "object",
              "null"
            ],
            "properties": {
              "name": {
                "type": "string",
                "description": "Name of end node that this concept is related to."
              },
              "direction": {
                "type": "string",
                "enum": ["bidirectional"],
                "description": "Direction of the relationship."
              }
            },
            "required": ["name", "direction"],
            "additionalProperties": false,
            "description": "Most general (non-specific) relation type regarding other concepts."
          },
          "has_subconcept": {
            "type": [
              "object",
              "null"
            ],
            "properties": {
              "name": {
                "type": "string",
                "description": "Name of end node that is a subconcept derived from this concept."
              },
              "direction": {
                "type": "string",
                "enum": ["to"],
                "description": "Direction of the relationship."
              }
            },
            "required": ["name", "direction"],
            "additionalProperties": false,
            "description": "Points to more specific or narrower concepts derived from the current concept."
          },
          "is_prerequisite_of": {
            "type": [
              "object",
              "null"
            ],
            "properties": {
              "name": {
                "type": "string",
                "description": "Name of end node that require the current concept as a prerequisite."
              },
              "direction": {
                "type": "string",
                "enum": ["to"],
                "description": "Direction of the relationship."
              }
            },
            "required": ["name", "direction"],
            "additionalProperties": false,
            "description": "Indicates prerequisite concepts required for understanding the current concept."
          }
        },
        "required": ["related_to", "has_subconcept", "is_prerequisite_of"],
        "additionalProperties": false
      }
    },
    "required": [
      "attributes",
      "relationships"
    ],
    "additionalProperties": false
  }
}
</output json schema>
</example successful conversion>


Here is the markdown schema that you will convert to json schema:
<input markdown>
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



## Relationships (Edges)

- **involves_concept** ← *Concept* (the reverse of **involved_in_theorem**)
  - Concepts not part of hypothesis/assumption, but used in proof.
  - *Example*: Links to "Conditional Probability", "Marginal Probability"
### Inbound Relations/Prerequisites
- **depends_on** ← *Concept* (the reverse of **is_prerequisite_of**)
- **needs_property** ← *Property* (the reverse of **has_property**)
  - Properties that are necessary for the theorem which doesn't fit in any concept involved in the theorem.
  - *Example*: (?) may not be necessary. can't quite think of any examples yet.

- **uses_theorem** ← *Theorem* (the reverse of **used_to_prove**)
  - Other theorems referenced or utilized within the proof, but not as part of hypothesis/assumption.
  - *Example*: 
- **is_corollary_of** ← *Theorem* (the reverse of **is_basis_for**, more specific than **uses_theorem**)
  - Indicates if the theorem is a corollary derived from another theorem.
  - *Example*: "Bayes' Theorem" is a corollary of "conditional Probability"

### Outbound Relations/Results
- **concludes** → *List of Properties*/*Concepts* (the reverse of **derived_from(theorem)**)
  - Concepts that are derived from the theorem.
  - *Example*: "Negative Binomial Distribution"
</input markdown>
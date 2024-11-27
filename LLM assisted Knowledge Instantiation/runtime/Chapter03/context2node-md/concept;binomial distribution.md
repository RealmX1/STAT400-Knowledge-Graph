```markdown
# Binomial Distribution

## Attributes

- **Name**: Binomial Distribution
  - **Aliases**: None specified

- **Definition**:
  - **Notation**: $X \sim \text{Binomial}(n, p)$
    - **Explanation**:
      - $n$
        - Range: $n \in \mathbb{N}$
        - Description: Number of trials
      - $p$
        - Range: $p \in (0,1)$
        - Description: Probability of success in each trial

  - **Description**: 
    The Binomial distribution models the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success. It is commonly used in situations where the outcomes of interest are categorical, typically with binary outcomes such as success/failure or yes/no.

## Relationships

### Relation regarding concept
- **has_subconcept** → Bernoulli Distribution

- **is_prerequisite_of** → 
  - Geometric Distribution
  - Negative Binomial Distribution

- **related_to** → Discrete Distribution

### Relation regarding theorem
- **involved_in** → 
  - Binomial Experiment
  - Parameters associated to the Binomial Distribution

- **concludes_from** ←
  - Binomial Experiment

### Relation regarding exercise/application
- **involved_in** 
  - Application Example: "Suppose we sample n students (with replacement) from campus and check if their height is less than or equal to 60 inches..."

> Source: Stat400 teaching material - Jonathan Fernandez
```

In the case of a relevant node named "Discrete Distribution," a **related_to** relation is established to link "Binomial Distribution" within the broader realm of discrete distributions, which includes various subtypes.
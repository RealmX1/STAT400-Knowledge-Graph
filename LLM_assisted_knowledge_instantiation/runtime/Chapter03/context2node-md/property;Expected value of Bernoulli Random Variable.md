# Property Node

## Name

Expected value of Bernoulli Random Variable

## Aliases

- Mean of Bernoulli Random Variable
- Expected Value

## Definition

- **Notation**: 
  - Raw LaTeX: `E(\text{Bernoulli}(p)) = p`
  - Rendered: $E(\text{Bernoulli}(p)) = p$
- **Range**: 
  - Raw LaTeX: `E(\text{Bernoulli}(p)) \in [0, 1]`
  - Rendered: $E(\text{Bernoulli}(p)) \in [0, 1]$

## Description

The Expected Value of a Bernoulli Random Variable is simply the probability of success in a Bernoulli trial. It represents the average result of the random variable over a large number of trials. The expected value is the same as the parameter \( p \) of the Bernoulli distribution, reflecting the likelihood of success on each trial.

## Proof

Considering a Bernoulli random variable \( X \) with \( X \sim \text{Bernoulli}(p) \), the expected value is calculated as follows:

1. \( X \) takes the value 1 with probability \( p \) and value 0 with probability \( 1 - p \).
2. Therefore, the expected value \( E(X) \) can be calculated as:
   
   \[
   E(X) = 1 \cdot p + 0 \cdot (1-p) = p
   \]

> NEED TO mark SOURCE for the information used here. By default we will use `Stat400 teaching material - Jonathan Fernandez`

## Relationships

- **has_property** <= (i.e. **is_property_of** =>) *Concept*
  - Bernoulli Distribution
- **has_subconcept** <= (i.e. **is_subconcept_of** =>) *Concept*
  - Expected Value of Random Variable
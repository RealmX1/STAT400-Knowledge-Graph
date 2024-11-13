# Exercise Node Schema

## Attributes

- **Name**: wigets in a factory

- **Problem Statement**:
  Imagine you are working at a factory that produces widgets. In a batch of 50 widgets, 10 are defective, and 40 are not. You randomly select 5 widgets for a quality check. You are interested in finding the probability that exactly 2 of the 5 widgets you selected are defective.
  - **Notation**: PMF, probability

- **Solution**:

  Here:
  $
  \text{Population size } N = 50, \quad n = 5, \quad m = 10.
  $

  Based on the distribution of a Hypergeometric random variable,
  $
  p(x = 2) = \frac{\binom{10}{2} \binom{50 - 10}{5 - 2}}{\binom{50}{5}} = \frac{\binom{10}{2} \binom{40}{3}}{\binom{50}{5}} = 0.21.
  $

- **Difficulty Level**: 1/5

> From `Stat400 teaching material - Jonathan Fernandez`

## Relationships (Edges)

- **is_exercise_for** → *discrete_hypergeometric_concept*
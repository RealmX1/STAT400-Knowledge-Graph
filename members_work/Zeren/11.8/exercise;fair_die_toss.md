# Exercise Node Schema

## Attributes

- **Name**: coin toss example

- **Problem Statement**:
Find PMF of a fair six-sided die.
  - **Notation**: PMF

- **Solution**:
  Consider a fair six-sided die. When rolling the die, each side (1, 2, 3, 4, 5, and 6) has an equal probability of occurring. Since the die is fair, the probability of rolling any specific number is uniform. 

  The probability mass function for this uniform discrete distribution can be defined as:
  $
  P(X = x) = \frac{1}{6}, \quad \text{where } x \in \{1, 2, 3, 4, 5, 6\}.
  $

  In this example, each number from 1 to 6 is equally likely, so the distribution of outcomes follows a discrete uniform distribution.

- **Difficulty Level**: 1/5

> From `Stat400 teaching material - Jonathan Fernandez`

## Relationships (Edges)

- **is_exercise_for** → *uniform discrete distribution*
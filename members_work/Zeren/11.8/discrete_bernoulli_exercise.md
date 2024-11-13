# Exercise Node Schema

## Attributes

- **Name**: coin toss example

- **Problem Statement**:
  Let the outcome of the coin flip be denoted as a random variable $X$. If the coin lands on heads, let $X = 1$. If the coin lands on tails, let $X = 0$. Assume that the probability of landing on heads (success) is $p$, which could be, for instance, 0.5 for a fair coin. Compute PMF of $X$
  - **Notation**: PMF

- **Solution**:
  The probability mass function (PMF) of the Bernoulli distribution can be expressed as:
  $
  P(X = x) = 
  \begin{cases} 
  p & \text{if } x = 1 \\
  1 - p & \text{if } x = 0 
  \end{cases}
  $

- **Difficulty Level**: 1/5

> From `Stat400 teaching material - Jonathan Fernandez`

## Relationships (Edges)

- **is_exercise_for** → *discrete_bernoulli_concept*
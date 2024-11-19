# Exercise Node Schema

## Attributes

- **Name**: coin toss example

- **Problem Statement**:
  5 coins are tossed, each with a probability of heads of $\frac{1}{2}$. Assume outcomes are independent, find the PMF of the number of heads.
  - **Notation**: PMF

- **Solution**:
  Let $X$ denote the number of heads obtained. Then $X$ is a binomial random variable with parameter $(5, \frac{1}{2})$.

  $
  p(0) = \binom{5}{0} \left(\frac{1}{2}\right)^0 \left(\frac{1}{2}\right)^{5 - 0} = \frac{1}{32}
  $

  $
  p(1) = \binom{5}{1} \left(\frac{1}{2}\right)^1 \left(\frac{1}{2}\right)^{5 - 1} = \frac{5}{32}
  $

  $
  p(2) = \binom{5}{2} \left(\frac{1}{2}\right)^2 \left(\frac{1}{2}\right)^{5 - 2} = \frac{10}{32}
  $

  $
  p(3) = \binom{5}{3} \left(\frac{1}{2}\right)^3 \left(\frac{1}{2}\right)^{5 - 3} = \frac{10}{32}
  $

  $
  p(4) = \binom{5}{4} \left(\frac{1}{2}\right)^4 \left(\frac{1}{2}\right)^{5 - 4} = \frac{5}{32}
  $

  $
  p(5) = \binom{5}{5} \left(\frac{1}{2}\right)^5 \left(\frac{1}{2}\right)^{5 - 5} = \frac{1}{32}
  $

- **Difficulty Level**: 1/5

> From `Stat400 teaching material - Jonathan Fernandez`

## Relationships (Edges)

- **is_exercise_for** → *discrete_binomial_concept*
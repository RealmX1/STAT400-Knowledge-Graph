# Theorem Node Schema

## Attributes

- **Name**: Binomial-Bernoulli relationship


- **Statement**: A Bernoulli R.V $X \sim \text{Bernoulli}(p)$ is just a special case of Binomial R.V $Y \sim \text{Binomial}(n,p)$ with parameter (1,p).
  - **Axioms/Premises**: Condition: Given that $Y \sim \text{Binomial}(n,p)$ and if n=1,   

  - **Conclusion**: then, the Binomial distribution is reduced to Bernoulli distribution!

- **Description**: provides ways to simply binomial to bernoulli only if certain condition is met.

- **Proof**: 
  Given a binomial R.V $X \sim \text{Binomial}(n,p)$.let's see what happens when n=1:
  we know that the PMF of such a binomial random variable is given by
  $
  p(X = i) = \binom{n}{i} p^i (1 - p)^{n - i}, \quad i = 0, 1, \ldots, n.
  $ \
  if n=1, then 
  $
  p(X = 0) = \binom{1}{0} p^0 (1 - p)^{1 - 0} = 1-p,\quad i = 0
  $
  and 
  $
  p(X = 1) = \binom{1}{1} p^1 (1 - p)^{1 - 1} = p,\quad i = 1
  $,
  this is exactly PMF of a Bernoulli distribution with parameter 
  $p(X = 0) = 1-p$ and $p(X = 1)=p$

## Relationships (Edges)

### Outbound Relations/Results
- **concludes** → discrete_bernoulli_concept

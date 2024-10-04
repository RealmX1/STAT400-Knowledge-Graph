Chapter2:{Random Variables}
Section:{Discrete Random Variables}

## Properties (Attributes)

- **Name**: Discrete Random Variable

- **Aliases**: ["Discrete Variable", "Discrete Random Quantity"] ??

- **Definition**: 

  > A random variable $X: \mathcal{S} \longrightarrow \mathbb{R}$ is **discrete** if the cumulative distribution function of $X$, $F_X$, is a step function.
  
  *Source*: Stat400 teaching material - Jonathan Fernandez

- **Notation**:

  - **Random Variable**: `"X"` → $X$
> it might be a good idea to give have automated rendering of relevant notation from related nodes.
- **Relevant Notation**: rendered in real time
  - **Probability Mass Function**: `"p_X(x) = P(X = x)"` → $p_X(x) = P(X = x)$ where $X$ is the random variable, and $x$ represent value of one possible outcome of $X$.

  - **Cumulative Distribution Function**: `"F_X(x) = P(X \leq x)"` → $F_X(x) = P(X \leq x)$

  - **Expected Value**: `"E(X) = \sum_{x\in \mathcal{X}} x\; p_X(x)"` → $E(X) = \sum_{x\in \mathcal{X}} x\; p_X(x)$

  - **Variance**: `"V(X) = \sum_{x\in \mathcal{X}} (x - \mu_X)^2\; p_X(x)"` → $V(X) = \sum_{x\in \mathcal{X}} (x - \mu_X)^2\; p_X(x)$

> (not necessary here) need automation method for aligning usage of notation, especially when data come from different sources. Will be needed for automation pipeline for adding new exercise.

- **Alias Notation**:

  - NONE

- **Description**:

  A discrete random variable is a function that assigns numerical values to the outcomes of a random experiment, where these values are countable and distinct. The probability mass function (PMF) of a discrete random variable $X$ is defined as $p_X(x) = P(X = x)$, representing the probability that $X$ takes the value $x$. The cumulative distribution function (CDF) of $X$ is a step function, increasing only at points where $X$ has positive probability. Discrete random variables are fundamental in modeling scenarios where outcomes are discrete, such as counts of occurrences.

- **Tags/Categories**: ["Probability Theory", "Statistics", "Random Variables", "Discrete Distributions"]

- **Examples**:

  - **Binomial Distribution**: Counting the number of successes in a fixed number of independent Bernoulli trials.
  - **Poisson Distribution**: Modeling the number of events occurring in a fixed interval of time or space.
  - **Geometric Distribution**: Number of trials needed to achieve the first success in repeated independent Bernoulli trials.
  - **Hypergeometric Distribution**: Number of successes in a sequence of draws without replacement from a finite population.

## Relationships (Edges)

- **is_subconcept_of** → **Random Variable**

- **has_subconcept** → **Probability Mass Function**, **Expected Value of a Discrete Random Variable**, **Variance of a Discrete Random Variable**

- **related_to** → **Continuous Random Variable**, **Cumulative Distribution Function**

- **depends_on** → **Discrete Distribution**, **Set Theory** 

- **has_property** → **Expected Value**, **Variance**, **Probability Mass Function**, **Cumulative Distribution Function**

- **involves_in** → **Calculations of Expected Values**, **Variance Computations**, **Probability Distributions**
> add operation node type for calculation explanation.
- **has_application** → **Modeling Count Data**, **Number of Successes in Trials**, **Queueing Theory**, **Reliability Analysis**

---

*Note*: The probability mass function $p_X(x)$ is only non-zero at the specific values $\mathcal{X}$ that $X$ can take. The expected value and variance are key parameters for summarizing the distribution of a discrete random variable, calculated using the PMF.
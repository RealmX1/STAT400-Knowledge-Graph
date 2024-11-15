# Property Node Schema

## Attributes

- **Name**: 
  Expected Value and variance of discrete uniform Distribution

- **Definition**:
  Given
  $
  X \sim \text{Unif}(a,b).
  $
  Then, the set of values $X$ can take is finite or countably infinite, typically $\{a, a+1, \ldots, b\}$, where $a$ and $b$ are the minimum and maximum. And we have

  $
  \mathbb{E}[X]= \frac{a + b}{2}
  $

  $
  \text{Var}(X) = \frac{(b - a + 1)^2 - 1}{12}
  $

- **Proof**:

  Given
  $
  X \sim \text{Unif}(a,b)
  $
  where a and b are min and max of X respectively.

  Let $X$ takes $n$ equally likely values $x_1, x_2, \dots, x_n$ where $x_1=a$ and $x_n=b$. The mean or expected value of $X$, denoted $\mathbb{E}[X]$, is given by:
  $
  \mathbb{E}[X] = \sum_{i=1}^n x_i \cdot P(X = x_i)
  $
  Since $X$ is a discrete uniform random variable, each $x_i$ has equal probability $\frac{1}{n}$:
  $
  \mathbb{E}[X] = \sum_{i=1}^n x_i \cdot \frac{1}{n} = \frac{1}{n} \sum_{i=1}^n x_i
  $
  Thus, the mean of $X$ is:
  $
  \mathbb{E}[X] = \frac{1}{n} \sum_{i=1}^n x_i
  $
  If the values $x_1, x_2, \dots, x_n$ are sequential integers from $a$ to $b$, where $a = x_1$ and $b = x_n$, the mean can be simplified to:
  $
  \mathbb{E}[X] = \frac{a + b}{2}
  $
  Now, the variance of $X$, denoted $\text{Var}(X)$, is defined as:
  $
  \text{Var}(X) = \mathbb{E}\left[(X - \mathbb{E}[X])^2\right]
  $
  Expanding this, we get:
  $
  \text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2
  $

  Step 1: Compute $\mathbb{E}[X^2]$

  Since $X$ is discrete uniform, we have:
  $
  \mathbb{E}[X^2] = \sum_{i=1}^n x_i^2 \cdot P(X = x_i) = \frac{1}{n} \sum_{i=1}^n x_i^2
  $

  Step 2: Substitute $\mathbb{E}[X]$ and $\mathbb{E}[X^2]$ into the Variance Formula

  Therefore, the variance is:
  $
  \text{Var}(X) = \frac{1}{n} \sum_{i=1}^n x_i^2 - \left(\frac{1}{n} \sum_{i=1}^n x_i\right)^2
  $

  If $X$ takes equally spaced integer values from $a$ to $b$, then the variance simplifies to:
  $
  \text{Var}(X) = \frac{(b - a + 1)^2 - 1}{12}
  $

  which can also be written as:
  $
  \text{Var}(X) = \frac{(n^2 - 1)}{12}
  $
  when $n = b - a + 1$.

  From `Stat400 teaching material - Jonathan Fernandez`

  
## Relationships (Edges)

- **is_property_of** ← *Uniform Distribution*
- **is_child_concept_of** ← *Mean and variance of random variable*
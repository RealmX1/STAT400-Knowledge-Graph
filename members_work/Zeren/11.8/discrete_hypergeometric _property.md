# Property Node Schema

## Attributes

- **Name**:
  expectation and variance of hypergeometric Distribution

- **Definition**:
  given
  $
  X \sim \text{hypergeometric}(n,N,m)
  $
  where:
  $X$ is a random variable following the hypergeometric distribution. Letting $p=\frac{m}{N}$, then we will have

  $
  \mathbb{E}[X] = np
  $
  and
  $
  \text{Var}(X) = np(1 - p) \left(1 - \frac{n - 1}{N - 1}\right)
  $



- **Proof**: 

  For a hypergeometric R.V defined in discrete_hypergeometric_concept, we will have

  $
  \mathbb{E}[X^k] = \sum_{i=0}^n i^k \cdot \frac{\binom{m}{i} \binom{N - m}{n - i}}{\binom{N}{n}} \\
  =\sum_{1}^n i^{k-1} \cdot \frac{m \binom{m-1}{i-1} \binom{N - m}{n - i}}{\frac{N}{n} \binom{N-1}{n-1}} \quad \text{because} \quad \frac{\binom{N}{n}}{\binom{N-1}{n-1}}= \frac{N}{n}, \quad \frac{\binom{m}{i}}{\binom{m-1}{i-1}}= \frac{m}{i} \\
  =\frac{mn}{N} \sum_{1}^n i^{k-1} \cdot \frac{\binom{m-1}{i-1} \binom{N - m}{n - i}}{\binom{N-1}{n-1}} \\
  \text{let } i-1 = j \text{, then } j+1 = i\\
  =\frac{mn}{N} \sum_{j=0}^{n-1} (j+1)^{k-1} \cdot \frac{\binom{m-1}{j} \binom{N - m}{n-j-1}}{\binom{N-1}{n-1}}\\
  =\frac{mn}{N} \mathbb{E}[(Y+1)^{k-1}] \text{ , where}\\
  \text{Y is a hypergeometric R.V with parameters } (n-1, N-1, m-1)
  $
  Thus, \
  $
  \mathbb{E}[X] =\frac{mn}{N} \mathbb{E}[(Y+1)^{1-1}] = \frac{mn}{N} \mathbb{E}[(Y+1)^0] = \frac{mn}{N} = np
  $
  and \
  $
  \mathbb{E}[X^2] =\frac{mn}{N} \mathbb{E}[(Y+1)^1] = \frac{mn}{N} (\mathbb{E}[Y]+1) = \frac{mn}{N}(\frac{(m-1)(n-1)}{N-1}+1)
  $
  $
  \text{Var}(X) =\mathbb{E}[X^2]- \mathbb{E}^2[X]=\frac{mn}{N}(\frac{(m-1)(n-1)}{N-1}+1-\frac{mn}{N})\\
  \text{Now, letting } p=\frac{m}{N} \leftrightarrow m=Np\\
  \therefore \frac{m-1}{N-1}=\frac{Np-1}{N-1}=\frac{p(N-1)}{N-1} -\frac{1-p}{N-1}=P-\frac{1-p}{N-1}\\
  \therefore \text{Var}(X) =np[(n-1) p - (n-1) \frac{1-p}{N-1} + 1 - np]
  =np[\cancel{np} - p - \frac{(n-1) (1-p)}{N-1} + 1 \cancel{-np}]\\
  =np(1-p)(1-\frac{n-1}{N-1})
  $

  

## Relationships (Edges)

- **is_property_of** ← *hypergeometric Distribution*
- **is_child_concept_of** ← *mean and/or variance of random variable*
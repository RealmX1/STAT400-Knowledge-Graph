# Theorem Node Schema

## Attributes

- **Name**: Hypergeometric-Binomial relationship

- **Statement**: 
  - **Axioms/Premises**: Suppose that we have a hypergeometric R.V $
  X \sim \text{hypergeometric}(n,N,m)
  $ and a binomial R.V $Y \sim \text{binomial}(n,p=\frac{m}{N})$ and when m and N is large in relation to n,  

  - **Conclusion**:  then hypergeometric distribution can be approximated by Binomial distribution!

- **Description**: Given that we have a hypergeometric R.V $
  X \sim \text{hypergeometric}(n,N,m)
  $ and a binomial R.V $Y \sim \text{binomial}(n,p=\frac{m}{N})$
  From properties of hypergeometric distribution and binomial distribution,  
  $
  \mathbb{E}[X] = np
  $
  ,
  $
  \text{Var}(X) = np(1 - p) \left(1 - \frac{n - 1}{N - 1}\right)
  $ 
  and\
  $
  \mathbb{E}[Y] = np
  $
  ,
  $
  \text{Var}(Y) = np(1 - p)
  $
  Then, 
  $
  \mathbb{E}[X] = \mathbb{E}[Y] = np
  $
  under no conditions.\
  If now N is large, then 
  $(1-\frac{n-1}{N-1}) \approx 1$. Then, 
  $
  \text{Var}(X) = \text{Var}(Y)
  $\
  So, $\text{Var}(X)$ is approximately equals to what it would be if the selection is done with replacement. This is true, because of our intuition that if m and N are large in relation to n, it shouldn't make much difference if the selection is done with replacement or not. Simply put, it m, N are large, then PMF of hypergeometric distribution can be approximated by the binomial distribution!

- **Proof**: 
  Suppose that we have a hypergeometric R.V $
  X \sim \text{hypergeometric}(n,N,m)
  $ and a binomial R.V $Y \sim \text{binomial}(n,p=\frac{m}{N})$ and when m and N is large in relation to n,\
  $
  p(x = i) = \frac{\binom{m}{i} \binom{N - m}{n - i}}{\binom{N}{n}}, \quad i = 0, 1, \ldots, n. \\
  =\frac{m!}{(m - i)!i!} \cdot \frac{(N - m)!}{(N - m -n + i)!(n - i)!} \cdot \frac{(N - n)!n!}{N!}\\
  =\binom{n}{i} \cdot \frac{m!}{(m - i)!} \cdot \frac{(N - m)!}{(N - m - (n - i))!} \cdot \frac{(N - n)!}{N(N-1)\ldots(N-i+1)(N-i)!}  \text{ because } \binom{n}{i} = \frac{n!}{(n-i)! i!}\\
  \text{Now, because PMF of Binomial distribution is } \binom{n}{i} p^i (1-p)^{n-i} \text{, we have to group the above formula into "i terms" and "n-i terms". Since } \frac{m!}{(m-i)!} = m(m-1)\ldots(m-(i-1)) \text{ we have one "i term" here. Also we noticed another "i term" in } N(N-1)\ldots(N-i+1) = N(N-1)\ldots(N-(i-1)) \text{. Thus, }\\
  \therefore p(x = i) = \binom{n}{i} \cdot \frac{m(m-1)\ldots(m-(i-1))}{N(N-1)\ldots(N-(i-1))} \cdot \frac{(N - m)!}{(N - m - (n - i))!} \cdot \frac{(N - n)!}{(N-i)!}\\
  \text{Now since N,m are large in relation to n (so to i as well), N-m is greater than n-i, So } \frac{(N - m)!}{(N - m - (n - i))!} \text{ equals } (N-m)((N-m)-1)\ldots((N-m)-(n-i-1)) \text{ and this gives us one "n-i term".}\\
  \therefore p(x = i) = \binom{n}{i} \cdot \frac{m(m-1)\ldots(m-(i-1))}{N(N-1)\ldots(N-(i-1))} \cdot (N-m)((N-m)-1)\ldots((N-m)-(n-i-1)) \cdot \frac{(N - n)!}{(N-i)!}\\
  \text{We then only left with last term. Because i<=n, } (N-i)! \geq (N-n)! \text{ and } (N-i)! = (N-i)(N-(i+1))\ldots(N-(n-1))(N-n)! \text{so, } \frac{(N - n)!}{(N-i)!}=\frac{\cancel{(N-n)!}}{(N-i)(N-(i+1))\ldots(N-(n-1))\cancel{(N-n)!}} \text{ and this is another "n-i term". To wrap up,}\\
  \therefore p(x = i) = \binom{n}{i} \cdot \frac{m(m-1)\ldots(m-(i-1))}{N(N-1)\ldots(N-(i-1))} \cdot \frac{(N-m)((N-m)-1)\ldots((N-m)-(n-i-1))}{(N-i)(N-(i+1))\ldots(N-(n-1))}\\
  =\binom{n}{i} p^i (1-p)^{n-i} \text{ because by letting } p=\frac{m}{N} \text{ and m, N are large } \frac{m(m-1)\ldots(m-(i-1))}{N(N-1)\ldots(N-(i-1))} \approx (\frac{m}{N})^i = p^i \text{ and } (1-p)^{n-i}=(1-\frac{m}{N})^{n-i}=(\frac{N-m}{N})^{n-i} \approx \frac{(N-m)((N-m)-1)\ldots((N-m)-(n-i-1))}{(N-i)(N-(i+1))\ldots(N-(n-1))}
  $

## Relationships (Edges)

### Outbound Relations/Results
- **concludes** → discrete_binomial_concept

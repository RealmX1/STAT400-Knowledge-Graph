Notations used in the Textbook by Dr. Fernandez
Here are the distributions and their respective notations extracted from the text:

1. **Uniform Discrete Distribution**:  
   \( X \sim \text{Uniform}(N) \)  
   PMF:  
   \[
   p_X(x) = \frac{1}{N}, \quad \text{for } x \in \{1, 2, 3, \dots, N\}
   \]

2. **Bernoulli Distribution**:  
   \( X \sim \text{Bernoulli}(p) \)  
   PMF:  
   \[
   p_X(x) = 
   \begin{cases}
   1 - p & \text{if } x = 0 \\
   p & \text{if } x = 1
   \end{cases}
   \]  
   Alternatively:  
   \[
   p_X(x) = p^x(1-p)^{1-x}, \quad x \in \{0,1\}
   \]

3. **Binomial Distribution**:  
   \( X \sim \text{Binomial}(n, p) \)  
   PMF:  
   \[
   p_X(x) = {n \choose x} p^x (1 - p)^{n - x}, \quad x \in \{0, 1, 2, \dots, n\}
   \]

4. **Hypergeometric Distribution**:  
   \( X \sim \text{Hyper}(N, M, n) \)  
   PMF:  
   \[
   p_X(x) = \frac{{M \choose x}{N - M \choose n - x}}{{N \choose n}}, \quad x \in \{0, 1, 2, \dots, \min(n, M)\}
   \]

5. **Geometric Distribution**:  
   \( X \sim \text{Geom}(p) \)  
   PMF:  
   \[
   p_X(x) = (1 - p)^{x - 1} p, \quad x \in \{1, 2, 3, \dots\}
   \]

6. **Negative Binomial Distribution**:  
   \( X \sim \text{NegBinom}(r, p) \)  
   PMF:  
   \[
   p_X(x) = {x + r - 1 \choose x} (1 - p)^x p^r, \quad x \in \{0, 1, 2, \dots\}
   \]

7. **Poisson Distribution**:  
   \( X \sim \text{Pois}(\lambda) \)  
   PMF:  
   \[
   p_X(x) = e^{-\lambda} \frac{\lambda^x}{x!}, \quad x \in \{0, 1, 2, \dots\}
   \]

These notations describe the standard discrete probability distributions mentioned in the chapter.





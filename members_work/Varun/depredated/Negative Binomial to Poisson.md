### **Negative Binomial to Poisson**

#### **Name:**

* Conversion from Negative Binomial to Poisson Distribution  
* **Aliases**: None

#### **Hypotheses/Assumptions:**

* A negative binomial distribution models the number of failures before achieving *n* successes in a sequence of Bernoulli trials.  
* The Poisson distribution can be seen as the limiting case of the negative binomial distribution when the number of trials increases to infinity while keeping the mean constant.

#### **Statement:**

* The negative binomial distribution converges to the Poisson distribution as *n* (the number of successes) tends to infinity and the success probability *p* becomes small, such that the mean remains constant.

#### **Description:**

* **Negative Binomial Distribution**:  
  pX(x)=(x+n−1x)pn(1−p)xp\_X(x) \= {x \+ n \- 1 \\choose x} p^n (1 \- p)^xpX​(x)=(xx+n−1​)pn(1−p)x  
  where *x* is the number of failures before *n* successes, and *p* is the probability of success.  
* **Poisson Distribution**:  
  P(X=x)=λxe−λx\!P(X \= x) \= \\frac{\\lambda^x e^{-\\lambda}}{x\!}P(X=x)=x\!λxe−λ​  
  where *λ* is the expected number of events occurring in a fixed interval (mean of the distribution).  
* **Convergence**:  
  * If *n → ∞* and *p → 0* such that *np \= λ* (a constant), then the negative binomial distribution converges to the Poisson distribution with mean *λ*.

#### **Proof:**

1. Start with the PMF of the negative binomial distribution: pX(x)=(x+n−1x)pn(1−p)xp\_X(x) \= {x \+ n \- 1 \\choose x} p^n (1 \- p)^xpX​(x)=(xx+n−1​)pn(1−p)x  
2. Consider the limiting case where *n → ∞*, *p → 0*, and *np \= λ*.  
3. Use the binomial expansion and Stirling’s approximation for large *n* and small *p* to show that the limiting form of the negative binomial PMF becomes the Poisson PMF: P(X=x)=λxe−λx\!P(X \= x) \= \\frac{\\lambda^x e^{-\\lambda}}{x\!}P(X=x)=x\!λxe−λ​

#### **Tags/Categories:**

* Probability Theory  
* Distribution Convergence

### **Relationships (Edges)**

#### **Inbound Relations/Prerequisites:**

* **involves\_concept** ← *Negative Binomial Distribution*  
  * The negative binomial distribution models the number of failures before a certain number of successes in Bernoulli trials.  
* **involves\_concept** ← *Poisson Distribution*  
  * The Poisson distribution is used to model the number of events happening in a fixed interval with a known average rate.

#### **Outbound Relations/Results:**

* **concludes** → *Poisson Distribution*  
  * The Poisson distribution is derived as the limiting case of the negative binomial distribution when *n* tends to infinity and *p* tends to zero.

#### **is\_specialization\_of → *Negative Binomial Distribution***

* This theorem represents the Poisson distribution as a limiting form of the negative binomial distribution.

### **Other Relations**

#### **is\_generalization\_of:**

* The negative binomial distribution is a generalization of the Poisson distribution when considering finite *n* and non-zero *p*.

#### **has\_application:**

* The convergence between these distributions is useful in approximating the number of rare events over a large number of trials, such as modeling the occurrence of accidents or failures in systems with high redundancy.

This captures the relationship between the **negative binomial** and **Poisson** distributions, where the latter can be viewed as a limiting case of the former under certain conditions.


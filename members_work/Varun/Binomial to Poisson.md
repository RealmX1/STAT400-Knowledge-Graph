### **Binomial to Poisson**

#### **Name:**

* Conversion from Binomial to Poisson Distribution  
* **Aliases**: None

#### **Hypotheses/Assumptions:**

* The binomial distribution models the number of successes in a fixed number of independent Bernoulli trials.  
* The Poisson distribution is a limiting case of the binomial distribution when the number of trials is large, and the success probability is small, while keeping the expected number of successes constant.

#### **Statement:**

* The binomial distribution converges to the Poisson distribution as *n* (the number of trials) tends to infinity and the success probability *p* tends to zero, such that the expected number of successes *np \= λ* remains constant.

#### **Description:**

* **Binomial Distribution**:  
  P(X=k)=(nk)pk(1−p)n−kP(X \= k) \= {n \\choose k} p^k (1 \- p)^{n-k}P(X=k)=(kn​)pk(1−p)n−k  
  where *n* is the number of trials, *k* is the number of successes, and *p* is the probability of success in a single trial.  
* **Poisson Distribution**:  
  P(X=k)=λke−λk\!P(X \= k) \= \\frac{\\lambda^k e^{-\\lambda}}{k\!}P(X=k)=k\!λke−λ​  
  where *λ* is the expected number of successes (mean of the distribution).  
* **Convergence**:  
  * If *n → ∞* and *p → 0* such that *np \= λ* (a constant), then the binomial distribution converges to the Poisson distribution with mean *λ*.

#### **Proof:**

1. Start with the PMF of the binomial distribution: P(X=k)=(nk)pk(1−p)n−kP(X \= k) \= {n \\choose k} p^k (1 \- p)^{n-k}P(X=k)=(kn​)pk(1−p)n−k  
2. As *n* becomes large and *p* becomes small, use the approximation for binomial coefficients and exponential limits to show that the limiting form of the binomial PMF matches the Poisson PMF: P(X=k)=λke−λk\!P(X \= k) \= \\frac{\\lambda^k e^{-\\lambda}}{k\!}P(X=k)=k\!λke−λ​ where *λ \= np* remains constant in the limit.

#### **Tags/Categories:**

* Probability Theory  
* Distribution Convergence

### **Relationships (Edges)**

#### **Inbound Relations/Prerequisites:**

* **involves\_concept** ← *Binomial Distribution*  
  * The binomial distribution models the number of successes in a fixed number of Bernoulli trials with a constant probability of success.  
* **involves\_concept** ← *Poisson Distribution*  
  * The Poisson distribution is used to model the number of events happening in a fixed interval with a known average rate.

#### **Outbound Relations/Results:**

* **concludes** → *Poisson Distribution*  
  * The Poisson distribution is derived as the limiting case of the binomial distribution when *n* tends to infinity and *p* tends to zero.

#### **is\_specialization\_of → *Binomial Distribution***

* This theorem represents the Poisson distribution as a limiting form of the binomial distribution.

### **Other Relations**

#### **is\_generalization\_of:**

* The binomial distribution is a generalization of the Poisson distribution when considering a finite number of trials and non-zero probability of success.

#### **has\_application:**

* This relationship is commonly applied in situations where we are modeling the occurrence of rare events over a large number of trials, such as defects in a manufacturing process or arrivals at a queue in a fixed interval.

This captures the relationship between the **binomial** and **Poisson** distributions, where the Poisson can be viewed as an approximation of the binomial distribution when the number of trials is large and the probability of success is small.


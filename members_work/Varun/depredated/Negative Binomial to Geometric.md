### **Negative Binomial to Geometric**

#### **Name:**

* Conversion from Negative Binomial to Geometric Distribution  
* **Aliases**: None

#### **Hypotheses/Assumptions:**

* The negative binomial distribution models the number of failures before achieving *n* successes in a series of independent Bernoulli trials.  
* The geometric distribution is a special case of the negative binomial distribution when *n \= 1*, meaning it models the number of failures before the first success.

#### **Statement:**

* The geometric distribution is a special case of the negative binomial distribution when *n \= 1*, which models the number of failures before the first success in a series of Bernoulli trials.

#### **Description:**

* **Negative Binomial Distribution**:  
  P(X=x)=(x+n−1x)pn(1−p)xP(X \= x) \= {x \+ n \- 1 \\choose x} p^n (1 \- p)^xP(X=x)=(xx+n−1​)pn(1−p)x  
  where *x* is the number of failures before the *n*\-th success, *n* is the number of successes, and *p* is the probability of success in each trial.  
* **Geometric Distribution**:  
  P(X=x)=(1−p)xpP(X \= x) \= (1 \- p)^x pP(X=x)=(1−p)xp  
  where *x* is the number of failures before the first success and *p* is the probability of success.  
* **Special Case**:  
  * When *n \= 1*, the negative binomial distribution becomes the geometric distribution.

#### **Proof:**

1. Start with the PMF of the negative binomial distribution: P(X=x)=(x+n−1x)pn(1−p)xP(X \= x) \= {x \+ n \- 1 \\choose x} p^n (1 \- p)^xP(X=x)=(xx+n−1​)pn(1−p)x  
2. Set *n \= 1* to get: P(X=x)=(x+1−1x)p(1−p)x=p(1−p)xP(X \= x) \= {x \+ 1 \- 1 \\choose x} p (1 \- p)^x \= p (1 \- p)^xP(X=x)=(xx+1−1​)p(1−p)x=p(1−p)x  
3. This is exactly the PMF of the geometric distribution, proving that the geometric distribution is a special case of the negative binomial distribution when *n \= 1*.

#### **Tags/Categories:**

* Probability Theory  
* Distribution Specialization

### **Relationships (Edges)**

#### **Inbound Relations/Prerequisites:**

* **involves\_concept** ← *Negative Binomial Distribution*  
  * The negative binomial distribution models the number of failures before achieving *n* successes in Bernoulli trials.  
* **involves\_concept** ← *Geometric Distribution*  
  * The geometric distribution is used to model the number of failures before the first success.

#### **Outbound Relations/Results:**

* **concludes** → *Geometric Distribution*  
  * The geometric distribution is derived as a special case of the negative binomial distribution when *n \= 1*.

#### **is\_specialization\_of → *Negative Binomial Distribution***

* This theorem represents the geometric distribution as a special case of the negative binomial distribution.

### **Other Relations**

#### **is\_generalization\_of:**

* The negative binomial distribution is a generalization of the geometric distribution when the number of successes *n \> 1*.

#### **has\_application:**

* The geometric distribution is often applied in scenarios where we are interested in the number of failures before the first success, such as modeling waiting times or counting the number of attempts needed to achieve a certain event.

This captures the relationship between the **negative binomial** and **geometric** distributions, where the geometric distribution is a special case of the negative binomial distribution when only one success is required.


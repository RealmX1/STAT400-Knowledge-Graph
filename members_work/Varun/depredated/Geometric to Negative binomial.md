### **Geometric to Negative binomial**

#### **Name:**

* Conversion from Geometric to Negative Binomial Distribution  
* **Aliases**: None

#### **Hypotheses/Assumptions:**

* The geometric distribution models the number of failures before the first success in a series of Bernoulli trials.  
* The negative binomial distribution models the number of failures before achieving *n* successes in a series of Bernoulli trials.  
* Assume independent and identically distributed trials with success probability *p*.

#### **Statement:**

* The geometric distribution can be considered a special case of the negative binomial distribution when the number of successes *n \= 1*.

#### **Description:**

* **Geometric Distribution**: The probability mass function (PMF) of the geometric distribution is given by:  
  pX(x)=p(1−p)x−1p\_X(x) \= p (1 \- p)^{x \- 1}pX​(x)=p(1−p)x−1  
  where *x* is the number of failures before the first success and *p* is the probability of success.  
* **Negative Binomial Distribution**: The PMF of the negative binomial distribution is:  
  pX(x)=(x+n−1x)pn(1−p)xp\_X(x) \= {x \+ n \- 1 \\choose x} p^n (1 \- p)^xpX​(x)=(xx+n−1​)pn(1−p)x  
  where *n* is the number of successes and *x* is the number of failures before the *n*\-th success.

#### **Proof:**

1. Starting from the PMF of the negative binomial distribution, we set *n \= 1* to convert it into the geometric distribution: pX(x)=(x+1−1x)p1(1−p)x=p(1−p)xp\_X(x) \= {x \+ 1 \- 1 \\choose x} p^1 (1 \- p)^x \= p(1 \- p)^xpX​(x)=(xx+1−1​)p1(1−p)x=p(1−p)x  
2. This matches the form of the geometric distribution, thus proving that the geometric distribution is a special case of the negative binomial distribution with *n \= 1*.

#### **Tags/Categories:**

* Probability Theory  
* Distribution Relationships

#### **Inbound Relations/Prerequisites:**

* **involves\_concept** ← *Geometric Distribution*  
  * The geometric distribution is used to model the number of failures before the first success.  
* **involves\_concept** ← *Negative Binomial Distribution*  
  * The negative binomial distribution is a more general form that models the number of failures before achieving *n* successes.

#### **Outbound Relations/Results:**

* **concludes** → *Geometric Distribution* (The reverse relation)  
  * The geometric distribution is derived from the negative binomial distribution when *n \= 1*.

#### **is\_specialization\_of → *Negative Binomial Distribution***

* This theorem is a specific case derived from the negative binomial distribution.

### **Other Relations**

#### **is\_generalization\_of:**

* The negative binomial distribution is a generalization of the geometric distribution.

#### **has\_application:**

* This relationship is often used in modeling real-world problems where we count the number of failures before achieving a set number of successes, such as modeling waiting times or reliability testing.

This structure mirrors the relationships between distributions as shown in the image you provided, with the geometric and negative binomial distributions having a clear mathematical and conceptual link.


NODES:

**HYPERGEOMETRIC DISTRIBUTION:**

**Name:** Hypergeometric Distribution

**Definition:**   
Fix N, M, n ∈. Suppose we have population of size N with exactly M successes  
in it. Suppose an experiment involves choosing n objects from the population  
(without replacement). Given ω an outcome for this experiment, let  
X(ω) := number of successes in  ω.

**Notation:**   
 X ∼ Hyper(N, M, n) if X takes values X := {0, 1, 2, 3, . . . , min(n, M )}  
and the probability mass function of X is given as

p\_X(x) \= \\frac{\\binom{M}{x} \\binom{N \- M}{n \- x}}{\\binom{N}{n}}, x \\in \\{0, 1, 2, 3, \\ldots, \\min(n, M)\\}

**Aliases:**  
“Sampling without replacement distribution”

**Description:**  
When we are sampling from a population without replacement, the random variable that tracks the number of successes actually has the "Hypergeometric Distribution"

**Tags/Categories:**  
Discrete Distributions, Statistics

**Examples:**  
Fix $N,M,n\\in \\N$. Suppose we have population of size $N$ with exactly $M$ successes in it. Suppose an experiment involves choosing $n$ objects from the population (without replacement). Given $\\omega$ an outcome for this experiment, let  
$$X(\\omega) := \\text{number of successes in $\\omega$}$$, in this setting $X$ is said to have the H/ypergeometeric distribution.

**Relationships:**  
**Is\_subconcept\_of:**  
Discrete Probability Distributions

**Depends\_on:**  
Binomial Distribution, Sampling without replacement

**Has\_property:**  
Expected value: n \\cdot \\frac{M}{N}

Variance : \\frac{N \- n}{N \- 1} \\cdot n \\cdot \\frac{M}{N} \\cdot \\left(1 \- \\frac{M}{N}\\right)

**Related\_to:**  
Multivariate hypergeometric distribution, Binomial Distribution

**has\_application:**   
Inspection of defective orders, Identifying voters

**Geometric Distribution:**  
**Name:** Geometric Distribution

**Definition:**  
The geometric random variable models phenomena that involve ”waiting”.  
\[Geometric Distribution\] We say that X has the Geometric distribution with  
parameters  
• p ∈ (0, 1): P (Success), the probability of a success

**Notation:**  
X ∼ Geom(p) if X takes values X := {1, 2, 3, . . . , } \= N  
and the probability mass function of X is given as  
pX (x) \= px(1 − p)(x−1) x ∈ {0, 1, 2, 3, . . . , }

**Aliases:**  
“Furry Distribution”

**Description:**  
It models the number of trials needed to achieve the first success in a sequence of independent Bernoulli trials, where each trial has a constant probability of success

**Tags/Categories:**  
Discrete Distributions, Statistics

**Examples:**  
\\begin{enumerate}  
    \\item Suppose we sample students (with replacement) from campus until a student with height is less than or equal to 60inches is found.   
    \\\\  
    Since the sampling is with replacement, the result of a given trial is independent of the other trials. Therefore this experiment can be modelled by $X\\sim \\text{Geom}(p)$ distribution, where $$P(\\text{Success}) \= P(\\text{finding a student with height less than or equal to 60 inchex})$$   
    and  event  
    $$\\{X= k \\} := \\{\\text{we find $k$ students before the first student with height less than or equal to 60 inches}\\}$$  
    \\\\  
    In this setting, $p\_X(k) \= P(X=k)$, is probability of picking exactly $k$ students before finding a student with height less than or equal to 60inches.    
    \\\\  
    Also, $P(X \\ge k)$, picking more than or equal to $k$ students before finding a student with height less than or equal to 60inches.  
    \\item  Suppose we sample students (with replacement) from campus until we find one that has taken a statistics course.   
    \\\\  
    This experiment can be modelled by $X\\sim \\text{Geom}(p)$ distribution,   
    where  
    $$P(\\text{Success}) \= P(\\text{finding a student who has taken a statistics course})$$  
    and the event   
    $$\\{X= k \\} := \\{\\text{we pick $k$ students before finding the first student who has taken at least one statistics class}\\}$$  
    \\\\  
    In this setting, $p\_X(k) \= P(X=k)$,  is the probability of picking exactly $k$ students before finding a student who has taken at least one statistics class.   
      
    \\item  Suppose we choose potatoes (with replacement, even though that does not really make sense) until we find a potato that does not have a blemish.   
    \\\\  
      
    In this setting, a potato is a success if it does not have any blemishes.   
    \\\\  
    This experiment can be modelled by $X\\sim \\text{Geom}(p)$ distribution,   
    $$P(\\text{Success}) \= P(\\text{finding a potato without any blemishes})$$  
      
    and the event   
    $$\\{X=k\\} := \\{\\text{we pick $k$ potatoes before finding the first potato without any blemishes}\\}$$  
    \\\\  
    In this setting, $p\_X(k) \= P(X=k)$, is the probability of picking exactly $k$  potatoes before finding the first potato without any blemishes. 

**Relationships:**

**Is\_subconcept\_of:**  
Discrete Probability Distributions

**Depends\_on:**  
Binomial Distribution, Sampling without replacement, Bernoulli trials

**Properties:**

The expected value of X is given by:  
E(X) \= 1/p  
2\. The variance of X is given by:  
V (X) \= 1 − p/p^2

**Related\_to:**  
Binomial Distribution, Bernoulli distribution, Bernoulli trials

**has\_application:**   
Number of defects, Number of bankruptcies

**Negative Binomial Distribution:**

**Name:** Negative binomial distribution

**Definition:**  
The Negative Binomial random variable also models phenomena that involve  
”waiting”.  
\[Negative Binomial Distribution\] We say that X has the Negative Binomial  
distribution with parameters  
• r ∈ N : number of successes we are waiting for.  
• p ∈ (0, 1): P (Success), the probability of a success.

**Notation:**  
X ∼ NegBinom(r, p) if X takes values X := {0, 1, 2, 3, . . . , } \=  
N and the probability mass function of X is given as  
pX (x) \=x \+ r − 1Cx p^r (1 − p)^x                             x ∈ {0, 1, 2, 3, . . . , }

**Aliases:**  
Pascal Distribution

**Description**  
In [probability theory](https://en.wikipedia.org/wiki/Probability_theory) and [statistics](https://en.wikipedia.org/wiki/Statistics), the negative binomial distribution is a [discrete probability distribution](https://en.wikipedia.org/wiki/Discrete_probability_distribution) that models the number of failures in a sequence of independent and identically distributed [Bernoulli trials](https://en.wikipedia.org/wiki/Bernoulli_trial) before a specified (non-random) number of successes

**Tags/Categories:**  
Discrete Distributions, Statistics

**Examples**

\\begin{enumerate}  
    \\item Suppose we sample students (with replacement) from campus until we find $r$ students with height is less than or equal to 60inches is found.   
    \\\\  
    Since the sampling is with replacement, the result of a given trial is independent of the other trials. Therefore this experiment can be modelled by $X\\sim \\text{NegBinom}(r, p)$ distribution, where $$P(\\text{Success}) \= P(\\text{finding a student with height less than or equal to 60 inchex})$$   
    and  event  
    $$\\{X= k \\} := \\{\\text{we find $k$ students of height greater than 60inches before the finding the $r$th student with height less than or equal to 60 inches}\\}$$  
    \\\\  
    In this setting, $p\_X(k) \= P(X=k)$, is probability of finding exactly $k$ students with height greater than 60inches before finding the $r$th student with height less than or equal to 60inches.    
    \\\\  
    Also, $P(X \\ge k)$, finding more than or equal to $k$ students with height greater than 60inches before finding $r$th student with height less than or equal to 60inches.  
    \\item  Suppose we sample students (with replacement) from campus until we find $r$ students that have taken a statistics course.   
    \\\\  
    This experiment can be modelled by $X\\sim \\text{NegBinom}(r, p)$ distribution,   
    where  
    $$P(\\text{Success}) \= P(\\text{finding a student who has taken a statistics course})$$  
    and the event   
    $$\\{X= k \\} := \\{\\text{we find $k$ students who have never taken a statistics class before finding $r$th student who has taken at least one statistics class}\\}$$  
    \\\\  
    In this setting, $p\_X(k) \= P(X=k)$,  is the probability of finding exactly $k$ students who have never taken a statistics class before finding $r$th student who has taken at least one statistics class.   
      
    \\item  Suppose we choose potatoes (with replacement, even though that does not really make sense) until we find $r$ potatoes that do not have a blemish.   
    \\\\  
      
    In this setting, a potato is a success if it does not have any blemishes.   
    \\\\  
    This experiment can be modelled by $X\\sim \\text{NegBinom}(r, p)$ distribution,   
    $$P(\\text{Success}) \= P(\\text{finding a potato without any blemishes})$$  
      
    and the event   
    $$\\{X=k\\} := \\{\\text{find exactly $k$ potatoes with blemishes before finding the $r$th potato without any blemishes}\\}$$  
    \\\\  
    In this setting, $p\_X(k) \= P(X=k)$, is the probability of finding exactly $k$ potatoes with blemishes before finding the $r$th potato without any blemishes. 

**Relationships:**

**Is\_subconcept\_of:**  
Discrete Probability Distributions

**Properties:**  
The expected value of X is given by:  
E(X) \= r(1 − p)/p  
The variance of X is given by:  
V (X) \= r(1 − p)/p^2

**Depends\_on:**  
Binomial Distribution, Bernoulli trials

**Related\_to:**  
Binomial Distribution, Bernoulli distribution, Bernoulli trials

**Has\_application:**

Modeling the number of defaults on a loan before a certain number of payments are made  
Modelling the number of defects in a manufactured product before a certain number of units are produced


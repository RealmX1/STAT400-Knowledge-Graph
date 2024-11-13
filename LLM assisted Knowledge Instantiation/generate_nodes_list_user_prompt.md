

**Input:**
- **Node Type Descriptions:**  
  <node_types> 
    **There are 5 types of nodes - Concept Node, Property Node, Theorem Node, Exercise Node, and Application Example Node.**
    ## Node Types
    - **Concept Node** 
        - self-explanatory
        - Examples: 
        - "Poisson Distribution"
        - "Variance of Distribution"
        - "Random Variable
    - **Property Node** 
        - Property of a concept A that is instantiation of a concept node B.
        - Two types of properties: Essential and Accidental
        - The properties modeled in KG should all be essential properties. 
        - Essential properties are defining, unchanging, and necessary for a concept to be what it is. (or strictly derived from other essential properties)
            - E.g. Variance function of Poisson Distribution
        - Accidental properties are contextual, variable, and non-essential to the identity of the concept.
            - E.g. Variance value of an arbitrary Poisson Distribution (is accidental in context of the concept "Poisson Distribution")
        - Examples of what should be modeled as property node:
        - For the concept node "Poisson Distribution":
            - "Variance (function) of Poisson Distribution" is a property of concept "Poisson Distribution", and this property is an instantiation of concept "Variance of Distribution".
            - similarly, "Expected value of Poisson Distribution" is a property of concept "Poisson Distribution", and this property is an instantiation of concept "Expected value of Distribution".
            - "PMF of Poisson Distribution" is a property of concept "Poisson Distribution", and this property is an instantiation of concept "Probability Mass Function (PMF)".
            - similarly, "CDF of Poisson Distribution" is a property of concept "Poisson Distribution", and this property is an instantiation of concept "Cumulative Distribution Function (CDF)".
            - Note that the $\lambda$ in "Poisson Distribution" is a parameter, not a property. It is strictly owned by "Poisson Distribution" but it doesn't have a hiearchical relation with another concept node.
        - Note:
        - What distinguish "property of a node" and "child concept" is that, 
            - a child concept is only at the begining of a "is-a" relationship, it is a binary relationship (between parent concept and child concept)
            - e.g. "Poisson Distribution" is a child concept of "Discrete Distribution"
            - the property is both at the beginning of a "is-a" relation, and also at the end of a "has-a"/"is" relationship. it is a ternary relationship (between parent concept, owner concept, and property concept)
            - e.g. "Variance of Poisson Distribution" is a child concept of "Variance of Distribution", and at the same time owned by "Poisson Distribution" (strictly dependent on), thus it is a property of "Poisson Distribution".
    - **Theorem Node**:
        - Theorem consist of a statement and a proof. The statement can be decomposed into a list of axioms/premises and a conclusion.
        - Do not take what the text book mark as "theorem" as reference of generating theorem nodes.
    - **Exercise Node**:
        - self-explanatory
    - **Application Example Node**:
        - Instance of a concept/theorem/property that is applied in a real-world scenario.
  </node_types>  
  <context>
    \chapter[Discrete Random Variables]{Discrete Random Variable}
    In this chapter we will go over some standard examples of discrete random variables, some of these distributions are so important they have their own specific names. 
    \\

    Recall that $X$ is said to be a discrete random variables if the cumulative distribution function $F_X$ is a step function. This implies that the set of values of $X$, $\X$, will be a discrete subset of $\R$ (a set with no limit points).

    \section[Uniform Discrete Random Variable]{Uniform Discrete Random Variable}
    \begin{defn}
    The random variable $X$ has \textbf{uniform discrete distribution} with parameter $N\in \N$ if it is supported on

    $$\X:=\{1,2,3,\cdots,N\}$$
    and probability mass function of $X$ is given by:

    $$p_X(x)=P(X=x)=\frac{1}{N} \quad \quad \text{for all $x\in \X$}$$
    \end{defn}

    \begin{thm}[Parameters associated to the Uniform Distribution]
        Suppose $X$ has the Uniform distribution on $\{1, 2, 3, \dots, N\}$ then,
        \begin{enumerate}
            \item The expected value of $X$ is given by:
            $$E(X) = \frac{N+1}{2}$$
            \item The variance of $X$ is given by:
            $$V(X) = \frac{(N+1)(N-1)}{12}$$
        \end{enumerate}
    \end{thm}

    \section[Bernoulli Distribution]{Bernoulli Distribution}
    The Bernoulli distribution simulates a "trial" whose outcome is either a success or a failure. 

    \begin{defn}[Bernoulli Trial]
    An experiment is called a Bernoulli trial if it has exactly two outcomes, a success or a failure. 
    \end{defn}

    \begin{defn}[Bernoulli Distribution]
        We say that $X$ has the Bernoulli distribution with parameter $p\in (0,1)$, typically denoted by $X \sim \text{Bernoulli}(p)$ if $X$ takes values $\mathcal{X}:= \{0,1\}$ and the probability mass function of $X$ is given as
        $$p_X(x) = \begin{cases}
            1-p \quad \text{if $x=0$}\\
            p \quad \text{if $x=1$}
        \end{cases}$$
        The pmf can also be written as
        $$p_X(x) = p^x(1-p)^{(1-x)}\quad \quad x\in \{0,1\}$$
    \end{defn}

    Events associated to the Bernoulli distribution are of the form:
    \begin{enumerate}
        \item $\{X = 0\}$: the trial was a failure.
        \item $\{X =1\}$: the trial was a success. 
    \end{enumerate}


    \begin{thm}[Parameters associated to the Bernoulli Distribution]
        Suppose $X\sim \text{Bernoulli}(p)$ then,
        \begin{enumerate}
            \item The expected value of $X$ is given by:
            $$E(X) = p$$
            \item The variance of $X$ is given by:
            $$V(X) = p(1-p)$$
        \end{enumerate}
    \end{thm}

    Examples of Bernoulli distribution in applications:
    \begin{enumerate}
        \item Suppose we sample a random student from campus and check if the height of the student is less than or equal to 60inches. 
        \\
        This experiment can be modelled by $X\sim \text{Bernoulli}(p)$ distribution, where the event 
        $$\{X=1\} := \{\text{a randomly chosen student has height $\le 60$ inches}\}$$
        \\
        In this setting, $p_X(1) = P(X=1) = p$, is the proportion of students on campus whose height is less than or equal to 60inches. 
        \item  Suppose we sample a random student from campus and check if they have taken a statistics course. 
        \\
        This experiment can be modelled by $X\sim \text{Bernoulli}(p)$ distribution, where the event 
        $$\{X=1\} := \{\text{a randomly chosen student has taken a statistics course}\}$$
        \\
        In this setting, $p_X(0) = P(X=0) = (1-p)$, is the proportion of students on campus who have never taken a statistics class. 
        \item  Suppose we choose a potato at a supermarket, and we put it into our cart if it has no blemishes.  
        \\
        This experiment can be modelled by $X\sim \text{Bernoulli}(p)$ distribution, where the event 
        $$\{X=1\} := \{\text{a randomly chosen potato has no blemishes}\}$$
        \\
        In this setting, $p_X(1) = P(X=1) = p$, is the proportion of potatoes without blemishes in the supermarket aisle. 
    \end{enumerate}

    \section[Binomial Distribution]{Binomial Distribution}
    Suppose an experiment involves performing $n$ independent $\text{Bernoulli}(p)$ trials. An outcome for this experiment is a sequence of length $n$, with the $i$th entry in the sequence tracking if the $i$th trial was a success or a failure. In this setting, we might be interested in knowing the number of success in the outcome, and the Binomial random variable does exactly that. 
    \\

    \begin{defn}[Binomial Distribution]
        We say that $X$ has the Binomial distribution with parameters
        \begin{itemize}
            \item $n\in \mathbb{N}$ : the number of trials
            \item $p\in (0,1)$: $P(\text{Success})$, the probability of a success. 
        \end{itemize}
        typically denoted by $X \sim \text{Binomial}(n, p)$ if $X$ takes values $\mathcal{X}:= \{0,1, 2, 3, \dots, n\}$ and the probability mass function of $X$ is given as
        $$p_X(x) = {n \choose x} p^x(1-p)^{(n-x)}\quad \quad x\in \{0,1, 2, 3, \dots, n\}$$
    \end{defn}

    \begin{thm}[Binomial Experiment]
        Suppose $n\in \mathbb{N}$. The experiment involves performing $n$ independent $\text{Bernoulli}(p)$ trials. 
        \\
        Let $\omega$ be an outcome for this experiment, and $$X(\omega) := \text{number of successes in $\omega$}$$
        Then, 
        $$X \sim \text{Binomial}(n, p)$$
    \end{thm}
    \begin{proof}
    The proof involves explicitly calculating the pmf of $X$ and showing that it is the same as the pmf of the Binomial distribution with the given parameters. We leave this as an exercise for the reader. 
    \end{proof}


    Events associated to the Binomial distribution are of the form:
    \begin{enumerate}
        \item $\{X = k \}$: there are exactly $k$ successes in $n$ trials. 
        \item $\{a < X < b\}$: the number of successes in $n$ trials are greater  than $a$ but less than $b$.
        \item $\{a \le X\}$: there are more than $a$ successes in $n$ trials.
    \end{enumerate}


    \begin{thm}[Parameters associated to the Binomial Distribution]
        Suppose $X\sim \text{Binomial}(n, p)$ then,
        \begin{enumerate}
            \item The expected value of $X$ is given by:
            $$E(X) = np$$
            \item The variance of $X$ is given by:
            $$V(X) = np(1-p)$$
        \end{enumerate}
    \end{thm}
    Examples of Binomial distribution in applications:
    \begin{enumerate}
        \item Suppose we sample $n$ students (with replacement) from campus and check if their height of the chosen student is less than or equal to 60inches. 
        \\
        Since the sampling is with replacement, the result of a given trial is independent of the other trials. Therefore this experiment can be modelled by $X\sim \text{Binom}(n, p)$ distribution, where the event 
        $$\{X= k \} := \{\text{there are exactly $k$ students with height $\le 60$ inches among the $n$ chosen students}\}$$
        \\
        In this setting, $p_X(k) = P(X=k)$, is probability of finding exactly $k$ students with height $\le 60$ among $n$ randomly chosen students. 
        \\
        Also, $P(X \ge k)$, is probability of finding at least  $k$ students with height $\le 60$ among $n$ randomly chosen students. 
        \item  Suppose we sample $n$ students (with replacement) from campus and check if they have taken a statistics course. 
        \\
        This experiment can be modelled by $X\sim \text{Binom}(n, p)$ distribution, where the event 
        $$\{X=k\} := \{\text{there are exactly $k$ students who have taken a statistics class among the $n$ chosen students}\}$$
        \\
        In this setting, $p_X(k) = P(X=k)$, is the probability that of finding exactly $k$ students who have taken a statistics class among the $n$ chosen students. 
        
        \item  Suppose we choose $n$ potatoes (with replacement, even though that does not really make sense), a potato is a success if it does not have any blemishes. 
        \\
        This experiment can be modelled by $X\sim \text{Binom}(n, p)$ distribution, where the event 
        $$\{X=k\} := \{\text{there are exactly $k$ good potatoes among $n$ randomly chosen potatoes}\}$$
        \\
        In this setting, $p_X(k) = P(X=k)$, is the probability of finding exactly $k$ potatoes without blemishes among $n$ randomly chosen potatoes. 
    \end{enumerate}
    Note that we have be emphasizing that the sampling be with replacement, this ensures that trials are independent of each other.
    \\

    In many applications, where the population is large and $n$ is small (in comparison to the population), sampling without replacement can still result in "approximately" independent trials.
    \\

    When we are sampling from a population without replacement, the random variable that tracks the number of successes actually has the "Hypergeometric Distribution"

    \section{Hypergeometric Distribution}
    Fix $N,M,n\in \N$. Suppose we have population of size $N$ with exactly $M$ successes in it. Suppose an experiment involves choosing $n$ objects from the population (without replacement). Given $\omega$ an outcome for this experiment, let
    $$X(\omega) := \text{number of successes in $\omega$}$$, in this setting $X$ is said to have the H/ypergeometeric distribution.


    \begin{defn}[Hypergeometric Distribution]
        We say that $X$ has the Hypergeometric distribution with parameters
        \begin{itemize}
            \item $N\in \mathbb{N}$ : population size
            \item $M \in \mathbb{N}$: number of success in the population. 
            \item $n\in \mathbb{N}$: number individuals chosen from the population. 
        \end{itemize}
        typically denoted by $X \sim \text{Hyper}(N, M, n)$ if $X$ takes values $\mathcal{X}:= \{0,1, 2, 3, \dots, \min(n, M)\}$ and the probability mass function of $X$ is given as
        $$p_X(x) = \frac{{N \choose x} {N-M \choose n-x}}{{N \choose n}}\quad \quad x\in \{0,1, 2, 3, \dots, \min(n, M)\}$$
    \end{defn}

    \begin{thm}[Parameters associated to the Hypergeometric Distribution]
        Suppose $X\sim \text{Hyper}(N, M, n)$ then,
        \begin{enumerate}
            \item The expected value of $X$ is given by:
            $$E(X) = n \left(\frac{M}{N}\right)$$
            \item The variance of $X$ is given by:
            $$V(X) = \left(\frac{N-n}{N-1} \right)\cdot n\cdot \left(\frac{M}{N}\right)\cdot \left(1-\frac{M}{N} \right) $$
        \end{enumerate}
    \end{thm}

    \section{Geometric Distribution}
    The geometric random variable models phenomena that involve "waiting". 

    \begin{defn}[Geometric Distribution]
        We say that $X$ has the Geometric distribution with parameters
        \begin{itemize}
            \item $p\in (0,1)$: $P(\text{Success})$, the probability of a success. 
        \end{itemize}
        typically denoted by $X \sim \text{Geom}(p)$ if $X$ takes values $\mathcal{X}:= \{1, 2, 3, \dots, \} = \mathbb{N}$ and the probability mass function of $X$ is given as
        $$p_X(x) = p^x(1-p)^{(x-1)}\quad \quad x\in \{0,1, 2, 3, \dots, \}$$
    \end{defn}


    \begin{thm}[Geometric Experiment]
        The experiment involves performing independent $\text{Bernoulli}(p)$ trials until the first success is observed.  
        \\  
        Let $\omega$ be an outcome for this experiment, and $$X(\omega) := \text{number of trials in $\omega$}$$
        Then, 
        $$X \sim \text{Geom}(p)$$
    \end{thm}
    \begin{proof}
    We first observe that the sample space for this experiment looks like:
    $$ \mathcal{S} = \{S, FS, FFS, FFFS, FFFFS, \dots, \}$$
    From here, the proof involves explicitly calculating the pmf of $X$ and showing that it is the same as the pmf of the Geometric distribution with parameter $p$. We leave this as an exercise for the reader. 
    \end{proof}
    The above theorem shows that the Geometric distribution models phenomena that involve waiting for one success. 

    \begin{thm}[Parameters associated to the Geometric Distribution]
        Suppose $X\sim \text{Geom}(p)$ then,
        \begin{enumerate}
            \item The expected value of $X$ is given by:
            $$E(X) = \frac{1}{p}$$
            \item The variance of $X$ is given by:
            $$V(X) = \frac{1-p}{p^2}$$
        \end{enumerate}
    \end{thm}
    Examples of Geometric distribution in applications:
    \begin{enumerate}
        \item Suppose we sample students (with replacement) from campus until a student with height is less than or equal to 60inches is found. 
        \\
        Since the sampling is with replacement, the result of a given trial is independent of the other trials. Therefore this experiment can be modelled by $X\sim \text{Geom}(p)$ distribution, where $$P(\text{Success}) = P(\text{finding a student with height less than or equal to 60 inchex})$$ 
        and  event
        $$\{X= k \} := \{\text{we find $k$ students before the first student with height less than or equal to 60 inches}\}$$
        \\
        In this setting, $p_X(k) = P(X=k)$, is probability of picking exactly $k$ students before finding a student with height less than or equal to 60inches.  
        \\
        Also, $P(X \ge k)$, picking more than or equal to $k$ students before finding a student with height less than or equal to 60inches.
        \item  Suppose we sample students (with replacement) from campus until we find one that has taken a statistics course. 
        \\
        This experiment can be modelled by $X\sim \text{Geom}(p)$ distribution, 
        where
        $$P(\text{Success}) = P(\text{finding a student who has taken a statistics course})$$
        and the event 
        $$\{X= k \} := \{\text{we pick $k$ students before finding the first student who has taken at least one statistics class}\}$$
        \\
        In this setting, $p_X(k) = P(X=k)$,  is the probability of picking exactly $k$ students before finding a student who has taken at least one statistics class. 
        
        \item  Suppose we choose potatoes (with replacement, even though that does not really make sense) until we find a potato that does not have a blemish. 
        \\
        
        In this setting, a potato is a success if it does not have any blemishes. 
        \\
        This experiment can be modelled by $X\sim \text{Geom}(p)$ distribution, 
        $$P(\text{Success}) = P(\text{finding a potato without any blemishes})$$
        
        and the event 
        $$\{X=k\} := \{\text{we pick $k$ potatoes before finding the first potato without any blemishes}\}$$
        \\
        In this setting, $p_X(k) = P(X=k)$, is the probability of picking exactly $k$  potatoes before finding the first potato without any blemishes. 
    \end{enumerate}


    \section{Negative Binomial Distribution}
    The Negative Binomial random variable also models phenomena that involve "waiting". 

    \begin{defn}[Negative Binomial Distribution]
        We say that $X$ has the Negative Binomial distribution with parameters
        \begin{itemize}
        \item $r \in \mathbb{N}$: number of successes we are waiting for.
            \item $p\in (0,1)$: $P(\text{Success})$, the probability of a success. 
        \end{itemize}
        typically denoted by $X \sim \text{NegBinom}(r, p)$ if $X$ takes values $\mathcal{X}:= \{0, 1, 2, 3, \dots, \} = \mathbb{N}$ and the probability mass function of $X$ is given as
        $$p_X(x) = {x+r-1 \choose x}p^r(1-p)^x\quad \quad x\in \{0,1, 2, 3, \dots, \}$$
    \end{defn}


    \begin{thm}[Negative Binomial Experiment]
        The experiment involves performing independent $\text{Bernoulli}(p)$ trials until $r$ successes are observed.  
        \\  
        Let $\omega$ be an outcome for this experiment, and $$X(\omega) := \text{number of failures in $\omega$}$$
        Then, 
        $$X \sim \text{NegBinom}(r, p)$$
    \end{thm}
    \begin{proof}
    We first observe that the sample space for this experiment is infinite, and looks like
    $$ \mathcal{S} = \{SS\dots S, FSS\dots S, SFS\dots S, \dots , \}$$

    The proof involves explicitly counting the outcomes in the sets 
    $$\{X = k\} = \{\text{exactly $k$ failures observed before the $r$th success}\}$$ 
    and using this to calculate the pmf of $X$, and showing that it is the same as the pmf of the Negative Binomial distribution with parameters $r$ and $p$. We leave this as an exercise for the reader. 
    \end{proof}
    The above theorem shows that the Negative Binomial distribution models phenomena that involve waiting for $r$ successes. 


    \begin{thm}[Parameters associated to the Negative Binomial Distribution]
        Suppose $X\sim \text{NegBinom}(r, p)$ then,
        \begin{enumerate}
            \item The expected value of $X$ is given by:
            $$E(X) = \frac{r(1-p)}{p}$$
            \item The variance of $X$ is given by:
            $$V(X) = \frac{r(1-p)}{p^2}$$
        \end{enumerate}
    \end{thm}


    Examples of Negative Binomial distribution in applications:
    \begin{enumerate}
        \item Suppose we sample students (with replacement) from campus until we find $r$ students with height is less than or equal to 60inches is found. 
        \\
        Since the sampling is with replacement, the result of a given trial is independent of the other trials. Therefore this experiment can be modelled by $X\sim \text{NegBinom}(r, p)$ distribution, where $$P(\text{Success}) = P(\text{finding a student with height less than or equal to 60 inchex})$$ 
        and  event
        $$\{X= k \} := \{\text{we find $k$ students of height greater than 60inches before the finding the $r$th student with height less than or equal to 60 inches}\}$$
        \\
        In this setting, $p_X(k) = P(X=k)$, is probability of finding exactly $k$ students with height greater than 60inches before finding the $r$th student with height less than or equal to 60inches.  
        \\
        Also, $P(X \ge k)$, finding more than or equal to $k$ students with height greater than 60inches before finding $r$th student with height less than or equal to 60inches.
        \item  Suppose we sample students (with replacement) from campus until we find $r$ students that have taken a statistics course. 
        \\
        This experiment can be modelled by $X\sim \text{NegBinom}(r, p)$ distribution, 
        where
        $$P(\text{Success}) = P(\text{finding a student who has taken a statistics course})$$
        and the event 
        $$\{X= k \} := \{\text{we find $k$ students who have never taken a statistics class before finding $r$th student who has taken at least one statistics class}\}$$
        \\
        In this setting, $p_X(k) = P(X=k)$,  is the probability of finding exactly $k$ students who have never taken a statistics class before finding $r$th student who has taken at least one statistics class. 
        
        \item  Suppose we choose potatoes (with replacement, even though that does not really make sense) until we find $r$ potatoes that do not have a blemish. 
        \\
        
        In this setting, a potato is a success if it does not have any blemishes. 
        \\
        This experiment can be modelled by $X\sim \text{NegBinom}(r, p)$ distribution, 
        $$P(\text{Success}) = P(\text{finding a potato without any blemishes})$$
        
        and the event 
        $$\{X=k\} := \{\text{find exactly $k$ potatoes with blemishes before finding the $r$th potato without any blemishes}\}$$
        \\
        In this setting, $p_X(k) = P(X=k)$, is the probability of finding exactly $k$ potatoes with blemishes before finding the $r$th potato without any blemishes. 
    \end{enumerate}


    \section{Poisson Distribution}
    The Poisson is distribution is a very useful distribution that shows up in many applications, especially in the context of Poisson Processes. 

    \begin{defn}[Poisson Distribution]
        We say that $X$ has the Poisson  distribution with parameters
        \begin{itemize}
        \item $\lambda \in \mathbb{R}_{+}$: rate parameter
        \end{itemize}
        typically denoted by $X \sim \text{Pois}(\lambda)$ if $X$ takes values $\mathcal{X}:= \{0, 1, 2, 3, \dots, \} = \mathbb{N}$ and the probability mass function of $X$ is given as
        $$p_X(x) = e^{-\lambda} \frac{\lambda^k}{k!}$$
    \end{defn}

    To show that $p_X$ is indeed a pmf, we observe the series expansion 
    $$e^{\lambda}= \sum_{k=0}^\infty \frac{\lambda^k}{k!}$$

    \begin{thm}[Parameters associated to the Poisson Distribution]
        Suppose $X\sim \text{Pois}(\lambda)$ then,
        \begin{enumerate}
            \item The expected value of $X$ is given by:
            $$E(X) = \lambda$$
            \item The variance of $X$ is given by:
            $$V(X) = \lambda$$
        \end{enumerate}
    \end{thm}



    \section[Relationships Between Discrete Distributions]{Relationships Between Discrete Distributions}
    \subsection[Binomial and Hypergeometric]{Binomial and Hypergeometric}
    Let $N,M,n\in \N$ be given and set $p=\frac{M}{N}$. Suppose,
    \begin{enumerate}[itemsep=0pt, topsep=1pt, partopsep=0pt,label=(\alph*)]
    \item bin$(x;n,p)$ is the probability mas function for binomial distribution with parameters: \begin{align*}
    n&=\text{ sample size}\\
    p&=\text{ probability of success}
    \end{align*}
    \item hyper$(x;N,M,n)$ is the probability mass function for hypergeometric distribution with parameters\begin{align*}
    n&=\text{ sample size}\\
    M&=\text{number of successes}\\
    N&=\text{population size}
    \end{align*}
    Then, if $N,M\to \infty$, and $\frac{M}{N}\to p$, then hyper$(x;N,M,n)\to$bin$(x;n,p)$. 
    \\

    An alternate way to state this is to say that if sample size N is small compared to population size $N$, we can assume that samples are approximately independent.
    \end{enumerate}
    \subsection[Binomial and Poisson]{Binomial and Poisson}
    Suppose \begin{enumerate}[itemsep=0pt, topsep=1pt, partopsep=0pt,label=(\alph*)]
    \item bin$(x;n,p)$ is the probability mas function for binomial Distribution with parameters: \begin{align*}
    n&=\text{ sample size}\\
    p&=\text{ probability of success}
    \end{align*}
    \item pois$(x;\lambda)$ is the probability mass function for Poisson Distribution with parameters $\lambda>-$
    \end{enumerate}
    Then, if $n\to \infty$ and $p\to 0$ such that $n\cdot p\to \lambda$, then then bin$(x;N,M,n)\to$ pois$(x;n,p)$. 
    \\

    If $n$ is large and $p$ is small, bin$(x;N,M,n)\approx$ pois$(x;n,p)$, this is sometimes stated by saying that the Poisson Distribution is approximately the Binomial Distribution for rare events.
  </context>  
- **Existing `node_name:node_type` Pairs in the Graph:**  
  <existing_nodes> 
  None
  </existing_nodes>
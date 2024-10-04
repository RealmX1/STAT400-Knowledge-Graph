# Table of Contents

## Probability

### Sets, Experiment, and Probability

- Definition: [Experiment]

- Definition: [Sample Space]

- Definition: [Event]

- General description: To say that \textbf{an event $E$ has happened} means "we performed the experiment, and the outcome of this experiment was in the set $E$".

- Definition: [Simple Event]

- Example: Experiments involving coin tosses:

- Example: Experiments involving die rolls:

- Example: Consider the following two step experiment: In step 1, we toss a coin; In step 2, we roll a 6-sided die. All possible outcomes are contained in the set

- Example: We can perform an experiment where we pick a random student from campus, and ask if they have walked more than 3000 steps today. All possible outcomes of this experiment are contained in the set $\{``\text{Yes}",\,``\text{No}"\}$.

- Example: We can perform an experiment where we pick a student from campus and measure their height. All possible outcomes are contained in the set of positive real numbers, that is $(0, \infty)$.

- General description: Our goal is to assign probabilities or chance to events $E$ corresponding to an experiment. Since events and sample spaces are described as sets and subsets, we will first need to remind ourselves of how to work with these mathematical objects.

### Set Theory

- General description: We will need to understand some basics of sets and set operations. We define the operations along with the visual of the the operation using Venn Diagrams.

- Definition: [Empty Set]

- General description: Let $A,B$ be two sets.\\

- Definition: [Containment/Subset]

- Definition: [Equality]

- Definition: [Complement]

- Definition: [Union]

- Definition: [Intersection]

- Definition: [Difference]

- Definition: [Disjoint Sets/Mutually Exclusive]

- General description: We will often have to work with an infinite collection of sets, to do so, we will first need to label the sets using an "indexing set". Given a set $\Gamma$, a collection of sets indexed by $\Gamma$ will be denoted by $\{A_\alpha\}_{\alpha\in \Gamma}$. 

- Definition: [Pairwise Disjoint Collection]

- Definition: [Partition]

- Definition: [Countable Union/Intersection]

#### Axioms of Probability

- General description: Let $\mathcal{S}$ be the sample space of an experiment and let $E\subset \mathcal{S}$ be and event. We are interested in assigning a number to $E$ that quantifies the chance/probability that $E$ occurs. We will denote the probability of $E$ as $P(E)$.

- Definition: [Sigma Algebra]

- General description: Note that there are multiple sigma algebras that can be associated to a sample space. The trivial sigma algebra is $\{\emptyset, \mathcal{S}\}$ - the smallest possible sigma algebra. The power set $\mathcal{P}(\mathcal{S})$ of $\mathcal{S}$ also satisfies the axioms to be a sigma algebra, and this is the largest possible sigma algebra associated to $\mathcal{S}$. All other sigma algebra are somewhere in between these two extreme examples. We can use sub-setting as a natural way to define a partial order on all possible sigma algebras. 

- Definition: [Probability Function]

- Theorem: [Properties of a Probability Function]

- General description: Defining a probability function can often times be a tedious task, as the number of conditions needed to be checked grow exponentially (as a function of the sigma algebra). 

- Theorem: Suppose the sample space of an experiment is countable, listed as, $\mathcal{S} = \{s_i\}_{i\in \mathbb{N}} = \{s_1, s_2, s_3, \dots, \}$. Let $\mathcal{B}:=\mathcal{P}(\mathcal{S})$ be the powerset of $\mathcal{S}$. 

- General description: Using the theorem above, we can assign probability functions experiments with countable sample space, by assigning probabilities just to the simple events.

- Example: Consider the experiment consisting of tossing a coin two times. The sample space is $S = \{HH, HT, TH, TT\}$. Take the largest possible sigma algebra, that is the power set of $S$, denoted as $\mathcal{P}(S)$, which contains $|\mathcal{P}(S)| = 2^4 = 16$ elements. In this experiment, if the coin is a fair coin, we can assign the following probability function $P: \mathcal{P}(S)\to \R$:

### Conditional Probability and Independence

- General description: If the probability function attached to an experiments must be useful (say to draw some conclusions about events associated to the experiment), we will need to incorporate the features of the experiment as in our pursuit to calculate probability functions.

- Definition: [Conditional Event]

- General description: Given two events $E$ and $F$ we can consider the following events:

- Definition: [Multiplication Principle]

- General description: The term $P(F\mid E)$ is called the conditional probability of the event "F given E", in fact we use the multiplication principle to formally define conditional proability

- Definition: [Conditional Probability]

- General description: The multiplication principle informs us that the probability of the simultaneous occurrence of event $E$ and event $F$, that is $P(E\cap F)$, depends not only on information about the individual occurrence (with no additional information about the other event) of $E$ (that is $P(E)$) and $F$ (that is $P(F)$), \textbf{but} also the interaction/influence of how the event $E$ affects the occurrence of event $F$ (given by the conditional probability $P(F \mid E)$) or how the event $F$ affects the occurrence of event $E$ (given by the conditional probability $P(E \mid F)$).

- Definition: [Independent Events]

- General description: Observe that, $P(E \mid F) = E(E)$, tells us that the fact that $F$ happened did not affect the probability of $E$ happening. 

- Example: We revisit the experiment where we want to assign probabilities to the simple events associated to tossing a coin two times. 

### Bayes' Theorem

- General description: We are now ready to state the general theorems

- Theorem: [Law of Total Probability]

- General description: The last equation in the theorem is just the application of the multiplication principle.

- Theorem: [Bayes' Theorem]

- Proof: Using the fact that $\{A_1, A_2, \dots, A_k\}$ is a partition and the law of total probability we have:

- Example: %% Choosing a coin and tossing it two times

- Example: Suppose we now randomly choose a coin from the bag containing a fair coin and a two headed coin, and toss it two times independently. 

- Example: [Disease Testing]

### Probability and Counting

- General description: Suppose we are in the setting where the sample space $\mathcal{S}$ satisfies the following two conditions:

- Theorem: [Fundamental Theorem of Counting]

- Proof: We prove this theorem using the principle of mathematical induction applied to the number of tasks. We can structure the task $T$ as a tree, with level $i$ in the tree corresponding to the $i$th task $T_i$.

- Example: Add examples of counting.

#### Choosing from $n$ distinct objects

- General description: We will often want to count the number of ways of selecting $k$ objects from a set of $n$ distinct objects.

- Example: Suppose we want to count the total number of ways one can choose 4 digits from the set of 10 digits $\{0,1,2,3,4,5,6,7,8,9\}$.

- General description: \begin{center}

- Example: We set $n=10,k=3,$ where $S=\{0,1,2,3,4,5,6,7,8,9\}$.\\

- General description: The \textbf{number of possible arrangement of size k from n objects}

- Example: Consider choosing $3$ digits from the set $\{1,2,3,4,5\}$. 

## Random Variables

### Random Variables: Examples and Definitions

- General description: In practical applications we are typically interested in numerical features associated to an outcome of an experiment.

- Example: Suppose we toss a two sided coin three times. The sample space of this experiment is given by: 

- Example: Suppose we randomly sample a student from the campus. The sample space for this experiment is given by:

- General description: These questions provide answers to very specific numeric/quantitative features of the student.

- Definition: [Random Variable]

- General description: Intuitively, a random variable measures a specific quantitative feature of the sample space outcome. Here is a schematic to consider: 

- Definition: [Events Associated to a Random Variable]

- Example: Suppose the sample space $\mathcal{S}$ is all students on campus.

- General description: %%%%%%%%%%%%%%%%%%%% Example: toss a coin three times %%%%%%%%%%%%%%%%

- Example: Suppose we toss a coin three times, and we want to know if the first toss was a head?

- Example: Suppose we tossed a coin three times, and we were interested in counting the number of heads in three tosses. We can work through this as follows:

- General description: %%%%%%%%%%%%%%%%%%%%%%%%% end of example %%%%%%%%%%%%%%

- Definition: [Cumulative Distribution Function]

- General description: %%%%% Example: Toss a coin once

- Example: Suppose we toss a coin with $P(H) = p \in (0,1)$ once. Let $X$ be the random variable that tracks the outcome of the coint toss, that is 

- Example: Suppose we toss a fair coin ($P(H) = \frac{1}{2}$) three times, and let 

- General description: It is possible to classify all functions that can arise as cumulative distribution functions of random variable as follows:

- Theorem: [Classification of CDFs]

### Discrete Random Variables

- Definition: [Discrete Random Variable]

- Definition: [Probability Mass Function]

- General description: It is easy to observe that the only points where $p_X$ can be non-zero are the values, $\mathcal{X}$, that $X$ can take.

- Definition: [Parameters for Discrete Variables]

### Continuous Random Variables

- Definition: [Continuous Random Variable]

- Definition: [Probability Density Function]

- Definition: [Parameters for Continuous Variables]

- Definition: [Identically Distributed Random Variables]

- Example: Suppose we toss a fair coin five times, and $X$ tracks the number of heads in five tosses, and $Y$ tracks the number of tails in five tosses. Then, it is possible to show that even though $X$ and $Y$ are not equal as functions on the sample space, the cdfs $F_X$ and $F_Y$ are exactly the same. As a result $X$ and $Y$ will be identically distributed. 

## Discrete Random Variable

### Uniform Discrete Random Variable

- Definition: The random variable $X$ has \textbf{uniform discrete distribution} with parameter $N\in \N$ if it is supported on

- Theorem: [Parameters associated to the Uniform Distribution]

### Bernoulli Distribution

- General description: The Bernoulli distribution simulates a "trial" whose outcome is either a success or a failure.

- Definition: [Bernoulli Trial]

- Definition: [Bernoulli Distribution]

- General description: Events associated to the Bernoulli distribution are of the form:

- Theorem: [Parameters associated to the Bernoulli Distribution]

- General description: Examples of Bernoulli distribution in applications:

### Binomial Distribution

- General description: Suppose an experiment involves performing $n$ independent $\text{Bernoulli}(p)$ trials. An outcome for this experiment is a sequence of length $n$, with the $i$th entry in the sequence tracking if the $i$th trial was a success or a failure. In this setting, we might be interested in knowing the number of success in the outcome, and the Binomial random variable does exactly that. 

- Definition: [Binomial Distribution]

- Theorem: [Binomial Experiment]

- Proof: The proof involves explicitly calculating the pmf of $X$ and showing that it is the same as the pmf of the Binomial distribution with the given parameters. We leave this as an exercise for the reader.

- General description: Events associated to the Binomial distribution are of the form:

- Theorem: [Parameters associated to the Binomial Distribution]

- General description: Examples of Binomial distribution in applications:

### Hypergeometric Distribution

- General description: Fix $N,M,n\in \N$. Suppose we have population of size $N$ with exactly $M$ successes in it. Suppose an experiment involves choosing $n$ objects from the population (without replacement). Given $\omega$ an outcome for this experiment, let

- Definition: [Hypergeometric Distribution]

- Theorem: [Parameters associated to the Hypergeometric Distribution]

### Geometric Distribution

- General description: The geometric random variable models phenomena that involve "waiting".

- Definition: [Geometric Distribution]

- Theorem: [Geometric Experiment]

- Proof: We first observe that the sample space for this experiment looks like:

- General description: The above theorem shows that the Geometric distribution models phenomena that involve waiting for one success.

- Theorem: [Parameters associated to the Geometric Distribution]

- General description: Examples of Geometric distribution in applications:

### Negative Binomial Distribution

- General description: The Negative Binomial random variable also models phenomena that involve "waiting".

- Definition: [Negative Binomial Distribution]

- Theorem: [Negative Binomial Experiment]

- Proof: We first observe that the sample space for this experiment is infinite, and looks like

- General description: The above theorem shows that the Negative Binomial distribution models phenomena that involve waiting for $r$ successes.

- Theorem: [Parameters associated to the Negative Binomial Distribution]

- General description: Examples of Negative Binomial distribution in applications:

### Poisson Distribution

- General description: The Poisson is distribution is a very useful distribution that shows up in many applications, especially in the context of Poisson Processes.

- Definition: [Poisson Distribution]

- General description: To show that $p_X$ is indeed a pmf, we observe the series expansion 

- Theorem: [Parameters associated to the Poisson Distribution]

### Relationships Between Discrete Distributions

#### Binomial and Hypergeometric

- General description: Let $N,M,n\in \N$ be given and set $p=\frac{M}{N}$. Suppose,

#### Binomial and Poisson

- General description: Suppose \begin{enumerate}[itemsep=0pt, topsep=1pt, partopsep=0pt,label=(\alph*)]

## Point Estimation

### Introduction to Point Estimation

- General description: One goal of statistic is to draw insights/inference about certain aspects of the population using sample data. For example, we might want to estimate the following \begin{enumerate}

- Definition: Suppose \begin{align*}

- General description: \note \begin{enumerate}

- Definition: If $\widehat{\theta}$ is a point estimator for the population parameter $\theta$, then the relation of average value of $\widehat{\theta}$ and true value $\theta$, or \textbf{Bias of $\widehat{\theta}$} is \begin{align*}

- Definition: We say $\widehat{\theta}$ is an \textbf{unbiased estimator} for $\theta$ if \begin{align*}

- General description: \exercise Suppose we have estimators $\widehat{\theta_1},\widehat{\theta_2},\cdots,\widehat{\theta_k}$ estimating $\theta$. Among all the $\widehat{\theta_i},$ is there a notion of one estimator being better than theothers?

### Principle of Unbiased Estimation

- Example: Let population be $\{0,1\}$ and the population distribution be $\text{Bernolli}(p)$, i.e $P(X=1)=p$. Let $\{X_1,X_2,\cdots,X_n\}$ be a random sample. Recall that \begin{align*}

- Example: Suppose $\{X_1,X_2,\cdots,X_n\}$ is a random sample from a population with mean $\mu$ and variance $\sigma^2$. Then, we define the following: \begin{align*}

- Definition: Suppose $\widehat{\theta}$ is a statistic for a random sample $\{X_1,X_2,\cdots,X_n\}$ such that \begin{align*}

- Theorem: \textbf{Principle of Minimum Variance Unbiased Estimation:}\\

- Example: We know that $\widehat{\theta_1}=\overline{X}$ and $\widehat{\theta_2}=\overline{X}+X_1-X_n$ are both unbiased estimators of $\mu$\\

- Theorem: If $\{X_1,X_2,\cdots,X_n\}$ is a random sample from a normally distributed population, i.e N$(\mu,\sigma^2)$. Then the estimator $\overline{X}$ is the  Minimum Variance Unbiased Estimator for $\mu$.\\

- General description: \note \begin{enumerate}

### Methods of Point Estimation

- General description: Suppose Population has distribution $X$ and probability mass function or probability density function of $X$ is $f(x)$.\\

#### The Method of Moments

- General description: If there are $m$ parameters: $\theta_1,\theta_2,\theta_3,\cdots,\theta_m$ tand we want to estimate using $\{X_1,X_2,\cdots,X_n\}$. It is the same to get $m$-equations by equating the first $m$ population moments to the first $m$ sample moments and pray we can solve these equations to get estimators $\widehat{\theta_1},\widehat{\theta_2},\cdots \widehat{\theta_n}$ for $\theta_1,\theta_2,\cdots,\theta_m$ respectively.\\

- Example: \textbf{Sampling From Exponential Distribution}\\

- Example: \textbf{Sampling From Normal Distribution}\\

- Example: \textbf{Sampling From Gamma Distribution}\\

#### Maximum Likelihood Estimation

- Definition: Suppose $\{X_1,X_2,\cdots,X_n\}$, a random sample from population with probability density function/probability mass function $f(x)$.\\

- Theorem: \textbf{Properties of Maximum Likelihood Estimators}:\begin{enumerate}

- Example: \textbf{Sampling From Exponential Distribution}:\\

- Example: \textbf{Sampling From Normal Distribution}\\

## Statistical Inference

### Point estimators

- General description: Point estimators are an attempt at estimating a quantity of interest about the population. We have already seen this idea in play: the sample average is how we estimate the population mean (i.e the sample average is a point estimator for the population mean) and the sample variance is a point estimator for the population variance.

- Definition: Suppose that $\theta$ is a parameter. An \textit{estimator

- General description: for $\theta$, denoted by $\hat{\theta}$ (and $\hat{\theta}_n$ if we want to emphasize the sample size) is a statistic (i.e a function defined on the random sample).

- Example: \[

- General description: = \frac{X_1 + \ldots + X_n}{n}

#### Unbiasedness, Consistency and Mean Squared Error

- General description: We now turn our attention towards what makes a good (useful) estimator. There are several notions that are interrelated. We look at a couple below.

- Definition: The quantity

- General description: ) - \theta$

- Definition: The \textit{MVUE (minimum variance unbiased estimator)

- General description: tells us that When we have multiple unbiased estimators, we should pick the one with the lowest variance. 

### Constructing Estimators

- General description: So far we have discussed what makes a point estimator good. What we have not done is discuss how to construct a point estimator. In this section, we talk about how to construct point estimators that under certain technical conditions have good properties.\\

#### The method of moments

- General description: We start our discussion with the method of moments (abbreviated as \textbf{MM}). The method of moments relies on:

- Example: Suppose $X_1, \ldots, X_n$ is a random sample with $X_i \sim Ber(p)$. $p$ is a fixed but unknown number. Construct a point estimator $\hat{p

- General description: _{MM}$ using the method of moments.\\

- Example: Let $X_1, \ldots, X_n$ be a random sample with $X_i \sim \mathcal{N

- General description: (\mu,\sigma^2)$, where $\mu$ and $\sigma^2$ are fixed but unknown numbers. Construct point estimators $\hat{\mu}_{MM}$ and $\hat{\sigma}^2_{MM}$ for $\sigma^2$.\\

#### Maximum likelihood estimation

- General description: We now turn our attention to maximum likelihood estimation (abbreviated as \textbf{MLE}). The idea behind maximum likelihood estimators is to find an estimator $\hat{\theta}$ that maximizes the probability of the observed sample.

- Example: Let $X_1, \ldots, X_n$ be a random sample with $X_1 \sim Ber(p)$. We find the MLE for $p$.

- General description: \]

- Definition: The log-likelihood function $\ell(\underline{\theta

- General description: )$ is defined as $\ell(\underline{\theta}) = \ln \mathcal{L} (\underline{\theta})$.

- Example: Suppose that $X_1, \ldots, X_n$ is an (iid) random sample with $X_1 \sim \mathcal{N

- General description: (\mu, \sigma^2)$ where both $\mu, \sigma^2$ are fixed but unknown. Find the MLEs for $\mu, \sigma^2$.\\

- Example: Let $X_1, \ldots, X_n$ be a random sample with $X_1 \sim U[0,\theta]$ where $\theta > 0$ is fixed but unknown. Now

- General description: _{MM} = \frac{2}{n} \sum_{i=1}^n X_i\]

### A quick look back

- General description: Now that we have discussed point estimators, here are some important facts about how we approached the topics.

## Confidence Intervals

### Constructing Confidence Intervals

- General description: Let's start with an example to get an idea of what the process might look like.

- Example: Suppose that we have a random sample $X_1, \ldots, X_n$ with $X_1 \sim \mathcal{N

- General description: (\mu, \sigma^2)$. $\sigma^2$ is known, but $\mu$ is not known. We want to construct an interval $I(X_1, \ldots, X_n) = \left((a(X_1,\ldots, X_n), b(X_1, \ldots, X_n)\right)$ such that

- Example: Take $n=10$ and $\sigma^2=4$, i.e we have a random sample $X_1, \ldots, X_{10

- General description: $ where $X_i \sim \mathcal{N}(\mu,4)$. Recall again that $\mu$ is fixed, but unknown to us. 

#### Approximate Confidence Intervals

- General description: In the previous section we made two key assumptions.

- Definition: We say that $I(X_1, \ldots, X_n)$ is an $1-\alpha$ approximate confidence interval for $\theta$ if 

- General description: By setting


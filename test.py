import re

chapter_pattern = r'\\chapter(?:\[(.*?)\])?\{(.*?)\}'

section_content = r'''\chapter{Confidence Intervals}

In the previous chapter, we used a given sample $X_1, \ldots, X_n$ to construct estimates of various parameters of interest ($\overline{X}$ for $\mu$, $S^2$ for $\sigma^2$, etc.) In this chapter, we focus on using a sample to \textit{create intervals} that are likely to contain a parameter of interest.\\

\note It is the \textit{interval being constructed} that depends on the sample, \textbf{not the value of the parameter} (which while unknown to us is \textbf{fixed} and does not depend on the sample).

\defn{
A $1-\alpha$ confidence interval (abbreviated as \textbf{CI}) for a parameter $\theta$ is an interval 
\[
I(X_1, \ldots, X_n) = \left((a(X_1,\ldots, X_n), b(X_1, \ldots, X_n)\right)
\]
such that the equality 
\[
P(\theta \in I(X_1,\ldots, X_n)) = 1-\alpha
\]
holds for all possible values of $\theta$.
}
'''

subsections = re.split(chapter_pattern, section_content)
for subsection in subsections:
    print(f"'{subsection}'\n")

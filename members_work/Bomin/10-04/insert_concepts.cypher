// Uniform Discrete Distribution
MERGE (c:Concept {name: 'Uniform Discrete Distribution'})
SET c.aliases = ['Discrete Uniform Distribution']
SET c.definition = 'The Uniform Discrete Distribution is a probability distribution where a discrete random variable X takes on a finite number of equally spaced values, each with equal probability.'
SET c.notation_latex_code = 'X \\sim \\text{Uniform}(1, N)'
SET c.notation_rendered = 'X ∼ Uniform(1, N)'
SET c.pmf_latex_code = 'p_X(x) = \\frac{1}{N}, \\quad x \\in \\{1, 2, \\dots, N\\}'
SET c.pmf_rendered = 'p_X(x) = 1/N, x ∈ {1, 2, ..., N}'
SET c.description = 'A random variable X has a Uniform Discrete Distribution with parameter N ∈ ℕ if it is supported on X = {1, 2, 3, ..., N} and each outcome is equally likely. This implies that the probability mass function (PMF) is constant over its support.'
SET c.source = 'Stat400 teaching material - Jonathan Fernandez'
SET c.tags = ['Probability Theory', 'Statistics', 'Discrete Distribution', 'Uniform Distribution']

MERGE (ev:Property {name: 'Expected Value', formula: 'E(X) = (N + 1)/2'})
MERGE (var:Property {name: 'Variance', formula: 'V(X) = ((N + 1)(N - 1))/12'})

MERGE (c)-[:HAS_PROPERTY]->(ev)
MERGE (c)-[:HAS_PROPERTY]->(var)

MERGE (related:Concept {name: 'Continuous Uniform Distribution'})
MERGE (c)-[:RELATED_TO]->(related)

MERGE (theorem:Theorem {name: 'Parameters associated with the Uniform Distribution'})
MERGE (c)-[:INVOLVED_IN_THEOREM]->(theorem)


// Bernoulli Distribution
MERGE (c:Concept {name: 'Bernoulli Distribution'})
SET c.definition = 'The Bernoulli Distribution models a random experiment with exactly two outcomes: success (1) and failure (0).'
SET c.notation_latex_code = 'X \\sim \\text{Bernoulli}(p)'
SET c.notation_rendered = 'X ∼ Bernoulli(p)'
SET c.pmf_latex_code = 'p_X(x) = \\begin{cases} 1 - p & \\text{if } x = 0, \\\\ p & \\text{if } x = 1. \\end{cases}'
SET c.pmf_rendered = 'p_X(x) = { 1 - p if x = 0; p if x = 1 }'
SET c.description = 'A random variable X has the Bernoulli Distribution with parameter p ∈ (0, 1) if it represents the outcome of a single Bernoulli trial, where p is the probability of success. It is the simplest discrete distribution and forms the building block for the Binomial Distribution.'
SET c.source = 'Stat400 teaching material - Jonathan Fernandez'
SET c.tags = ['Probability Theory', 'Statistics', 'Discrete Distribution', 'Bernoulli Trial']

MERGE (ev:Property {name: 'Expected Value', formula: 'E(X) = p'})
MERGE (var:Property {name: 'Variance', formula: 'V(X) = p(1 - p)'})

MERGE (c)-[:HAS_PROPERTY]->(ev)
MERGE (c)-[:HAS_PROPERTY]->(var)

MERGE (related:Concept {name: 'Binomial Distribution'})
MERGE (c)-[:RELATED_TO]->(related)

MERGE (theorem:Theorem {name: 'Parameters associated with the Bernoulli Distribution'})
MERGE (c)-[:INVOLVED_IN_THEOREM]->(theorem)

MERGE (app:Application {description: 'Modeling success/failure experiments like coin tosses, quality control tests, and yes/no surveys.'})
MERGE (c)-[:HAS_APPLICATION]->(app)


// Binomial Distribution
MERGE (c:Concept {name: 'Binomial Distribution'})
SET c.definition = 'The Binomial Distribution models the number of successes in a fixed number of independent Bernoulli trials.'
SET c.notation_latex_code = 'X \\sim \\text{Binomial}(n, p)'
SET c.notation_rendered = 'X ∼ Binomial(n, p)'
SET c.pmf_latex_code = 'p_X(x) = \\binom{n}{x} p^x (1 - p)^{n - x}, \\quad x = 0, 1, \\dots, n'
SET c.pmf_rendered = 'p_X(x) = (n choose x) p^x (1 - p)^{n - x}, x = 0, 1, ..., n'
SET c.description = 'A random variable X has the Binomial Distribution with parameters n ∈ ℕ and p ∈ (0, 1) if it represents the number of successes in n independent Bernoulli trials each with success probability p.'
SET c.source = 'Stat400 teaching material - Jonathan Fernandez'
SET c.tags = ['Probability Theory', 'Statistics', 'Discrete Distribution', 'Bernoulli Trials']

MERGE (ev:Property {name: 'Expected Value', formula: 'E(X) = np'})
MERGE (var:Property {name: 'Variance', formula: 'V(X) = np(1 - p)'})

MERGE (c)-[:HAS_PROPERTY]->(ev)
MERGE (c)-[:HAS_PROPERTY]->(var)

MERGE (related1:Concept {name: 'Bernoulli Distribution'})
MERGE (related2:Concept {name: 'Poisson Distribution'})
MERGE (c)-[:RELATED_TO]->(related1)
MERGE (c)-[:RELATED_TO {description: 'as an approximation'}]->(related2)

MERGE (theorem:Theorem {name: 'Parameters associated with the Binomial Distribution'})
MERGE (c)-[:INVOLVED_IN_THEOREM]->(theorem)

MERGE (app:Application {description: 'Used in scenarios like quality control, clinical trials, and survey sampling where the outcome is the number of successes in a series of independent trials.'})
MERGE (c)-[:HAS_APPLICATION]->(app)


// Hypergeometric Distribution
MERGE (c:Concept {name: 'Hypergeometric Distribution'})
SET c.definition = 'The Hypergeometric Distribution models the number of successes in a sequence of draws from a finite population without replacement.'
SET c.notation_latex_code = 'X \\sim \\text{Hypergeometric}(N, M, n)'
SET c.notation_rendered = 'X ∼ Hypergeometric(N, M, n)'
SET c.pmf_latex_code = 'p_X(x) = \\frac{\\binom{M}{x} \\binom{N - M}{n - x}}{\\binom{N}{n}}, \\quad x = 0, 1, \\dots, \\min(n, M)'
SET c.pmf_rendered = 'p_X(x) = [ (M choose x)(N - M choose n - x) ] / (N choose n ), x = 0, 1, ..., min(n, M)'
SET c.description = 'A random variable X has the Hypergeometric Distribution with parameters N (population size), M (number of successes in the population), and n (number of draws) when sampling is done without replacement. Unlike the Binomial Distribution, trials are not independent.'
SET c.source = 'Stat400 teaching material - Jonathan Fernandez'
SET c.tags = ['Probability Theory', 'Statistics', 'Discrete Distribution', 'Sampling Without Replacement']

MERGE (ev:Property {name: 'Expected Value', formula: 'E(X) = n * (M / N)'})
MERGE (var:Property {name: 'Variance', formula: 'V(X) = n * (M / N) * (1 - (M / N)) * ((N - n) / (N - 1))'})

MERGE (c)-[:HAS_PROPERTY]->(ev)
MERGE (c)-[:HAS_PROPERTY]->(var)

MERGE (related:Concept {name: 'Binomial Distribution'})
MERGE (c)-[:RELATED_TO {description: 'approximates Binomial when N is large'}]->(related)

MERGE (theorem:Theorem {name: 'Parameters associated with the Hypergeometric Distribution'})
MERGE (c)-[:INVOLVED_IN_THEOREM]->(theorem)

MERGE (app:Application {description: 'Used in quality control and lotteries where sampling is without replacement.'})
MERGE (c)-[:HAS_APPLICATION]->(app)


// Geometric Distribution
MERGE (c:Concept {name: 'Geometric Distribution'})
SET c.definition = 'The Geometric Distribution models the number of trials needed to get the first success in repeated independent Bernoulli trials.'
SET c.notation_latex_code = 'X \\sim \\text{Geom}(p)'
SET c.notation_rendered = 'X ∼ Geom(p)'
SET c.pmf_latex_code = 'p_X(x) = p(1 - p)^{x - 1}, \\quad x = 1, 2, 3, \\dots'
SET c.pmf_rendered = 'p_X(x) = p(1 - p)^{x - 1}, x = 1, 2, 3, ...'
SET c.description = 'A random variable X has the Geometric Distribution with parameter p ∈ (0, 1) if it represents the number of trials required to achieve the first success in independent Bernoulli trials.'
SET c.source = 'Stat400 teaching material - Jonathan Fernandez'
SET c.tags = ['Probability Theory', 'Statistics', 'Discrete Distribution', 'Waiting Time']

MERGE (ev:Property {name: 'Expected Value', formula: 'E(X) = 1 / p'})
MERGE (var:Property {name: 'Variance', formula: 'V(X) = (1 - p) / p^2'})

MERGE (c)-[:HAS_PROPERTY]->(ev)
MERGE (c)-[:HAS_PROPERTY]->(var)

MERGE (related:Concept {name: 'Negative Binomial Distribution'})
MERGE (c)-[:RELATED_TO]->(related)

MERGE (theorem:Theorem {name: 'Parameters associated with the Geometric Distribution'})
MERGE (c)-[:INVOLVED_IN_THEOREM]->(theorem)

MERGE (app:Application {description: 'Used in modeling the number of trials until first success in scenarios like quality control testing and reliability analysis.'})
MERGE (c)-[:HAS_APPLICATION]->(app)


// Negative Binomial Distribution
MERGE (c:Concept {name: 'Negative Binomial Distribution'})
SET c.definition = 'The Negative Binomial Distribution generalizes the Geometric Distribution by modeling the number of failures before achieving a specified number of successes.'
SET c.notation_latex_code = 'X \\sim \\text{NegBinomial}(r, p)'
SET c.notation_rendered = 'X ∼ NegBinomial(r, p)'
SET c.pmf_latex_code = 'p_X(x) = \\binom{x + r - 1}{x} p^r (1 - p)^x, \\quad x = 0, 1, 2, \\dots'
SET c.pmf_rendered = 'p_X(x) = (x + r - 1 choose x) p^r (1 - p)^x, x = 0, 1, 2, ...'
SET c.description = 'A random variable X has the Negative Binomial Distribution with parameters r ∈ ℕ and p ∈ (0, 1) if it represents the number of failures before achieving r successes in independent Bernoulli trials.'
SET c.source = 'Stat400 teaching material - Jonathan Fernandez'
SET c.tags = ['Probability Theory', 'Statistics', 'Discrete Distribution', 'Waiting Time']

MERGE (ev:Property {name: 'Expected Value', formula: 'E(X) = r(1 - p) / p'})
MERGE (var:Property {name: 'Variance', formula: 'V(X) = r(1 - p) / p^2'})

MERGE (c)-[:HAS_PROPERTY]->(ev)
MERGE (c)-[:HAS_PROPERTY]->(var)

MERGE (related:Concept {name: 'Geometric Distribution'})
MERGE (c)-[:RELATED_TO {description: 'special case when r = 1'}]->(related)

MERGE (theorem:Theorem {name: 'Parameters associated with the Negative Binomial Distribution'})
MERGE (c)-[:INVOLVED_IN_THEOREM]->(theorem)

MERGE (app:Application {description: 'Used in modeling the number of trials required to achieve a specified number of successes, such as in insurance claims or equipment failure.'})
MERGE (c)-[:HAS_APPLICATION]->(app)


// Poisson Distribution
MERGE (c:Concept {name: 'Poisson Distribution'})
SET c.definition = 'The Poisson Distribution models the number of events occurring in a fixed interval of time or space when events occur independently and at a constant average rate.'
SET c.notation_latex_code = 'X \\sim \\text{Poisson}(\\lambda)'
SET c.notation_rendered = 'X ∼ Poisson(λ)'
SET c.pmf_latex_code = 'p_X(x) = e^{-\\lambda} \\dfrac{\\lambda^x}{x!}, \\quad x = 0, 1, 2, \\dots'
SET c.pmf_rendered = 'p_X(x) = e^{-λ} (λ^x) / x!, x = 0, 1, 2, ...'
SET c.description = 'A random variable X has the Poisson Distribution with parameter λ > 0 if it represents the number of events occurring in a fixed period of time or space, with the events happening independently and at a constant rate.'
SET c.source = 'Stat400 teaching material - Jonathan Fernandez'
SET c.tags = ['Probability Theory', 'Statistics', 'Discrete Distribution', 'Poisson Process']

MERGE (ev:Property {name: 'Expected Value', formula: 'E(X) = λ'})
MERGE (var:Property {name: 'Variance', formula: 'V(X) = λ'})

MERGE (c)-[:HAS_PROPERTY]->(ev)
MERGE (c)-[:HAS_PROPERTY]->(var)

MERGE (related:Concept {name: 'Binomial Distribution'})
MERGE (c)-[:RELATED_TO {description: 'Poisson approximation to the Binomial'}]->(related)

MERGE (theorem:Theorem {name: 'Parameters associated with the Poisson Distribution'})
MERGE (c)-[:INVOLVED_IN_THEOREM]->(theorem)

MERGE (app:Application {description: 'Used in modeling the number of occurrences of rare events in fields like telecommunications (number of calls), astronomy (number of meteors), and finance (number of defaults).'})
MERGE (c)-[:HAS_APPLICATION]->(app)


// Relationships Between Distributions

// Binomial and Hypergeometric
MERGE (binomial:Concept {name: 'Binomial Distribution'})
MERGE (hypergeometric:Concept {name: 'Hypergeometric Distribution'})
MERGE (binomial)-[:RELATED_TO {description: 'Hypergeometric approximates Binomial when N is large compared to n'}]->(hypergeometric)

// Binomial and Poisson
MERGE (poisson:Concept {name: 'Poisson Distribution'})
MERGE (binomial)-[:RELATED_TO {description: 'Binomial approximates Poisson when n is large and p is small'}]->(poisson)

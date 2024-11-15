```cypher
// Create the new Exercise node
CREATE (e:Exercise {
  name: "coin toss example",
  problem_statement: "5 coins are tossed, each with a probability of heads of \\(\\frac{1}{2}\\). Assume outcomes are independent, find the PMF of the number of heads.",
  notation: "PMF",
  solution: "Let \\(X\\) denote the number of heads obtained. Then \\(X\\) is a binomial random variable with parameter \\((5, \\frac{1}{2})\\).\\np(0) = \\binom{5}{0} \\left(\\frac{1}{2}\\right)^0 \\left(\\frac{1}{2}\\right)^{5 - 0} = \\frac{1}{32}\\np(1) = \\binom{5}{1} \\left(\\frac{1}{2}\\right)^1 \\left(\\frac{1}{2}\\right)^{5 - 1} = \\frac{5}{32}\\np(2) = \\binom{5}{2} \\left(\\frac{1}{2}\\right)^2 \\left(\\frac{1}{2}\\right)^{5 - 2} = \\frac{10}{32}\\np(3) = \\binom{5}{3} \\left(\\frac{1}{2}\\right)^3 \\left(\\frac{1}{2}\\right)^{5 - 3} = \\frac{10}{32}\\np(4) = \\binom{5}{4} \\left(\\frac{1}{2}\\right)^4 \\left(\\frac{1}{2}\\right)^{5 - 4} = \\frac{5}{32}\\np(5) = \\binom{5}{5} \\left(\\frac{1}{2}\\right)^5 \\left(\\frac{1}{2}\\right)^{5 - 5} = \\frac{1}{32}",
  difficulty_level: "1/5",
  source: "Stat400 teaching material - Jonathan Fernandez"
})

// Since there are no existing nodes, create the 'discrete_binomial_concept' node
MERGE (c:Concept {name: "discrete_binomial_concept"})

// Create the relationship
CREATE (e)-[:IS_EXERCISE_FOR]->(c)
```
Given a dictionary of following format, create a html rendering function that get passed to nodeLabel (https://github.com/vasturiano/force-graph), and render the content of the node properly on the webpage. The rendering should render the hiearchy between attributes of the nodes as different <h{n}> blocks (starting from h3); e.g.,
for Input example
  "attributes": {
    "name": "Poisson Distribution",
    "aliases": null,
    "definition": {
      "notation": "Pois(\\lambda)",
      "explanation": [
        {
          "part": "\\lambda",
          "range": "\\lambda \\in \\{0, \\infty\\}",
          "description": "The parameter \\lambda represents the average rate or mean number of occurrences during a given time interval."
        }
      ],
      "description": "The Poisson Distribution is a discrete probability distribution expressing the probability of a given number of events occurring in a fixed interval of time or space if these events happen with a known constant mean rate and independently of the time since the last event."
    }
  }

the rendering should be
<h3>name</h3>
<p>Poisson Distribution</p>
<!-- <h4>aliases</h4> -->
<!-- note that there is no aliases in this example, so this section is skipped -->
<h3>definition</h3>
<h4>notation</h4>
<p>Pois(\\lambda)</p>
<h5>explanation1</h5>
<p>The parameter \\lambda represents the average rate or mean number of occurrences during a given time interval.</p>
<!-- <h5>explanation2</h5>
... more if there are more than 1 -->
<h4>description</h4>
<p>The Poisson Distribution is a discrete probability distribution expressing the probability of a given number of events occurring in a fixed interval of time or space if these events happen with a known constant mean rate and independently of the time since the last event.</p>

For rendering latex properly in <p> tags, both MathJax and KaTeX are supported.
https://chatgpt.com/share/673d1055-6eb0-800b-bb16-ae11b6a3db1e
Note that information provided by chatgpt may not be accurate.
input = r"""```markdown
# Property Node

## Attributes

- **Name**: Expected value of Hypergeometric Distribution
  - **Aliases**: ["Mean of Hypergeometric Distribution", "Expected Value"]

- **Definition**:
  - **Notation**:
    - Latex: `E(X) = n \left(\frac{M}{N}\right)`
    - Rendered: $E(X) = n \left(\frac{M}{N}\right)$
    - **Range**: The expected value $E(X)$ is not necessarily a whole number; it takes a value based on $N$, $M$, and $n$ within the defined bounds.

- **Description**:
  - The expected value of a Hypergeometric Distribution, which describes the mean or average outcome when randomly drawing $n$ items without replacement from a finite population of size $N$ containing exactly $M$ successes.

- **Proof**:
  - To determine the expected value of a hypergeometric random variable $X \sim \text{Hyper}(N, M, n)$, consider the indicator random variable $I_i$ which is 1 if the $i$-th draw is a success and 0 otherwise. Thus, $X = I_1 + I_2 + \cdots + I_n$. By the linearity of expectation, we have $E(X) = E(I_1) + E(I_2) + \cdots + E(I_n)$. Since the probability of each draw being a success is $\frac{M}{N}$, we find $E(X) = n \frac{M}{N}$.

## Relationships

- **is_property_of** ← Hypergeometric Distribution
- **is_child_concept_of** ← Expected Value of Distribution

```"""


def extract_markdown_content(response: str) -> str:
    # Find the outermost markdown block
    start = response.find("```markdown")
    if start == -1:
        return response
        
    # Find the matching closing block by counting nested blocks
    content_start = start + len("```markdown")
    count = 1
    current_pos = content_start
    
    while count > 0 and current_pos < len(response):
        next_triple = response.find("```", current_pos)
        if next_triple == -1:
            break
            
        # Move position past the triple backticks
        current_pos = next_triple + 3
        
        # Check if there's content after the backticks and if it starts with a letter
        remaining = response[current_pos:].lstrip()
        if remaining and remaining[0].isalpha():
            count += 1
        else:
            count -= 1
    
    if count == 0:
        return response[content_start:current_pos-3].strip()
    
    return response[content_start:].strip()

print(extract_markdown_content(input))
import re

subsection_pattern = r'\\subsection(?:\[([^\]]+)\])?\{([^}]+)\}'
section_content = r'''This is a section
\subsection{This is a subsection}
This is the content of the subsection
\subsection{This is another subsection}
This is the content of the another subsection
'''

subsections = re.split(subsection_pattern, section_content)
for subsection in subsections:
    print(f"'{subsection}'")

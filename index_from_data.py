import pandas as pd

# Read the CSV file
df = pd.read_csv('data/concepts_regex_blocks.csv')

# Initialize the content of index.md
index_content = "# Table of Contents\n\n"

current_chapter = ""
current_section = ""
current_subsection = ""

# Process each row in the DataFrame
for _, row in df.iterrows():
    chapter = row['chapter_name']
    section = row['section_name']
    subsection = row['subsection_name']
    block_type = row['block_type']
    content = row['block_content']

    # Add chapter if it's new
    if chapter != current_chapter:
        index_content += f"## {chapter}\n\n"
        current_chapter = chapter
        current_section = ""
        current_subsection = ""

    # Add section if it's new
    if pd.notna(section) and section != current_section:
        index_content += f"### {section}\n\n"
        current_section = section
        current_subsection = ""

    # Add subsection if it's new
    if pd.notna(subsection) and subsection != current_subsection:
        index_content += f"#### {subsection}\n\n"
        current_subsection = subsection

    # Add content
    index_content += f"- {block_type.capitalize()}: {content.split('\n')[0]}\n\n"

# Write the content to index.md
with open('index.md', 'w') as f:
    f.write(index_content)

print("index.md file created successfully!")
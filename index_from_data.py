import pandas as pd

# Read the CSV file
df = pd.read_csv('data/concepts_regex_blocks.csv')

# Initialize the content of index.md
index_content = "# Table of Contents\n\n"

current_chapter = ""
current_section = ""
current_subsection = ""

def index_with_section_briefing(df):
    
    
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
    with open('index_with_section_briefing.md', 'w') as f:
        f.write(index_content)

def index_only(df): # only log unique chapter + section name combinations
    index_content = ""
    
    current_chapter = ""
    current_section = ""
    
    for _, row in df.iterrows():
        chapter = row['chapter_name']
        section = row['section_name']

        if pd.notna(chapter) and chapter != current_chapter:
            index_content += f"## {chapter}\n\n"
            current_chapter = chapter

        if pd.notna(section) and section != current_section:
            index_content += f"### {section}\n\n"
            current_section = section
            
        index_content += f"- {row['block_type'].capitalize()}: {row['block_content'].split('\n')[0]}\n\n"

    with open('index_only.md', 'w') as f:
        f.write(index_content)

def main():
    index_with_section_briefing(df)
    index_only(df)

if __name__ == "__main__":
    main()

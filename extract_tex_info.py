import os
import re
import pandas as pd

block_name_mapping = {
    'defn': 'definition',
    'ex': 'example',
    'thm': 'theorem',
    'general': 'general description'
}

def extract_tex_info(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    chapter_pattern = r'\\chapter\[([^\]]+)\]'
    section_pattern = r'\\section(?:\[([^\]]+)\])?\{([^}]+)\}'
    subsection_pattern = r'\\subsection(?:\[([^\]]+)\])?\{([^}]+)\}'
    block_pattern = r'\\begin\{(defn|ex|thm)\}(.*?)\\end\{\1\}'

    chapter_name = re.search(chapter_pattern, content)
    chapter_name = chapter_name.group(1) if chapter_name else "Unknown Chapter"

    data = []

    sections = re.split(section_pattern, content)[1:]
    for i in range(0, len(sections), 3):
        section_name_bracket = sections[i]
        section_name_brace = sections[i+1]
        section_content = sections[i+2]

        section_name = section_name_bracket if section_name_bracket else section_name_brace

        subsections = re.split(subsection_pattern, section_content)
        
        if len(subsections) == 1:
            # No subsections found, process the entire section content
            process_content(section_content, data, chapter_name, section_name, None)
        else:
            # Process content before the first subsection
            process_content(subsections[0], data, chapter_name, section_name, None)
            
            # Process subsections
            for j in range(1, len(subsections), 3):
                subsection_name_bracket = subsections[j]
                subsection_name_brace = subsections[j+1]
                subsection_content = subsections[j+2]
                
                current_subsection = subsection_name_bracket if subsection_name_bracket else subsection_name_brace
                process_content(subsection_content, data, chapter_name, section_name, current_subsection)

    # Remove extracted blocks from the content
    remaining_content = re.sub(block_pattern, '', content, flags=re.DOTALL)

    return data, remaining_content

def process_content(content, data, chapter_name, section_name, subsection_name):
    block_pattern = r'\\begin\{(defn|ex|thm)\}(.*?)\\end\{\1\}'
    matches = list(re.finditer(block_pattern, content, re.DOTALL))

    prev_end = 0
    for match in matches:
        start, end = match.span()

        # Extract general description before this block
        general_content = content[prev_end:start].strip()
        if general_content and not general_content.isspace():
            data.append({
                'chapter_name': chapter_name,
                'section_name': section_name,
                'subsection_name': subsection_name,
                'block_type': block_name_mapping['general'],
                'block_content': general_content
            })

        # Extract the block
        block_type = match.group(1)
        block_content = match.group(2).strip()
        data.append({
            'chapter_name': chapter_name,
            'section_name': section_name,
            'subsection_name': subsection_name,
            'block_type': block_name_mapping[block_type],
            'block_content': block_content
        })

        prev_end = end

    # Process any remaining general description after the last block
    general_content = content[prev_end:].strip()
    if general_content and not general_content.isspace():
        data.append({
            'chapter_name': chapter_name,
            'section_name': section_name,
            'subsection_name': subsection_name,
            'block_type': block_name_mapping['general'],
            'block_content': general_content
        })

def main():
    tex_folder = r'Stat400_Concepts 09-30-2024\Stat400_Textbook'
    output_file = r'data\concepts_regex_blocks.csv'
    remaining_folder = r'data'

    all_data = []

    for filename in os.listdir(tex_folder):
        if filename.startswith('Chapter') and filename.endswith('.tex'):
            file_path = os.path.join(tex_folder, filename)
            extracted_data, remaining_content = extract_tex_info(file_path)
            all_data.extend(extracted_data)

            # Save remaining content to a new file
            # remaining_file = os.path.join(remaining_folder, f"remaining_of_{filename}")
            # with open(remaining_file, 'w', encoding='utf-8') as f:
            #     f.write(remaining_content)
            # print(f"Remaining content saved to {remaining_file}")

    df = pd.DataFrame(all_data)
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    main()
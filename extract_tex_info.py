import os
import re
import pandas as pd

def extract_tex_info(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    chapter_pattern = r'\\chapter\[([^\]]+)\]'
    section_pattern = r'\\section\{([^}]+)\}'
    block_pattern = r'\\begin\{(defn|ex|thm)\}(.*?)\\end\{\1\}'

    chapter_name = re.search(chapter_pattern, content)
    chapter_name = chapter_name.group(1) if chapter_name else "Unknown Chapter"

    data = []

    
    sections = re.split(section_pattern, content)[1:]
    for i in range(0, len(sections), 2):
        section_name = sections[i]
        section_content = sections[i+1]

        blocks = re.findall(block_pattern, section_content, re.DOTALL)
        for block_type, block_content in blocks:
            data.append({
                'chapter_name': chapter_name,
                'section_name': section_name,
                'block_type': block_type,
                'block_content': block_content.strip()
            })

    return data

def main():
    tex_folder = r'Stat400_Concepts 09-30-2024\Stat400_Textbook'
    output_file = r'data\concepts_regex_blocks.csv'

    all_data = []

    for filename in os.listdir(tex_folder):
        if filename.startswith('Chapter') and filename.endswith('.tex'):
            file_path = os.path.join(tex_folder, filename)
            all_data.extend(extract_tex_info(file_path))

    df = pd.DataFrame(all_data)
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    main()
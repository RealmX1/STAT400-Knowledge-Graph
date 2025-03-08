import os
import openai

client = openai.OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
    ],
)

def load_markdown_schema(schema_type: str):
    markdown_schema_path = os.path.join('node_schemas', f'{schema_type}_schema.md')
    if not os.path.exists(markdown_schema_path):
        raise FileNotFoundError(f"Schema file not found: {markdown_schema_path}")
    with open(markdown_schema_path, 'r', encoding='utf-8') as file:
        markdown_schema = file.read()
    return markdown_schema

def latex_to_markdown(latex_text: str, file_name: str):
    print(file_name)
    pass

def convert_all_file_in_directory(directory: str):
    for file in os.listdir(directory):
        print(file)
        if file.endswith('.tex'):
            with open(os.path.join(directory, file), 'r', encoding='utf-8') as f:
                latex_text = f.read()
            markdown_schema = load_markdown_schema('Theorem')
            markdown_text = latex_to_markdown(latex_text, file)

convert_all_file_in_directory('members_work/Varun/Conversions_new_schema')

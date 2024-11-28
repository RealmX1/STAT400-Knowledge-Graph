import os
import json
import re
from typing import List, Dict, Tuple
import time
from openai import OpenAI
import pandas as pd
from typing import Union
client = OpenAI()
from pathlib import Path

stage_names = ["generate_nodes_list", "context2node-md", "node-md2cypher"]

class KnowledgeGraphPipeline:
    def __init__(self, chapter_path: str, overwrite: bool = False):
        # OpenAI configuration
        self.chapter_path = chapter_path
        self.chapter_name = Path(chapter_path).stem
        self.overwrite = overwrite
        
        self.chapter_content = self.load_chapter_content()
        
        # Paths configuration
        self.schema_dir = "node_schemas/md_schemas"
        self.prompt_dir = "LLM assisted Knowledge Instantiation"
        self.runtime_dir = "LLM assisted Knowledge Instantiation/runtime"
        self.chapter_runtime_dir = Path(f"{self.runtime_dir}/{self.chapter_name}")
        
        # Delete and recreate runtime directory if overwrite is True
        if self.overwrite:
            os.rmdir(self.chapter_runtime_dir)
            self.chapter_runtime_dir.mkdir(parents=True, exist_ok=True)
        else:
            if not self.chapter_runtime_dir.exists():
                os.makedirs(self.chapter_runtime_dir, exist_ok=True)
            else:
                print(f"Runtime directory {self.chapter_runtime_dir} already exists. This run will not overwrite any already completed stages.")
                
        # Store state using pandas DataFrames
        self.existing_nodes = self.load_existing_nodes()
        self.new_nodes = pd.DataFrame(columns=["node_type", "node_name"])
    
    def load_existing_nodes(self) -> pd.DataFrame:
        self.existing_nodes_path = os.path.join(self.runtime_dir, "existing_nodes.csv")
        if os.path.exists(self.existing_nodes_path):
            return pd.read_csv(self.existing_nodes_path)
        else:
            return pd.DataFrame(columns=["node_type", "node_name"])

    def make_llm_call(self, system_prompt: str, user_input: str, response_format: dict = {"type":"text"}) -> str:
        # if response_format["type"] == "text":
        #     llm_call = client.chat.completions.create
        # elif response_format["type"] == "json_object" or response_format["type"] == "json_schema":
        #     llm_call = client.beta.chat.completions.parse
        """Make an API call to OpenAI"""
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                response_format=response_format,
                max_tokens=4096
            )
            
            print(f"Received response: {response.choices[0].message}")
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error making LLM call: {e}")
            return None

    def get_output_path(self, stage_name: str, file_name: str, file_type: str = "md"):
        stage_dir = os.path.join(self.chapter_runtime_dir, stage_name)
        if not os.path.exists(stage_dir):
            os.makedirs(stage_dir, exist_ok=self.overwrite)
        
        output_path = os.path.join(stage_dir, f"{file_name}.{file_type}")
        return output_path
    
    def check_overwrite(self, output_path: str):
        if not self.overwrite and os.path.exists(output_path):
            print(f"File already exists at {output_path}. Skipping...")
            return False
        return True

    def save_output(self, output_path: str, content: Union[str, pd.DataFrame], file_type: str = "md"):
        """Save output to a file"""
        if isinstance(content, pd.DataFrame) and file_type == "csv":
            content.to_csv(output_path, index=False)
        else:
            with open(output_path, "w", encoding="utf-8") as f:
                if file_type == "json":
                    json.dump(content, f, indent=4)
                elif file_type == "md":
                    f.write(content)

    def load_prompt(self, prompt_name: str) -> str:
        """Load a specific prompt template"""
        prompt_path = Path(self.prompt_dir) / prompt_name
        try:
            with open(prompt_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: Prompt file {prompt_name} not found")
            return None

    def load_chapter_content(self) -> str:
        """Load the content of the designated chapter"""
        try:
            print(self.chapter_path)
            with open(self.chapter_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: Chapter file not found at {self.chapter_path}")
            return None
    
    def load_node_type_description(self) -> str:
        # inside node_schemas\README.md, after the line "# Description used in Prompting"
        node_description_path = os.path.join('node_schemas', "README.md")
        with open(node_description_path, "r", encoding="utf-8") as f:
            node_description = f.read()
        # remove the all lines before and including "# Description used in Prompting"
        node_description = node_description.split("# Description used in Prompting")[1]
        return node_description
            

    def stage1_generate_nodes_list(self) -> pd.DataFrame:
        """Stage 1: Generate list of new nodes"""
        print("\n=== Stage 1: Generating list of new nodes ===")
        output_path = self.get_output_path(stage_name=stage_names[0], file_name="nodes_list", file_type="csv")
        if not self.check_overwrite(output_path):
            return pd.read_csv(output_path)
        
        # Load necessary resources
        prompt = self.load_prompt(f"{stage_names[0]}_prompt.md")
        
        if not prompt or not self.chapter_content:
            return False
        
        # Prepare input for LLM
        user_input = {
            "chapter_content": self.chapter_content,
            "existing_nodes": self.existing_nodes.to_dict('records'),
            "node_type_description": self.load_node_type_description()
        }
        
        # Make LLM call with JSON response format
        response = self.make_llm_call(
            prompt, 
            json.dumps(user_input),
            response_format={"type": "json_object"}
        )
        if not response:
            return False
            
        # Convert JSON response to DataFrame
        nodes_data = json.loads(response)
        self.new_nodes = pd.DataFrame(nodes_data['nodes'], columns=["node_type", "node_name"])
        
        # Save output
        self.save_output(output_path=output_path, content=self.new_nodes, file_type="csv")
        
        print(f"\nGenerated nodes list saved to: {output_path}")
        
        # Wait for user verification
        while True:
            proceed = input("\nReview the generated nodes list. Enter 'Y' to continue, or 'N' to abort: ")
            if proceed.upper() == 'N':
                print("Aborting pipeline execution after stage 1 without verifying nodes list.")
                exit(1)
            elif proceed.upper() == 'Y':
                # Concatenate with existing nodes
                self.existing_nodes = pd.concat([self.existing_nodes, self.new_nodes], ignore_index=True)
                
                # Save to runtime/existing_nodes.csv
                self.existing_nodes.to_csv(self.existing_nodes_path, index=False)
                
                return self.new_nodes
            
    def load_node_type_schema(self, node_type:str, type:str) -> str:
        schema_path = os.path.join(self.schema_dir, f"{node_type}_schema.{type}")
        with open(schema_path, "r", encoding="utf-8") as f:
            if type == "json":
                return json.load(f)
            else:
                text = f.read()
                # remove anything wrapped in ignore html tags
                text = re.sub(r'<ignore>.*?</ignore>', '', text, flags=re.DOTALL)
                # remove anything wrapped in "<!--" and "-->" (default comment in markdown)
                text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
                return text
        
    def load_stage2_prompt(self, node_name:str, node_type:str) -> str:
        system_prompt = self.load_prompt(f"{stage_names[1]}_prompt.md")
        
        input_format = system_prompt.split("Input will be provided in following format:")[1]
        """
        <div class="input">
            <div class="existing-nodes">{existing_nodes}</div>
            <div class="node-name">{node_name}</div>
            <div class="node-type">{node_type}</div>
            <div class="chapter-content">{chapter_content}</div>
            <div class="additional-context">{additional_context}</div>
            <div class="node-type-schema">{node_type_schema}</div>
        </div>
        """
        formatted_input = input_format.format(
            existing_nodes=self.existing_nodes,
            node_name=node_name,
            node_type=node_type,
            chapter_content=self.chapter_content,
            additional_context="",
            node_type_schema=self.load_node_type_schema(node_type, "md")
        )
        return system_prompt, formatted_input
        
    def stage2_generate_markdown_nodes(self, ask_for_verification: bool = True) -> bool:
        """Stage 2: Generate markdown for each new node"""
        print("\n=== Stage 2: Generating markdown nodes ===")
        
        # debug. load new_nodes from runtime/generate_nodes_list/nodes_list.md
        self.new_nodes = pd.read_csv(os.path.join(self.chapter_runtime_dir, stage_names[0], "nodes_list.csv"), header=0)
        
        for _, row in self.new_nodes.iterrows():
            node_type = row['node_type']
            node_name = row['node_name']
            
            output_path = self.get_output_path(stage_names[1], f"{node_type};{node_name}", "md")
            if not self.check_overwrite(output_path):
                continue
            
            print(f"\nProcessing node: ({node_type}) {node_name}")
            
            system_prompt, user_input = self.load_stage2_prompt(node_name, node_type)
            
            if not system_prompt or not user_input:
                print("Error: Failed to load system prompt or formatted input")
                return False
            
            # Make LLM call
            response = self.make_llm_call(system_prompt, user_input)
            if not response:
                continue
                
            # Save output
            self.save_output(output_path, response, "md")
            print(f"Generated markdown saved to: {output_path}")
            
            # Wait for user verification
            if ask_for_verification:
                proceed = input("\nReview the generated markdown. Enter 'Y' to continue, and 'N' to abort: ")
                if proceed.upper() != 'Y':
                    print(f"Aborting pipeline execution early after stage 2 without verifying {node_name}.")
                    return False
                
        return True
    
    def stage2_5_markdown_to_json(self) -> None:
        # For each markdown node, convert it to JSON
        markdown_dir = self.chapter_runtime_dir / stage_names[1]
        
        for markdown_file in markdown_dir.glob("*.md"):
            output_path = self.get_output_path(stage_names[1], f"{markdown_file.stem}", "json")
            if not self.check_overwrite(output_path):
                continue
            
            print(f"Turning {markdown_file.name} into JSON...")
            file_name = markdown_file.stem
            node_type, node_name = file_name.split(";")
            markdown_content = markdown_file.read_text(encoding="utf-8")
            
            json_schema = self.load_node_type_schema(node_type, "json")
            
            system_prompt = """You will be provided with a markdown node on a statistical knowledge, and a JSON schema for the respective node type. Your task is to convert the markdown node to a JSON object according to the schema.
Note that you should not change the content corresponding to each subsection in the markdown node; and you should use the formatting for latex in markdown, that is, using $...$ for inline math and $$...$$ for display math."""
            
            user_input = {
                "markdown_node": markdown_content
            }
            
            response_format = {
                "type": "json_schema",
                "json_schema": json_schema,
            }
            
            response = self.make_llm_call(system_prompt, json.dumps(user_input), response_format)
            data = json.loads(response)
            
            # save to runtime/stage2/node_type;node_name.json
            self.save_output(output_path, data, "json")
            print(f"Generated JSON saved to: {output_path}")
        
        # return True

    def stage3_generate_cypher(self) -> bool:
        """Stage 3: Convert markdown nodes to Cypher scripts"""
        print("\n=== Stage 3: Generating Cypher scripts ===")
        
        prompt = self.load_prompt(f"{stage_names[2]}_prompt.md")
        
        input_dir = self.chapter_runtime_dir / stage_names[1]
        if not input_dir.exists():
            print("Error: No markdown nodes found")
            return False
            
        for markdown_file in input_dir.glob("*.md"):
            input_file_name = markdown_file.stem
            output_file_name = f"cypher;{input_file_name}"
            print(f"\nProcessing markdown file: {input_file_name}")
            output_path = self.get_output_path(stage_names[2], output_file_name)
            if not self.check_overwrite(output_path):
                continue
            
            # check load the json file with same name if it exists
            json_file_path = self.get_output_path(stage_names[1], input_file_name, "json")
            if os.path.exists(json_file_path):
                print(f"JSON file already exists at {json_file_path}. loading it...")
                with open(json_file_path, 'r', encoding='utf-8') as f:
                    input_content = json.load(f)
            else:            
                # Read markdown content
                with open(markdown_file, "r", encoding="utf-8") as f:
                    input_content = f.read()
            
            existing_nodes_list = self.existing_nodes.to_dict('records')
            print(type(existing_nodes_list))
            print(existing_nodes_list[0])
            # Prepare input for LLM
            user_input = {
                "node_to_add": input_content,
                "existing_nodes": existing_nodes_list
            }
            
            # Make LLM call
            response = self.make_llm_call(prompt, json.dumps(user_input))
            if not response:
                continue
                
            # Save output
            self.save_output(output_path, response)  # Fixed the save_output call
            print(f"Generated Cypher script saved to: {output_path}")
            
            # # Wait for user verification
            # proceed = input("\nReview the generated Cypher script. Enter 'Y' to continue: ")
            # if proceed.upper() != 'Y':
            #     return False
                
        return True

def main():
    # Get OpenAI API key and chapter information
    chapter_path = "Stat400_Concepts 09-30-2024/Stat400_Textbook/Chapter03.tex"
    
    # Initialize pipeline
    pipeline = KnowledgeGraphPipeline(chapter_path)
    
    # Execute pipeline stages sequentially
    
    # print(f"\nExecuting Stage {1}...")
    # node_list = pipeline.stage1_generate_nodes_list()
    # print(node_list[:5])
    
    # print(f"\nExecuting Stage {2}...")
    # pipeline.stage2_generate_markdown_nodes()
    
    # print(f"\nExecuting Stage {2.5}...")
    # pipeline.stage2_5_markdown_to_json()
    
    print(f"\nExecuting Stage {3}...")
    pipeline.stage3_generate_cypher()
    
    print("\nPipeline execution completed")

if __name__ == "__main__":
    main() 
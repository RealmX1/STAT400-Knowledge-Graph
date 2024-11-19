import os
import json
import re
from typing import List, Dict, Tuple
import time
from openai import OpenAI
import pandas as pd

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
        existing_nodes_path = os.path.join(self.runtime_dir, "existing_nodes.csv")
        if os.path.exists(existing_nodes_path):
            return pd.read_csv(existing_nodes_path)
        return pd.DataFrame(columns=["node_type", "node_name"])

    def make_llm_call(self, system_prompt: str, user_input: str, response_format: dict = {"type":"text"}) -> str:
        """Make an API call to OpenAI"""
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                response_format=response_format
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error making LLM call: {e}")
            return None

    def save_output(self, stage_name: str, file_name: str, content: str):
        """Save LLM output to a file"""
        stage_dir = os.path.join(self.chapter_runtime_dir, stage_name)
        if not os.path.exists(stage_dir):
            os.makedirs(stage_dir, exist_ok=self.overwrite)
        
        output_path = os.path.join(stage_dir, f"{file_name}.md")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        return output_path

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
        schema_path = os.path.join('node_schemas', "README.md")
        with open(schema_path, "r", encoding="utf-8") as f:
            schema = f.read()
        # remove the all lines before and including "# Description used in Prompting"
        schema = schema.split("# Description used in Prompting")[1]
        return schema
            

    def stage1_generate_nodes_list(self) -> pd.DataFrame:
        """Stage 1: Generate list of new nodes"""
        print("\n=== Stage 1: Generating list of new nodes ===")
        
        # use existing nodes_list file if it exists and overwrite is False
        chapter_nodes_list_path = os.path.join(self.chapter_runtime_dir, stage_names[0], "nodes_list.md")
        if not self.overwrite and os.path.exists(chapter_nodes_list_path):
            print(f"Nodes list already exists at {chapter_nodes_list_path}. Loading it...")
            with open(chapter_nodes_list_path, "r", encoding="utf-8") as f:
                chapter_nodes = [line.strip().split(":") for line in f.readlines()]
                self.new_nodes = pd.DataFrame(chapter_nodes, columns=["node_type", "node_name"])
            return self.new_nodes
        
        # Load necessary resources
        prompt = self.load_prompt(f"{stage_names[0]}_prompt.md")
        
        if not prompt or not self.chapter_content:
            return False
        
        # Prepare input for LLM
        user_input = {
            "chapter_content": self.chapter_content,
            "existing_nodes": self.existing_nodes,
            "node_type_description": self.load_node_type_description()
        }
        
        # Make LLM call
        response = self.make_llm_call(prompt, json.dumps(user_input))
        if not response:
            return False
            
        # Save output
        output_path = self.save_output(stage_names[0], "nodes_list", response)
        print(f"\nGenerated nodes list saved to: {output_path}")
        
        # Wait for user verification
        while True:
            proceed = input("\nReview the generated nodes list. Enter 'Y' to continue, or 'N' to abort: ")
            if proceed.upper() == 'N':
                print("Aborting pipeline execution after stage 1")
                exit(1)
            elif proceed.upper() == 'Y':
                # Load user updated node list into DataFrame
                with open(output_path, "r", encoding="utf-8") as f:
                    chapter_nodes = [line.strip().split(":") for line in f.readlines()]
                    self.new_nodes = pd.DataFrame(chapter_nodes, columns=["node_type", "node_name"])
                
                # Concatenate with existing nodes
                self.existing_nodes = pd.concat([self.existing_nodes, self.new_nodes], ignore_index=True)
                
                # Save to runtime/existing_nodes.csv
                self.existing_nodes.to_csv(os.path.join(self.chapter_runtime_dir, "existing_nodes.csv"), index=False)
                
                return self.new_nodes
            
    def load_node_type_schema(self, node_type:str, type:str) -> str:
        schema_path = os.path.join(self.schema_dir, f"{node_type}_schema.{type}")
        with open(schema_path, "r", encoding="utf-8") as f:
            return f.read()
        
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
        
    def stage2_generate_markdown_nodes(self) -> bool:
        """Stage 2: Generate markdown for each new node"""
        print("\n=== Stage 2: Generating markdown nodes ===")
        
        # debug. load new_nodes from runtime/generate_nodes_list/nodes_list.md
        self.new_nodes = pd.read_csv(os.path.join(self.chapter_runtime_dir, stage_names[0], "nodes_list.csv"), header=0)
        
        for _, row in self.new_nodes.iterrows():
            node_type = row['node_type']
            node_name = row['node_name']
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
            output_path = self.save_output(stage_names[1], f"{node_type};{node_name}", response)
            print(f"Generated markdown saved to: {output_path}")
            
            # Wait for user verification
            proceed = input("\nReview the generated markdown. Enter 'Y' to continue, and 'N' to abort: ")
            if proceed.upper() != 'Y':
                return False
            else:
                self.stage2_5_markdown_to_json(response, node_type, node_name)
                
        return True
    
    def stage2_5_markdown_to_json(self, markdown_content: str, node_type: str, node_name: str) -> bool:
        """Stage 2.5: Convert markdown nodes to JSON"""
        print("\n=== Stage 2.5: Converting markdown nodes to JSON ===")
        
        json_schema = self.load_node_type_schema(node_type, "json")
        
        system_prompt = """
        You will be provided with a markdown node on a statistical knowledge, and a JSON schema for the respective node type. Your task is to convert the markdown node to a JSON object according to the schema.
        """
        
        user_input = {
            "markdown_node": markdown_content
        }
        
        response_format = {
            "type": "json_schema",
            "schema": json_schema
        }
        
        response = self.make_llm_call(system_prompt, json.dumps(user_input), response_format)
        
        # save to runtime/stage2/node_type;node_name.json
        output_path = self.save_output(stage_names[2], f"{node_type};{node_name}", response)
        print(f"Generated JSON saved to: {output_path}")
        
        return True

    def stage3_generate_cypher(self) -> bool:
        """Stage 3: Convert markdown nodes to Cypher scripts"""
        print("\n=== Stage 3: Generating Cypher scripts ===")
        
        prompt = self.load_prompt(f"{stage_names[2]}_prompt.md")
        
        markdown_dir = self.chapter_runtime_dir / stage_names[1]
        if not markdown_dir.exists():
            print("Error: No markdown nodes found")
            return False
            
        for markdown_file in markdown_dir.glob("*.md"):
            print(f"\nProcessing markdown file: {markdown_file.name}")
            file_name = markdown_file.stem
            output_file_name = f"cypher;{file_name}"
            
            # if output file already exists, and overwrite is false, skip.
            if not self.overwrite and os.path.exists(os.path.join(self.chapter_runtime_dir, stage_names[2], f"{output_file_name}.md")):
                print(f"Cypher script already exists at {os.path.join(self.chapter_runtime_dir, stage_names[2], f'{output_file_name}.md')}. Skipping...")
                continue
            
            # Read markdown content
            with open(markdown_file, "r", encoding="utf-8") as f:
                markdown_content = f.read()
            
            # Prepare input for LLM
            user_input = {
                "markdown_node": markdown_content,
                "existing_nodes": self.existing_nodes
            }
            
            # Make LLM call
            response = self.make_llm_call(prompt, json.dumps(user_input))
            if not response:
                continue
                
            # Save output
            output_path = self.save_output(stage_names[2], output_file_name, response)
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
    
    print(f"\nExecuting Stage {2}...")
    pipeline.stage2_generate_markdown_nodes()
    
    # print(f"\nExecuting Stage {3}...")
    # pipeline.stage3_generate_cypher()
    
    print("\nPipeline execution completed")

if __name__ == "__main__":
    main() 
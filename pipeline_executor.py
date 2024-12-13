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

from neo4j_agent import execute_cypher, add_node, add_relationship, check_node_exists, check_relationship_exists

stage_names = ["generate_nodes_list", "context2node-md", "node-md2cypher"]

class KnowledgeGraphPipeline:
    def __init__(self, chapter_path: str, overwrite: bool = False, rerun_cypher: bool = False, format_node_attributes: bool = False,
                 source_name: str = None, source_author: str = None):
        # OpenAI configuration
        self.chapter_path = chapter_path
        self.chapter_name = Path(chapter_path).stem
        self.overwrite = overwrite
        self.rerun_cypher = rerun_cypher
        self.format_node_attributes = format_node_attributes
        
        self.chapter_content = self.load_chapter_content()
        
        # Paths configuration
        self.schema_dir = "node_schemas/md_schemas"
        self.prompt_dir = "LLM_assisted_knowledge_instantiation/prompts"
        self.runtime_dir = "LLM_assisted_knowledge_instantiation/runtime"
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

    def make_llm_call(self, system_prompt: str, user_input: str, response_format: dict = {"type":"text"}, stage_name: str = None, node_name: str = None) -> str:
        # create csv to log the llm calls if it doesn't exist; it should be a dataframe with 5 columns: chapter_name, stage_name, system_prompt, user_input, response
        llm_call_log_df = pd.DataFrame(columns=["timestamp", "chapter_name", "stage_name", "node_name", "system_prompt", "user_input", "response"])
        llm_call_log_path = os.path.join(self.runtime_dir, "llm_call_log.csv")
        if os.path.exists(llm_call_log_path):
            llm_call_log_df = pd.read_csv(llm_call_log_path)
                
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
            
            # print(f"Received response: {response.choices[0].message}")
            # log the call
            llm_call_log_df.loc[len(llm_call_log_df)] = {
                "timestamp": time.time(),
                "chapter_name": self.chapter_name,
                "stage_name": stage_name,
                "system_prompt": system_prompt,
                "user_input": user_input,
                "response": response.choices[0].message.content,
                "node_name": node_name
            }
            llm_call_log_df.to_csv(llm_call_log_path, index=False)
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
    
    def load_json_schema(self, file_path: str) -> dict:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    # TODO: divide the node generation in to multiple step; each step focusing on a single node type
    def stage1_generate_nodes_list(self) -> pd.DataFrame:
        """Stage 1: Generate list of new nodes"""
        print("\n=== Stage 1: Generating list of new nodes ===")
        output_path = self.get_output_path(stage_name=stage_names[0], file_name="nodes_list", file_type="csv")
        if not self.check_overwrite(output_path):
            return pd.read_csv(output_path)
        
        # Load necessary resources
        prompt = self.load_prompt(f"{stage_names[0]}_prompt.md")
        schema = self.load_json_schema(Path(self.prompt_dir) / f"{stage_names[0]}_schema.json")
        
        response_format = {"type": "json_schema", "json_schema": schema}
        
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
            response_format,
            stage_name=stage_names[0]
        )
        if not response:
            return False
            
        # Convert JSON response to DataFrame
        nodes_data = json.loads(response)["nodes"]
        # save to temporary file
        temp_path = os.path.join(self.chapter_runtime_dir, "temp_nodes_list.csv")
        json.dump(nodes_data, open(temp_path, "w"), indent=4)
        
        self.new_nodes = pd.DataFrame(columns=["node_type", "node_name"])
        
        for node in nodes_data:
            node_name = node["node_name"]
            node_type = node["node_type"]
            self.new_nodes.loc[len(self.new_nodes)] = [node_type, node_name]
        
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
        # load chapter node list from first stage, and add it to self.existing_nodes
        chapter_node_list = pd.read_csv(os.path.join(self.chapter_runtime_dir, stage_names[0], "nodes_list.csv"), header=0)
        self.existing_nodes = pd.concat([self.existing_nodes, chapter_node_list], ignore_index=True)
        
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

    def extract_markdown_content(self, response: str) -> str:
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
            response = self.make_llm_call(system_prompt, user_input, stage_name=stage_names[1], node_name=node_name)
            if not response:
                continue
                
            # if there is a section in the response that goes with "```markdown{content}```"
            # extract the content and use this as the response
            node_md = self.extract_markdown_content(response)
            
            # Save output
            self.save_output(output_path, node_md, "md")
            print(f"Generated markdown saved to: {output_path}")
            
            # Wait for user verification
            if ask_for_verification:
                proceed = input("\nReview the generated markdown. Enter 'Y' to continue, and 'N' to abort: ")
                if proceed.upper() != 'Y':
                    print(f"Aborting pipeline execution early after stage 2 without verifying {node_name}.")
                    return False
                
        return True

    def process_attributes_text(self, attributes: str) -> str:
        attributes = attributes.strip()
        
        # remove first line if it start with "# " (remove the "# {node type} schema" line)
        if attributes.startswith("# "):
            attributes = attributes.split("\n", 1)[1]
            attributes = attributes.strip()
    
        # remove current first line if it is "## Attributes"
        if attributes.startswith("## Attributes"):
            attributes = attributes.split("\n", 1)[1]
            attributes = attributes.strip()
        return attributes
    
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
            attributes = ""
            
            json_schema = self.load_node_type_schema(node_type, "json")
            if not self.format_node_attributes:
                # remove schema/properties/attributes 
                del json_schema["schema"]["properties"]["attributes"]
                json_schema["schema"]["required"].remove("attributes")
                # remove the node_type
                del json_schema["schema"]["properties"]["node_type"]
                json_schema["schema"]["required"].remove("node_type")
                # check if the markdown_content contains "## Relationships"
                if "## Relationships" in markdown_content:
                    # cut the markdown_content and only provide the part regarding relationships
                    attributes, markdown_content = markdown_content.split("## Relationships")
                    attributes = self.process_attributes_text(attributes)
                    
                else:
                    attributes = self.process_attributes_text(markdown_content)
                    
                    dict = {
                        "attributes": attributes,
                        "relationships": ""
                    }
                    # node_json = json.dumps(dict)
                    self.save_output(output_path, dict, "json")
                    print(f"Generated JSON saved to: {output_path}")
                    continue
                
            system_prompt = """You will be provided with a markdown node on a statistical knowledge, and a JSON schema for the respective node type. Your task is to convert the markdown node to a JSON object according to the schema.
Note that you should not change the content corresponding to each subsection in the markdown node; and you should use the formatting for latex in markdown, that is, using $...$ for inline math and $$...$$ for display math."""
            user_input = {
                "markdown_node": markdown_content
            }
            
            response_format = {
                "type": "json_schema",
                "json_schema": json_schema,
            }
            
            response = self.make_llm_call(system_prompt, json.dumps(user_input), response_format, stage_name="md2json", node_name=node_name)
            node_json = json.loads(response)
            # add attributes to node_json
            node_json["attributes"] = attributes
            
            # save to runtime/stage2/node_type;node_name.json
            self.save_output(output_path, node_json, "json")
            print(f"Generated JSON saved to: {output_path}")
            
            # wait for user verification
            proceed = input("\nReview the generated JSON. Enter 'Y' to continue, and 'N' to abort: ")
            if proceed.upper() != 'Y':
                print(f"Aborting pipeline execution early after stage 2.5 without verifying {node_name}.")
                return False
        
        return True

    def stage3_add2neo4j(self) -> bool:
        """Stage 3: Convert markdown nodes to Cypher scripts"""
        print("\n=== Stage 3: Generating Cypher scripts ===")
        
        prompt = self.load_prompt(f"{stage_names[2]}_prompt.md")
        
        input_dir = self.chapter_runtime_dir / stage_names[1]
        if not input_dir.exists():
            print("Error: No markdown nodes from stage 2 found")
            return False
         
        relationships_cache = {}
        for markdown_file in input_dir.glob("*.md"):
            input_file_name = markdown_file.stem
            node_type, node_name = input_file_name.split(";")
            
            output_file_name = f"cypher;{input_file_name}"
            print(f"\nProcessing markdown file: {input_file_name}")
            output_path = self.get_output_path(stage_names[2], output_file_name, "json")
            
            # check if the node already exists
            node_exists, actual_node_name = check_node_exists(node_name, node_type)
            if node_exists:
                print(f"Node {node_name} already exists in database as {actual_node_name}")
                continue
                        
            # load the json file with same name if it exists
            json_file_path = self.get_output_path(stage_names[1], input_file_name, "json")
            if os.path.exists(json_file_path):
                print(f"Using json at {json_file_path}.")
                with open(json_file_path, 'r', encoding='utf-8') as f:
                    input_content = json.load(f)
            else:            
                # Read markdown content
                with open(markdown_file, "r", encoding="utf-8") as f:
                    input_content = f.read()
            
            print(f"Input content type: {type(input_content)}")
            # assuming json is loaded
            if not isinstance(input_content, dict):
                raise Exception(f"Error: Input content is not a dictionary for {input_file_name}")
        
            if "attributes" not in input_content:
                raise Exception(f"Error: 'attributes' is not a key in the input content for {input_file_name}")
                # continue
            attributes = input_content["attributes"]
            add_node(node_name, node_type, attributes)
            
            # check if "relationships" is a key in the dictionary
            if "relationships" not in input_content:
                raise Exception(f"Error: 'relationships' is not a key in the input content for {input_file_name}")
                # continue
                
            
            # cache relationships
            relationships = input_content["relationships"]
            relationships_cache[node_name] = {
                                                "node_type": node_type,
                                                "relationships": relationships,
                                            }
            
        
        # Match relationships
        unmatched_relations_cache = []
        for node_name, node_info in relationships_cache.items():
            node_type = node_info["node_type"]
            relationships = node_info["relationships"]
            
            for relationship_name in relationships:
                relationship = relationships[relationship_name]
                if not relationship:
                    continue
                assert "target_nodes" in relationship and "direction" in relationship
                target_nodes = relationship["target_nodes"]
                direction = relationship["direction"]
                
                for target_node_dict in target_nodes:
                    target_node = target_node_dict["target_node"]
                    target_node_name = target_node["target_node_name"]
                    target_node_type = target_node["target_node_type"]
                    print(f"Trying to add relation {relationship_name} from {node_name} to {target_node_name}")
                    node_exists, actual_target_node_name = check_node_exists(target_node_name, target_node_type)
                    if node_exists:
                        relationship_exists = check_relationship_exists(node_name, node_type, actual_target_node_name, target_node_type, relationship_name)
                        if relationship_exists:
                            print(f"\033[92mRelationship '{relationship_name}' already exists between '{node_name}' and '{actual_target_node_name}'\033[0m")
                        else:
                            add_relationship(source_node_name = node_name, source_node_type = node_type, 
                                             target_node_name = actual_target_node_name, target_node_type = target_node_type, 
                                             relationship_name = relationship_name, direction = direction)
                    else: # try to find a match in the existing nodes (note that the matching with existing node has already been done in stage 2 where the markdown nodes are generated)
                        # Filter existing nodes of the same type
                        
                        candidate_nodes = self.existing_nodes[
                            self.existing_nodes['node_type'] == target_node_type
                        ]['node_name'].tolist()
                        
                        if not candidate_nodes:
                            # No candidates found, add to unmatched cache
                            unmatched_relations_cache.append({
                                'source_node': node_name,
                                'source_type': node_type,
                                'target_node': target_node_name,
                                'target_type': target_node_type,
                                'relation': relationship_name
                            })
                            continue
                            
                        # Prepare LLM prompt
                        system_prompt = """You are tasked with finding whether a node that is an alias of the target node exist in a list of candidate nodes. You should return two fields in a JSON object:
                        - "matched_name": the matched node name if found, null if not found
                        Only return a match if you are highly confident it refers to the same concept."""
                        
                        user_input = {
                            "target_node": target_node_name,
                            "candidate_nodes": candidate_nodes,
                            "node_type": target_node_type
                        }
                        
                        response = self.make_llm_call(
                            system_prompt,
                            json.dumps(user_input),
                            response_format={"type": "json_object"},
                            stage_name="node_matching",
                            node_name=target_node_name
                        )
                        
                        if not response:
                            raise Exception(f"Error: Failed to get response from LLM for {target_node_name}")
                            continue
                            
                        result = json.loads(response)
                        match_result = result.get("matched_name")
                        if match_result:
                            # Add relation with matched node
                            add_relationship(
                                source_node_name=node_name,
                                source_node_type=node_type,
                                target_node_name=result["matched_name"],
                                target_node_type=target_node_type,
                                relationship_name=relationship_name,
                                direction=direction
                            )
                        else:
                            print(f"No match found for {target_node_name}")
                            # No match found, add to unmatched cache
                            unmatched_relations_cache.append({
                                'source_node': node_name,
                                'source_type': node_type,
                                'target_node': target_node_name,
                                'target_type': target_node_type,
                                'relationship_name': relationship_name
                            })
                
            
            check_recently_added_nodes_and_relations_script = """MATCH (n)
WHERE exists(n.created_at)
RETURN n
ORDER BY n.created_at DESC
LIMIT 10;
"""
            # proceed = input(f"\nReview the newly added nodes and relations. You can use the following script to check: \n{check_recently_added_nodes_and_relations_script}\nEnter 'Y' to continue: ")
            # if proceed.upper() != 'Y':
            #     return False
                
        return True
        

def main():
    
    # Get OpenAI API key and chapter information
    chapter_path = "Stat400_Concepts 09-30-2024/Stat400_Textbook/Chapter03.tex"
    
    # Initialize pipeline
    pipeline = KnowledgeGraphPipeline(chapter_path, rerun_cypher=True, source_name = "Stat400_Textbook", source_author = "Jonathan Fernandez")
    
    # Execute pipeline stages sequentially
    
    # print(f"\nExecuting Stage {1}...")
    # node_list = pipeline.stage1_generate_nodes_list()
    # print(node_list[:5])
    
    print(f"\nExecuting Stage {2}...")
    pipeline.stage2_generate_markdown_nodes()
    
    print(f"\nExecuting Stage {2.5}...")
    pipeline.stage2_5_markdown_to_json()
    
    print(f"\nExecuting Stage {3}...")
    pipeline.stage3_add2neo4j()
    
    print("\nPipeline execution completed")

if __name__ == "__main__":
    main() 
import pydantic_core, pydantic
import json

# read string from LLM assisted Knowledge Instantiation/runtime/Chapter03/context2node-md/concept;binomial distribution copy.json
with open("LLM assisted Knowledge Instantiation/runtime/Chapter03/context2node-md/concept;binomial distribution copy.json", "r") as f:
    data = f.read()

print(data[0:100])
json_data = json.loads(data)

print(type(json_data))

json_dict = json.loads(json_data)

print(type(json_dict))


json_str = json.dumps(json_dict, indent=4)

print(json_str)


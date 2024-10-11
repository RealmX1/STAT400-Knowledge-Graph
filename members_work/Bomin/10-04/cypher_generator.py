import re

# Read the markdown content from a file
with open('concept_nodes.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Initialize variables
concepts = []
current_concept = {}
lines = content.split('\n')
i = 0

while i < len(lines):
    line = lines[i].strip()
    if line.startswith('# '):  # New concept
        if current_concept:
            concepts.append(current_concept)
        current_concept = {
            'Name': line[2:].strip(),
            'Aliases': [],
            'Definition': '',
            'Notation': '',
            'Alias Notation': '',
            'Description': '',
            'Tags/Categories': [],
            'Properties': [],
            'Relationships': []
        }
        i += 1
    elif line.startswith('**Aliases**:'):
        aliases_line = line[len('**Aliases**:'):].strip()
        if aliases_line == 'None':
            current_concept['Aliases'] = []
        else:
            aliases = re.findall(r'\[([^\]]+)\]', aliases_line)
            if aliases:
                current_concept['Aliases'] = [alias.strip('" ') for alias in aliases[0].split(',')]
        i += 1
    elif line == '## Definition':
        i += 1
        # Read until the next section
        definition_lines = []
        while i < len(lines) and not lines[i].strip().startswith('## '):
            definition_lines.append(lines[i])
            i += 1
        definition_text = '\n'.join(definition_lines).strip()
        # Extract Notation, Description, Source
        notation_match = re.search(r'\*\*Notation\*\*:\s*(.*?)\n\n', definition_text, re.DOTALL)
        if notation_match:
            notation_text = notation_match.group(1).strip()
            current_concept['Notation'] = notation_text
            definition_text = definition_text.replace(notation_match.group(0), '')
        description_match = re.search(r'\*\*Description\*\*:\s*(.*?)\n\n', definition_text, re.DOTALL)
        if description_match:
            description_text = description_match.group(1).strip()
            current_concept['Description'] = description_text
            definition_text = definition_text.replace(description_match.group(0), '')
        source_match = re.search(r'\*\*Source\*\*:\s*(.*?)\n\n', definition_text, re.DOTALL)
        if source_match:
            source_text = source_match.group(1).strip()
            current_concept['Source'] = source_text
            definition_text = definition_text.replace(source_match.group(0), '')
        current_concept['Definition'] = definition_text.strip()
    elif line == '## Tags/Categories':
        i += 1
        tags = []
        while i < len(lines) and lines[i].strip() and not lines[i].startswith('## '):
            tag_line = lines[i].strip('- ')
            if tag_line:
                tags.append(tag_line)
            i += 1
        current_concept['Tags/Categories'] = tags
    elif line == '## Properties':
        i += 1
        properties = []
        while i < len(lines) and not lines[i].startswith('## '):
            prop_line = lines[i].strip()
            if prop_line.startswith('- **'):
                prop_name = prop_line[4:-2]
                i += 1
                formula_line = lines[i].strip()
                if formula_line.startswith('- Formula:'):
                    formula = formula_line[len('- Formula:'):].strip()
                    properties.append({'name': prop_name, 'formula': formula})
                else:
                    i -= 1  # Adjust index if formula not found
            i += 1
        current_concept['Properties'] = properties
    elif line == '## Relationships':
        i += 1
        relationships = []
        while i < len(lines) and not lines[i].startswith('# '):
            rel_line = lines[i].strip()
            if rel_line.startswith('- **'):
                rel_type_match = re.match(r'- \*\*(.+?)\*\*:', rel_line)
                if rel_type_match:
                    rel_type = rel_type_match.group(1)
                    rel_targets_line = rel_line[rel_line.find(':') + 1:].strip()
                    rel_targets = [t.strip() for t in rel_targets_line.strip('- ').split(',') if t.strip()]
                    if rel_targets:
                        relationships.append({'type': rel_type, 'targets': rel_targets})
                else:
                    # Handle multi-line targets
                    i += 1
                    while i < len(lines) and lines[i].startswith('  - '):
                        rel_targets_line = lines[i].strip('  - ')
                        if rel_targets_line.strip():
                            relationships[-1]['targets'].append(rel_targets_line.strip())
                        i += 1
                    continue
            i += 1
        current_concept['Relationships'] = relationships
    else:
        i += 1

# Append the last concept
if current_concept:
    concepts.append(current_concept)

# Now generate the Cypher script
cypher_statements = []

for idx_concept, concept in enumerate(concepts):
    # Create the concept node
    concept_name = concept['Name'].replace("'", "\\'")
    aliases = concept['Aliases']
    definition = concept['Definition'].replace("'", "\\'")
    description = concept['Description'].replace("'", "\\'")
    notation = concept['Notation'].replace("'", "\\'") if concept['Notation'] else ''
    tags = concept['Tags/Categories']
    source = concept.get('Source', '').replace("'", "\\'")

    # Merge concept node
    cypher = f"MERGE (c:Concept {{name: '{concept_name}'}})\n"

    # Set properties
    set_props = []
    if aliases:
        aliases_str = ', '.join([f"'{alias}'" for alias in aliases])
        set_props.append(f"c.aliases = [{aliases_str}]")
    if definition:
        set_props.append(f"c.definition = '{definition}'")
    if description:
        set_props.append(f"c.description = '{description}'")
    if notation:
        set_props.append(f"c.notation = '{notation}'")
    if tags:
        tags_str = ', '.join([f"'{tag}'" for tag in tags])
        set_props.append(f"c.tags = [{tags_str}]")
    if source:
        set_props.append(f"c.source = '{source}'")

    if set_props:
        cypher += f"SET {', '.join(set_props)}\n"

    # Add properties as separate nodes if needed
    for idx_prop, prop in enumerate(concept['Properties']):
        prop_name = prop['name'].replace("'", "\\'")
        formula = prop['formula'].replace("'", "\\'")
        prop_var = f"p{idx_concept}_{idx_prop}"
        # Merge property node
        cypher += f"MERGE ({prop_var}:Property {{name: '{prop_name}'}})\n"
        # Set formula
        cypher += f"SET {prop_var}.formula = '{formula}'\n"
        # Create relationship
        cypher += f"MERGE (c)-[:HAS_PROPERTY]->({prop_var})\n"

    # Add relationships
    for rel in concept['Relationships']:
        rel_type = rel['type']
        for idx_target, target in enumerate(rel['targets']):
            target_name = target.replace("'", "\\'")
            if not target_name:
                continue  # Skip empty target names
            rel_var = f"r{idx_concept}_{idx_target}"
            if rel_type.upper() == 'HAS_PROPERTY':
                # Properties are already handled
                continue
            elif rel_type.upper() == 'RELATED_TO':
                cypher += f"MERGE ({rel_var}:Concept {{name: '{target_name}'}})\n"
                cypher += f"MERGE (c)-[:RELATED_TO]->({rel_var})\n"
            elif rel_type.upper() == 'HAS_APPLICATION':
                # Applications might not be existing nodes, so we can create them
                cypher += f"MERGE ({rel_var}:Application {{name: '{target_name}'}})\n"
                cypher += f"MERGE (c)-[:HAS_APPLICATION]->({rel_var})\n"
            elif rel_type.upper() == 'INVOLVED_IN_THEOREM':
                cypher += f"MERGE ({rel_var}:Theorem {{name: '{target_name}'}})\n"
                cypher += f"MERGE (c)-[:INVOLVED_IN_THEOREM]->({rel_var})\n"
            else:
                # Other relationships can be handled similarly
                pass

    cypher_statements.append(cypher)

# Write the Cypher script to a file
with open('insert_concepts.cypher', 'w', encoding='utf-8') as f:
    for stmt in cypher_statements:
        f.write(stmt)
        f.write('\n')

print("Cypher script 'insert_concepts.cypher' has been generated.")

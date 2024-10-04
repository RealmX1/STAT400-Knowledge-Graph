LOAD CSV WITH HEADERS FROM 'file:///concepts_regex_blocks.csv' AS row
MERGE (c:Chapter {name: row.chapter_name})
MERGE (s:Section {name: row.section_name})
MERGE (c)-[:CONTAINS]->(s)

// Handle cases where subsection is present
FOREACH (_ IN CASE WHEN row.subsection_name IS NOT NULL THEN [1] ELSE [] END |
    MERGE (sub:Subsection {name: row.subsection_name})
    MERGE (s)-[:CONTAINS]->(sub)
    MERGE (block:Block {type: row.block_type, content: row.block_content})
    MERGE (sub)-[:CONTAINS]->(block)
)

// Handle cases where subsection is null (directly link block to section)
FOREACH (_ IN CASE WHEN row.subsection_name IS NULL THEN [1] ELSE [] END |
    MERGE (block:Block {type: row.block_type, content: row.block_content})
    MERGE (s)-[:CONTAINS]->(block)
)

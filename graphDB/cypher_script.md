LOAD CSV WITH HEADERS FROM 'file:///concepts_regex_blocks.csv' AS row
MERGE (c:Chapter {name: row.chapter_name})
MERGE (s:Section {name: row.section_name})
MERGE (c)-[:CONTAINS]->(s)

// Handle cases where subsection is present
FOREACH (_ IN CASE WHEN row.subsection_name IS NOT NULL THEN [1] ELSE [] END |
    MERGE (sub:Subsection {name: row.subsection_name})
    MERGE (s)-[:CONTAINS]->(sub)
    
    // Create Definition Block if block_type is 'definition'
    FOREACH (_ IN CASE WHEN row.block_type = 'definition' THEN [1] ELSE [] END |
        MERGE (block:Definition {content: row.block_content})
        MERGE (sub)-[:CONTAINS]->(block)
    )
    
    // Create Example Block if block_type is 'example'
    FOREACH (_ IN CASE WHEN row.block_type = 'example' THEN [1] ELSE [] END |
        MERGE (block:Example {content: row.block_content})
        MERGE (sub)-[:CONTAINS]->(block)
    )

    // Create Theorem Block if block_type is 'theorem'
    FOREACH (_ IN CASE WHEN row.block_type = 'theorem' THEN [1] ELSE [] END |
        MERGE (block:Theorem {content: row.block_content})
        MERGE (sub)-[:CONTAINS]->(block)
    )

    // Create Proof Block if block_type is 'proof'
    FOREACH (_ IN CASE WHEN row.block_type = 'proof' THEN [1] ELSE [] END |
        MERGE (block:Proof {content: row.block_content})
        MERGE (sub)-[:CONTAINS]->(block)
    )

    // Create GeneralDescription Block if block_type is 'general description'
    FOREACH (_ IN CASE WHEN row.block_type = 'general description' THEN [1] ELSE [] END |
        MERGE (block:GeneralDescription {content: row.block_content})
        MERGE (sub)-[:CONTAINS]->(block)
    )
)

// Handle cases where subsection is null (directly link block to section)
FOREACH (_ IN CASE WHEN row.subsection_name IS NULL THEN [1] ELSE [] END |

    // Create Definition Block if block_type is 'definition'
    FOREACH (_ IN CASE WHEN row.block_type = 'definition' THEN [1] ELSE [] END |
        MERGE (block:Definition {content: row.block_content})
        MERGE (s)-[:CONTAINS]->(block)
    )
    
    // Create Example Block if block_type is 'example'
    FOREACH (_ IN CASE WHEN row.block_type = 'example' THEN [1] ELSE [] END |
        MERGE (block:Example {content: row.block_content})
        MERGE (s)-[:CONTAINS]->(block)
    )

    // Create Theorem Block if block_type is 'theorem'
    FOREACH (_ IN CASE WHEN row.block_type = 'theorem' THEN [1] ELSE [] END |
        MERGE (block:Theorem {content: row.block_content})
        MERGE (s)-[:CONTAINS]->(block)
    )

    // Create Proof Block if block_type is 'proof'
    FOREACH (_ IN CASE WHEN row.block_type = 'proof' THEN [1] ELSE [] END |
        MERGE (block:Proof {content: row.block_content})
        MERGE (s)-[:CONTAINS]->(block)
    )

    // Create GeneralDescription Block if block_type is 'general description'
    FOREACH (_ IN CASE WHEN row.block_type = 'general description' THEN [1] ELSE [] END |
        MERGE (block:GeneralDescription {content: row.block_content})
        MERGE (s)-[:CONTAINS]->(block)
    )
)

### Procedure for manually modeling nodes:
1. Pull the latest version of our repo from github.
2. Make a copy of the folder `\node_schemas\md_schemas\` in your folder in this repo at `\members_work\<name>\` for saving your edit on schema. Skim through the schemas in it to get a general idea on
    - What types of nodes exist and 
    - What types of properties and relations each type of node models.
    - Remember that by no means this schema is the final version/definitive. Make your suggestion on modification by modifying your copy of the schema.
3. Read through assigned section in text book; 
    1. todo so, upload the `Stat400_Concepts.zip` file to overleaf. I've already asked Fernandes to add you guys (so that you have access to the original overleaf project) multiple times but he still hasn't done it yet, so this is the next best solution.
    2. for each section, start with each section's topic as a main node itself, and
        1.  Make another copy of the respective node schema ane rename it as `node_name;node_type`, for example, `discrete_uniform_distribution;concept`; also make a copy of `\meeting log\manual-modeling-prompt.md`.
        2.  When reading through it, 
            1.  copy down all the attributes and relationships to the `<context>` section of your copy of `manual-modeling-prompt.md` (or simply copy the entire section or even chapter, and scrutinize after LLM finish processing)
            2.  Logdown potential nodes (other than the section topics) for later modeling.
        3.  Copy the selected schema to `<schema>` section of your copy of `manual-modeling-prompt.md`. Run the prompt with LLM, and scrutinize the output. (remember to replace the `{topic}` and `{chapter_name}` in the prompt.)
            1.  Ofcourse you can also simply fillout the schema completely by hand. shouldn't be too much more work as compared to the above suggested method.
        4.  <u>Scrutinize the output with respect to textbook and online sources, especially the *italisized* parts (LLM is instructed to provide additional information in italicized text), and repeat the process of copy and run until the output is satisfactory.</u>
            1.  Mark sources different from textbook using a <source>source</source> tag before the content, after the formatting (`-`)
        5.  Log down your modification of the schema and the prompt in a .
        6.  Conclude the modeled node and add it to your folder.
    3. Continue with non-section topic nodes previously logged down in `3.2.2.2`; perform basically the same process as you do with the section main topics.

I'd automate all steps above other than manual scrutinization later after we do this for one or two weeks.
# gpt4-books
Code and data to support "Speak, Memory: An Archaeology of Books Known to ChatGPT/GPT-4"

This work probes what books GPT-4 and ChatGPT have memorized by assessing the degree to which models are able to predict the masked token (a proper name) in name cloze passages like the following:

> Though of a very ingenious mechanical turn, [MASK] could never get this table to suit him. He put chips under it, blocks of various sorts, bits of pasteboard, and at last went so far as to attempt an exquisite adjustment by final pieces of folded blotting paper.


## Full results

Full name cloze accuracy results (GPT-4, ChatGPT and BERT) for all books can be found here: [gpt4-books](https://docs.google.com/spreadsheets/d/1jW7EhsNjIGDMoK2JidyDD7UXH9N0NpEJfWFEj05_LC4/edit?usp=sharing).

## Generating name cloze passages

To generate name cloze passages for your own texts, see the [generate\_name\_cloze](https://github.com/bamman-group/gpt4-books/tree/main/generate_name_cloze) folder.
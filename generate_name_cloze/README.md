# Creating name cloze examples

A name cloze passage in our study is between 40-60 words long, where the original text contains exactly one PER named entity (a single token long) and no other named entities.  That name is replaced by the token "[MASK]".  Here's one example:

> Though of a very ingenious mechanical turn, [MASK] could never get this table to suit him. He put chips under it, blocks of various sorts, bits of pasteboard, and at last went so far as to attempt an exquisite adjustment by final pieces of folded blotting paper.

Here, the original name, "Nippers", has been replaced with "[MASK]".

`create_name_cloze.sh` provides an example for how to create name cloze passages for an input text.  The process involves running [BookNLP](https://github.com/booknlp/booknlp) on the text to tokenize it and extract entities; and then identifying passages that meet the criteria outlined above (for length and number of entities).

Run with on the sample text provided with:

`./create_name_cloze.sh 11231_bartleby.txt 11231_bartleby`

In this script, BookNLP files and the name cloze examples are all saved to `booknlp_output/11231_bartleby/`

The name cloze output is tab-separated, where each row (a name cloze passage) has the following columns:

* book id (the second argument to the script above)
* passage length in tokens
* BookNLP token ID of masked token
* BookNLP token ID of start token for passage
* BookNLP token ID of end token for passage
* The masked entity token
* The passage, with [MASK] replacing the masked entity token


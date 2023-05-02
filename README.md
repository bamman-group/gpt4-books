# gpt4-books
Code and data to support the following paper:

Kent K. Chang, Mackenzie Cramer, Sandeep Soni and David Bamman (2023), "[Speak, Memory: An Archaeology of Books Known to ChatGPT/GPT-4](https://arxiv.org/abs/2305.00118)", ArXiv.  

This work probes what books GPT-4 and ChatGPT have memorized by assessing the degree to which models are able to predict the masked token (a proper name) in name cloze passages like the following:

> Though of a very ingenious mechanical turn, [MASK] could never get this table to suit him. He put chips under it, blocks of various sorts, bits of pasteboard, and at last went so far as to attempt an exquisite adjustment by final pieces of folded blotting paper.

Detailed results on all books can be found here: [gpt4-books](https://docs.google.com/spreadsheets/d/1jW7EhsNjIGDMoK2JidyDD7UXH9N0NpEJfWFEj05_LC4/edit?usp=sharing).

## Generating name cloze passages

To generate name cloze passages for your own texts, see the [generate\_name\_cloze](https://github.com/bamman-group/gpt4-books/tree/main/generate_name_cloze) folder.


## 100 most memorized books

The following books in our set have the highest GPT-4 name cloze accuracy (where accuracy here is the fraction of times a model predicts the masked name exactly right in 100 passages from a book). Full name cloze accuracy results (GPT-4, ChatGPT and BERT) for all books can be found here: [gpt4-books](https://docs.google.com/spreadsheets/d/1jW7EhsNjIGDMoK2JidyDD7UXH9N0NpEJfWFEj05_LC4/edit?usp=sharing).

|GPT-4 Accuracy|ChatGPT Accuracy|BERT Accuracy|Year|Author|Title|
|---|---|---|---|---|---|
|0.98|0.82|0.00|1865|Lewis Carroll|Alice's Adventures in Wonderland|
|0.76|0.43|0.00|1997|J.K. Rowling|Harry Potter and the Sorcerer's Stone|
|0.74|0.29|0.00|1850|Nathaniel Hawthorne|The Scarlet Letter|
|0.72|0.11|0.00|1892|Arthur Conan Doyle|The Adventures of Sherlock Holmes|
|0.70|0.10|0.00|1815|Jane Austen|Emma|
|0.65|0.19|0.00|1823|Mary Wollstonecraft Shelley|Frankenstein; Or, The Modern Prometheus|
|0.62|0.13|0.00|1813|Jane Austen|Pride and Prejudice|
|0.61|0.18|0.00|1838|Charles Dickens|Oliver Twist|
|0.61|0.30|0.00|1853|Herman Melville|Bartleby, the Scrivener: A Story of Wall-Street|
|0.61|0.35|0.00|1884|Mark Twain|Adventures of Huckleberry Finn|
|0.61|0.08|0.00|1897|Bram Stoker|Dracula|
|0.59|0.22|0.00|1851|Herman Melville|Moby Dick; Or, The Whale|
|0.59|0.13|0.00|1902|Arthur Conan Doyle|The Hound of the Baskervilles|
|0.58|0.35|0.00|1876|Mark Twain|The Adventures of Tom Sawyer|
|0.57|0.30|0.00|1949|George Orwell|1984|
|0.54|0.10|0.00|1908|L. M. Montgomery|Anne of Green Gables|
|0.51|0.20|0.01|1954|J.R.R. Tolkien|The Fellowship of the Ring|
|0.49|0.16|0.13|2012|E.L. James|Fifty Shades of Grey|
|0.49|0.16|0.00|1847|Charlotte Brontë|Jane Eyre: An Autobiography|
|0.49|0.12|0.00|1883|Robert Louis Stevenson|Treasure Island|
|0.49|0.22|0.00|1903|Jack London|The Call of the Wild|
|0.49|0.24|0.01|1911|Frances Hodgson Burnett|The Secret Garden|
|0.48|0.14|0.00|2008|Suzanne Collins|The Hunger Games|
|0.47|0.20|0.01|1916|James Joyce|A Portrait of the Artist as a Young Man|
|0.45|0.09|0.00|1847|Emily Brontë|Wuthering Heights|
|0.45|0.10|0.01|1868|Louisa May Alcott|Little Women|
|0.43|0.27|0.00|1954|William Golding|Lord of the Flies|
|0.43|0.17|0.00|1979|Douglas Adams|The Hitchhiker's Guide to the Galaxy|
|0.42|0.08|0.00|1890|Oscar Wilde|The Picture of Dorian Gray|
|0.42|0.03|0.00|1898|Henry James|The Turn of the Screw|
|0.41|0.20|0.00|1912|Edgar Rice Burroughs|Tarzan of the Apes|
|0.40|0.06|0.00|1861|Charles Dickens|Great Expectations|
|0.37|0.06|0.00|1897|H. G. Wells|The Invisible Man: A Grotesque Romance|
|0.36|0.02|0.02|1914|James Joyce|Dubliners|
|0.34|0.05|0.00|1849|Charles Dickens|David Copperfield|
|0.33|0.02|0.01|1794|Ann Ward Radcliffe|The Mysteries of Udolpho|
|0.30|0.16|0.00|1959|Chinua Achebe|Things Fall Apart|
|0.28|0.12|0.00|1977|J. R. R. Tolkien and Christopher Tolkien|The Silmarillion|
|0.28|0.09|0.00|1922|James Joyce|Ulysses|
|0.27|0.13|0.00|1953|Ray Bradbury|Fahrenheit 451|
|0.27|0.13|0.00|1996|George R.R. Martin|A Game of Thrones|
|0.26|0.05|0.01|2003|Dan Brown|The Da Vinci Code|
|0.26|0.08|0.00|1965|Frank Herbert|Dune|
|0.25|0.20|0.01|1937|Zora Neale Hurston|Their Eyes Were Watching God|
|0.25|0.04|0.00|1851|Nathaniel Hawthorne|The House of the Seven Gables|
|0.25|0.03|0.00|1861|George Eliot|Silas Marner|
|0.25|0.01|0.00|1920|Edith Wharton|The Age of Innocence|
|0.25|0.14|0.00|1961|Harper Lee|To Kill a Mockingbird|
|0.24|0.03|0.03|1953|Ian Fleming|Casino Royale|
|0.24|0.00|0.00|1915|W. Somerset (William Somerset) Maugham|Of Human Bondage|
|0.23|0.09|0.00|1891|Thomas Hardy|Tess of the d'Urbervilles: A Pure Woman|
|0.23|0.05|0.00|1903|Henry James|The Ambassadors|
|0.22|0.13|0.00|1984|William Gibson|Neuromancer|
|0.22|0.00|0.00|1885|H. Rider (Henry Rider) Haggard|King Solomon's Mines|
|0.21|0.02|0.00|1900|Theodore Dreiser|Sister Carrie: A Novel|
|0.20|0.10|0.00|1985|Orson Scott Card|Ender's Game|
|0.20|0.03|0.00|1852|Charles Dickens|Bleak House|
|0.20|0.04|0.00|1877|Anna Sewell|Black Beauty|
|0.19|0.12|0.00|1932|Aldous Huxley|Brave New World|
|0.19|0.07|0.00|1826|James Fenimore Cooper|The Last of the Mohicans; A narrative of 1757|
|0.19|0.06|0.00|1868|Wilkie Collins|The Moonstone|
|0.19|0.00|0.00|1922|F. Scott (Francis Scott) Fitzgerald|The Beautiful and Damned|
|0.18|0.05|0.00|1855|Elizabeth Cleghorn Gaskell|North and South|
|0.18|0.04|0.00|1905|Emmuska Orczy, Baroness Orczy|The Scarlet Pimpernel|
|0.18|0.07|0.00|1937|Margaret Mitchell|Gone with the Wind|
|0.17|0.05|0.00|1968|Philip K. Dick|Do Androids Dream of Electric Sheep?|
|0.17|0.03|0.00|1848|Anne Brontë|The Tenant of Wildfell Hall|
|0.17|0.08|0.00|1908|E. M. (Edward Morgan) Forster|A Room with a View|
|0.16|0.06|0.05|2009|Dan Brown|The Lost Symbol|
|0.16|0.02|0.01|1848|William Makepeace Thackeray|Vanity Fair|
|0.16|0.03|0.00|1871|George Eliot|Middlemarch|
|0.16|0.05|0.01|1879|Henry James|Daisy Miller: A Study|
|0.15|0.04|0.04|2013|Dan Brown|Inferno|
|0.15|0.08|0.01|2014|Veronica Roth|Divergent|
|0.15|0.07|0.00|1899|Kate Chopin|The Awakening, and Selected Short Stories|
|0.15|0.03|0.00|1903|Samuel Butler|The Way of All Flesh|
|0.15|0.04|0.00|1940|John Steinbeck|The Grapes of Wrath|
|0.14|0.00|0.00|1913|D. H. (David Herbert) Lawrence|Sons and Lovers|
|0.13|0.05|0.00|1983|James Kahn|Return of the Jedi|
|0.13|0.02|0.01|1928|D. H. Lawrence|Lady Chatterley's Lover|
|0.13|0.01|0.00|1749|Henry Fielding|History of Tom Jones, a Foundling|
|0.13|0.04|0.00|1818|Jane Austen|Persuasion|
|0.13|0.03|0.00|1977|Alex Haley|Roots|
|0.12|0.02|0.00|1874|Thomas Hardy|Far from the Madding Crowd|
|0.11|0.11|0.00|1961|Irving Stone|The Agony and the Ecstasy|
|0.11|0.01|0.03|1957|Ian Fleming|From Russia with Love|
|0.11|0.04|0.00|1962|Madeleine L'Engle|A Wrinkle in Time|
|0.11|0.04|0.01|1939|Marjorie Kinnan Rawlings|The Yearling|
|0.10|0.05|0.00|1975|E. L. Doctorow|Ragtime|
|0.10|0.05|0.00|1929|Dashiell Hammett|The Maltese Falcon|
|0.10|0.08|0.07|1991|Diana Gabaldon|Outlander|
|0.10|0.02|0.00|1989|Kazuo Ishiguro|The Remains of the Day|
|0.10|0.05|0.00|1898|Elizabeth Von Arnim|Elizabeth and Her German Garden|
|0.10|0.00|0.00|1915|Charlotte Perkins Gilman|Herland|
|0.10|0.01|0.00|1983|Alice Walker|The Color Purple|
|0.09|0.02|0.00|1934|Dorothy L. Sayers|The Nine Tailors|
|0.09|0.03|0.00|1985|Margaret Atwood|The Handmaid's Tale|
|0.09|0.01|0.00|1778|Fanny Burney|Evelina, Or, the History of a Young Lady's Entrance into the World|
|0.09|0.02|0.00|1896|Sarah Orne Jewett|The Country of the Pointed Firs|
|0.09|0.04|0.00|1988|Toni Morrison|Beloved|

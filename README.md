# Few Shot Learning and Syntactic Invariance for Neural LMs


All the neural LMs are trained on the Wall Street Journal portion of the Penn Treebank.

### invar_item_generation

A python notebook for generating the test items used to test the neural LMs. There are two ways to generate the argument structure tests `generate_argstruct_tests` generates tests for both past-tense and infinitive verbs, whereas `generate_argstruct_tests_vbd` generates tests for only past-tense verbs.

Files are saved in the `/test_items_downsample` directory.

### /test_items_downsample/

Directory where the test items are stored after generation (these are `csv` files that end in `tests`).

Also stored in this directory are the outputs of the varios models on the tests. Models were run seperatly. The results for the `number` tests have an extra set of results `pp`, which include a prepositional phrase distractor and were generated after the base tests.

### data_wrangling.rmd

This file reads in all the model outputs stored in the `test_items_downsample` directory and combines them into two files: `argstruct_data.csv` and `number_data.csv`. These are the main results files.

This file harmonizes each verb with a number of their usage statistics: The number of times it occurs as each POS tag, as well as the number of times it takes an object, as well as a passive subject.

### invar_analysis.Rmd

This file is the main analysis script of the project. It reads in teh `argstruct_data.csv` and `number_data.csv`, analyzes them and generates images in the `images` folder.


### /data/

• `wsj_deps.conllu` contains the PTB portion of the penn treebank turned into dependency parses, using the tools found here: https://nlp.stanford.edu/software/stanford-dependencies.shtml

•`v_counts.csv`: every token with a VBD, VBN or VB tag, its lemma POS and the number of times it occurs in the corpus. This can be useufl for choosing open-class items in creating the sentences.

•`wsj_proportions.csv`: for each verb, this gives the counts of the number of times it occurs with a passive subject and object. This information is used in `data_wrangling.rmd` to track what proportion of the time it takes an object.

• `extract_verb_proportions.py` generates `wsj_proportions.csv`

•`filter.csv` a list of verbs that are the same in passive participle and past tense, which are the only verbs we want to use for the argstruct learning experiment.

### /vbd_only/

This is a seperate folder where we do analysis for the transformation tests for the argstruct learning. This folder is much like the `test_items_downsample` folder, except it also contains an analysis script `vbd_only_analysis.Rmd` that does a seperate analysis for these tests.


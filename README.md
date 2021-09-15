# Urmi morphological analyzer

This is a rule-based morphological analyzer for Christian Urmi (Afro-Asiatic > North-Eastern Neo-Aramaic). It is based on a formalized description of Urmi morphology and uses [uniparser-morph](https://github.com/timarkh/uniparser-morph) for parsing. It performs full morphological analysis of Urmi words (lemmatization, POS tagging, grammatical tagging). The text to be analyzed should be written in the Latin-based alphabet (the Assyrian New Alphabet).

## How to use
### Python package
The analyzer is available as a Python package. If you want to analyze Urmi texts in Python, install the module:

```
pip3 install uniparser-urmi
```

Import the module and create an instance of ``UrmiAnalyzer`` class. Set ``mode='strict'`` if you are going to process text in standard Assyrian New Alphabet, or ``mode='nodiacritics'`` if you expect some words to lack the diacritics (e.g. *t* instead of *ṭ*). After that, you can either parse tokens or lists of tokens with ``analyze_words()``, or parse a frequency list with ``analyze_wordlist()``. Here is a simple example:

```python
from uniparser_urmi import UrmiAnalyzer
a = UrmiAnalyzer(mode='strict')

analyses = a.analyze_words('вajjannux')
# The parser is initialized before first use, so expect
# some delay here (usually several seconds)

# You will get a list of Wordform objects
# The analysis attributes are stored in its properties
# as string values, e.g.:
for ana in analyses:
        print(ana.wf, ana.lemma, ana.gramm)

# You can also pass lists (even nested lists) and specify
# output format ('xml', 'json' or 'conll')
# If you pass a list, you will get a list of analyses
# with the same structure
analyses = a.analyze_words([['вajjannux'], ['Ptixli', 'tarra', 'd', 'xə', 'вetə', '.']],
	                       format='xml')
analyses = a.analyze_words([['вajjannux'], ['Ptixli', 'tarra', 'd', 'xə', 'вetə', '.']],
	                       format='conll')
analyses = a.analyze_words(['вajjannux', [['вəxtə'], ['Ptixli', 'tarra', 'd', 'xə', 'вetə', '.']]],
	                       format='json')
```

Refer to the [uniparser-morph documentation](https://uniparser-morph.readthedocs.io/en/latest/) for the full list of options.

If you want to quickly check an analysis for one particular word, you can also use the command-line interface. Here is an example for the word *вajjannux*:

```
python3 -m uniparser_urmi вajjannux
```

<!---
### Disambiguation
Apart from the analyzer, this repository contains a set of [Constraint Grammar](https://visl.sdu.dk/constraint_grammar.html) rules that can be used for partial disambiguation of analyzed Urmi texts. If you want to use them, set ``disambiguation=True`` when calling ``analyze_words``:

```python
analyses = a.analyze_words(['Ptixli', 'tarra', 'd', 'xə', 'вetə', '.'], disambiguate=True)
```

In order for this to work, you have to install the ``cg3`` executable separately. On Ubuntu/Debian, you can use ``apt-get``:

```
sudo apt-get install cg3
```

On Windows, download the binary and add the path to the ``PATH`` environment variable. See [the documentation](https://visl.sdu.dk/cg3/single/#installation) for other options.

Note that each time you call ``analyze_words()`` with ``disambiguate=True``, the CG grammar is loaded and compiled from scratch, which makes the analysis even slower. If you are analyzing a large text, it would make sense to pass the entire text contents in a single function call rather than do it sentence-by-sentence, for optimal performance.
-->

### Word lists
Alternatively, you can use a preprocessed word list. The ``wordlists`` directory contains a list of words from a 622-thousand-word [Christian Urmi corpus](https://neo-aramaic.web-corpora.net/index_en.html) (``wordlist.csv``) with 63,000 unique tokens, list of analyzed tokens (``wordlist_analyzed.txt``; each line contains all possible analyses for one word in an XML format), and list of tokens the parser could not analyze (``wordlist_unanalyzed.txt``). The recall of the analyzer on the corpus texts is about 76%.

## Description format
The description is carried out in the ``uniparser-morph`` format and involves a description of the inflection (paradigms.txt) and a grammatical dictionary (lexemes.txt). The dictionary contains descriptions of individual lexemes, each of which is accompanied by information about its stem, its part-of-speech tag and some other grammatical information, its consonant root, its inflectional type (paradigm), and English and/or Russian translations. See more about the format [in the uniparser-morph documentation](https://uniparser-morph.readthedocs.io/en/latest/format.html).

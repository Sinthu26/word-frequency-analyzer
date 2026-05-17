# Word Frequency Analyzer

This program is a command line tool that analyzes a text file and reports the most common words, sentence count, average word length, and other statistics. Built with Python and the NLTK natural language toolkit.

## Features

- Countrs total characters, words, and unique words
- Filters out English stop words using NLTK
- Identifies the top N most common words with frequency counts
- Computes average word length and finds the longest word
- Counts sentences using regex-based splitting

## Setup

Clone the repository and install dependencies:

```bash
git clone git@github.com:your-username/word-frequency-analyzer.git
cd word-frequency-analyzer
pip3 install -r requirements.txt
```

The first run will automatically download the NLTK stopwords corpus if it's not already installed on your machine.

## Usage

```bash
python3 analyzer.py
```

When running the program, you will be prompted to enter the path to a text file and it will provide all the information relevant to the text file.

## What I learned

Although this a simple project, it has deepened my understanding of several Python concepts:

- **The `collections.Counter` class** for frequency counting, which is more elegant than rolling your own dictionary
- **Generator expressions vs list comprehensions** — when each is appropriate
- **Regex (`re` module)** for splitting on multiple delimiters
- **The `max(iterable, key=...)` pattern** for finding extremes by a computed property
- **Single-source-of-truth design** — preprocessing data once and reusing it across multiple analyses
- **Integrating third-party libraries** (NLTK) with graceful fallback when data isn't downloaded

## Future Improvements

- Add support for multiple input files
- Generate word frequency visualizations using matplotlib
- Export results to JSON or CSV
- Support custom stop word lists via command-line argument
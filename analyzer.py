import re
import string
from collections import Counter

import nltk

try:
    from nltk.corpus import stopwords
    STOP_WORDS = set(stopwords.words("english"))
except LookupError:
    nltk.download("stopwords", quiet=True)
    from nltk.corpus import stopwords
    STOP_WORDS = set(stopwords.words("english"))


def load_text(filepath):
    """Read a text file and return its content as a single string."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def clean_word(word):
    """Strip punctuation from a word and convert to lowercase."""
    return word.strip(string.punctuation).lower()


def preprocess(text):
    """Return a list of cleaned, meaningful words from the text."""
    cleaned = (clean_word(w) for w in text.split())
    return [w for w in cleaned if w and w not in STOP_WORDS]


def count_sentences(text):
    """Count sentences by splitting on . ! ? punctuation."""
    sentences = re.split(r"[.!?]+", text)
    return len([s for s in sentences if s.strip()])


def display_top_words(word_counts, n=10):
    """Print the top N most common words with their counts."""
    print(f"\nTop {n} most common words:")
    print("-" * 30)
    for rank, (word, count) in enumerate(word_counts.most_common(n), start=1):
        print(f"{rank:>3}. {word:<15} {count}")


if __name__ == "__main__":
    filepath = input("Enter the path to a text file: ").strip()
    text = load_text(filepath)
    words = preprocess(text)

    print(f"\nTotal characters: {len(text)}")
    print(f"Total words: {len(text.split())}")
    print(f"Meaningful words: {len(words)}")
    print(f"Unique meaningful words: {len(set(words))}")
    print(f"Average word length: {sum(len(w) for w in words) / len(words):.2f}")
    print(f"Longest word: {max(words, key=len)}")
    print(f"Sentences: {count_sentences(text)}")

    display_top_words(Counter(words), n=10)
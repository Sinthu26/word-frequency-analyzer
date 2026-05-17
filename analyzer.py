import string
import nltk
from nltk.corpus import stopwords
from collections import Counter
import re

stop_words = stopwords.words('english')

def load_text(filepath):
    """Read a text file and return its content as a single string."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()
    
def clean_word(word):
    """Strip punctuation from a word and convert to lowercase."""
    return word.strip(string.punctuation).lower()

def get_word_counts(text):
    """Returns a dictionary of word frequencies from the given text."""
    words = text.split()
    cleaned = [clean_word(w) 
               for w in words 
               if clean_word(w) and clean_word(w) not in stop_words]
    return Counter(cleaned)

def get_sentences(text):
    """Returns the amount of sentences splitting on . , ! , ?"""
    sentences = re.split(r'[.!?]+', text)
    num_sentences = len([s for s in sentences if s.strip()])
    return num_sentences
    
def get_unique_word_count(text):
    """Return the number of unique words in the text."""
    words = text.split()
    cleaned = {clean_word(w) for w in words if clean_word(w)}
    return len(cleaned)

def display_top_words(word_counts, n=10):
    """Print the top N most common words with their counts."""
    print(f"\nTop {n} most common words: ")
    print("-" * 30)
    for rank, (word, count) in enumerate(word_counts.most_common(n), start=1):
        print(f"{rank:>3}. {word:<15} {count}")

def average_word_length(text):
    """Return the average length of words in the text ignoring punctuation."""
    cleaned = [clean_word(w) for w in text.split() if clean_word(w)]
    if not cleaned:
        return 0
    return sum(len(w) for w in cleaned) / len(cleaned)
    
def longest_word(text):
    """Finds the longest word in the text file."""
    words = text.split()
    if not words:
        return None
    return max(words, key=len)

if __name__ == "__main__":
    filepath = input("Enter the path to a text file: ").strip()
    text = load_text(filepath)
    
    print(f"\nTotal characters: {len(text)}")
    print(f"Total words: {len(text.split())}")
    print(f"Unique words: {get_unique_word_count(text)}")
    print(f"Average Word Length: {average_word_length(text)}")
    print(f"Number of Sentences: {get_sentences(text)}")
    print(f"Longest word in text: {longest_word(text)}")

    counts = get_word_counts(text)
    display_top_words(counts, n=10)    
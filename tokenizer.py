import string
from collections import Counter

def clean_text(text):
    """
    Cleans the input text by converting it to lowercase and removing punctuation.
    
    Parameters:
    text (str): The input text to clean.
    
    Returns:
    str: The cleaned text with all lowercase words and no punctuation.
    """
    # Validate input type
    assert isinstance(text, str), "Input must be a string"
    
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    return text

def tokenize(text):
    """
    Tokenizes the input text into a list of words.
    
    Parameters:
    text (str): The input text to tokenize.
    
    Returns:
    list: A list of words from the input text.
    """
    # Validate input type
    assert isinstance(text, str), "Input must be a string"
    
    # Clean text to remove punctuation and make lowercase
    text = clean_text(text)
    
    # Split the text into words
    words = text.split()
    
    return words

def count_words(text):
    """
    Counts the occurrences of each word in the input text.
    
    Parameters:
    text (str): The input text to count words in.
    
    Returns:
    dict: A dictionary where keys are words and values are their counts.
    """
    # Validate input type
    assert isinstance(text, str), "Input must be a string"
    
    # Tokenize the text into words
    words = tokenize(text)
    
    # Count word occurrences
    word_count = Counter(words)
    
    return dict(word_count)


# fmh7pv__DS5111su24_lab_01
# pkg_fmh7pv

A Python package with utility functions for processing and analyzing text.

## Features

- **clean_text**: Cleans the input text by removing unnecessary characters.
- **tokenize**: Splits the text into a list of words.
- **count_words**: Counts the number of words in the text.

## Installation

You can install the package directly from GitHub using `pip`:

```bash
pip install git+https://github.com/fmh7pv/fmh7pv__DS5111su24_lab_01.git
```

```python
from pkg_fmh7pv.example import clean_text, tokenize, count_words

text = "Hello world!"
clean = clean_text(text)  # "Hello world"
tokens = tokenize(clean)  # ['Hello', 'world']
count = count_words(clean)  # 2

print(f"Cleaned text: {clean}")
print(f"Tokens: {tokens}")
print(f"Word count: {count}")
```

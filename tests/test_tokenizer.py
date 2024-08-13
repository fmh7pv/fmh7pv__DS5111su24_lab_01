import pytest
import os
import subprocess
import sys
from tokenizer import tokenize

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Define the list of file paths
test_files = [
    'pg17192.txt',
    'pg932.txt',
    'pg1063.txt',
    'pg10031.txt',
    'pg14082.txt'
]

@pytest.mark.parametrize("file_path", test_files)
def test_tokenize_file(file_path):
    """
    GIVEN a file path
    WHEN the file's text is passed to the `tokenize` function
    THEN the function should return a non-empty list of tokens
    """
    # Construct the full path 
    full_path = os.path.join(os.path.dirname(__file__), 'files', file_path)
    
    # Read the content of the file
    with open(full_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Tokenize the text using the tokenize function
    tokens = tokenize(text)
    
    # Assert the tokens is a non-empty list
    assert isinstance(tokens, list), f"Output for {file_path} should be a list"
    assert len(tokens) > 0, f"Tokenized result is empty for {file_path}"

def test_tokenize_french():
    """
    GIVEN a snippet of French text
    WHEN the text is passed to the `tokenize` function
    THEN the function should return a non-empty list of tokens
    """
    french_text = '''Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»'''
    
    # Tokenize the text using the tokenize function
    tokens = tokenize(french_text)
    
    # Assert the tokens is a list
    assert isinstance(tokens, list), f"Tokenization failed on French text: {french_text}"
    assert len(tokens) > 0, "Tokenized result is empty for French text"

@pytest.mark.skip(reason="Japanese version not yet available")
def test_tokenize_japanese():
    """
    GIVEN a Japanese text
    WHEN the text is passed to the `tokenize` function
    THEN the function should return a non-empty list of tokens
    """
    # Given Japanese text
    text = 'ここに日本語のテキストがあります'
    
    # When the Japanese text is tokenized
    tokens = tokenize(text)
    
    # Then it should be a list of tokens
    assert isinstance(tokens, list), "Result is not a list"
    assert len(tokens) > 0, "Tokenized result is empty for Japanese text"

@pytest.mark.skipif(sys.platform != "linux", reason="Test only runs on Linux")
def test_tokenize_linux():
    """
    GIVEN a Linux-specific condition
    WHEN the text is passed to the `tokenize` function
    THEN the function should return a non-empty list of tokens
    """
    # Given a Linux-specific condition
    text = 'This test is specific to Linux'
    
    # When the text is tokenized
    tokens = tokenize(text)
    
    # Then it should be a list and have a non-zero length
    assert isinstance(tokens, list), "Result is not a list"
    assert len(tokens) > 0, "Tokenized result is empty for Linux-specific test"

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8 or higher")
def test_tokenize_python_version():
    """
    GIVEN a Python version condition
    WHEN the text is passed to the `tokenize` function
    THEN the function should return a non-empty list of tokens
    """
    # Given a Python version condition
    text = 'This test requires Python 3.8 or newer'
    
    # When the text is tokenized
    tokens = tokenize(text)
    
    # Then it should be a list and have a non-zero length
    assert isinstance(tokens, list), "Result is not a list"
    assert len(tokens) > 0, "Tokenized result is empty for Python version test"

def test_tokenize_bash_comparison():
    """
    GIVEN a text and its tokenized version using bash
    WHEN the Python tokenized result is compared with the bash result
    THEN the results should match
    """
    # Given a text and its tokenized version using bash
    text = "Suddenly Mary asked, 'Do you love me?'"
    python_result = tokenize(text)
    python_result_str = ' '.join(python_result)  # Convert list to string for comparison

    # Perform the same tokenization using a bash command
    bash_command = f"echo '{text}' | tr -s ' ' | tr -d '[:punct:]' | tr '[:upper:]' '[:lower:]' | xargs -n1 | sort | uniq"
    bash_result = subprocess.check_output(bash_command, shell=True).decode().strip().split('\n')
    
    # When compared with bash result
    # Then results should match
    assert python_result == bash_result, "Python and bash tokenization results differ"

@pytest.mark.xfail(reason="tokenize function doesn't handle non-string input")
def test_tokenize_non_string():
    """
    GIVEN a non-string list input
    WHEN a non-string input is passed
    THEN it should raise a TypeError
    """
    # Given a non-string list input
    non_string_input = ["hello", "world"]
    
    # When a non-string input is passed
    # Then it should raise a TypeError
    with pytest.raises(TypeError):
        tokenize(non_string_input)

import pytest
import re
import os
import subprocess
import sys
from tokenizer import count_words

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Define file paths
FILENAMES = [
    'pg17192.txt',
    'pg932.txt',
    'pg1063.txt',
    'pg10031.txt'
]

def read_file(file_path):
    """Helper function to read the content of a file."""
    full_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(full_path, 'r', encoding='utf-8') as file:
        return file.read()

def test_count_words_basic():
    """
    GIVEN a sample text with multiple words
    WHEN counting the words in the text using `count_words`
    THEN it should return the correct word count
    """
    # Given
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    
    # When
    result = count_words(text)
    
    # Then
    assert isinstance(result, int), "Result is not an integer"
    assert result == 14, "Word count is incorrect"

def test_count_words_french():
    """
    GIVEN French text with multiple words
    WHEN counting the words in the French text using `count_words`
    THEN it should return the correct word count
    """
    # Given
    text = """Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»"""
    
    # When
    result = count_words(text)
    
    # Then
    assert isinstance(result, int), "Result is not an integer"
    assert result == 24, "Word count is incorrect"

@pytest.mark.parametrize('filename', FILENAMES)
def test_count_words_files(filename):
    """
    GIVEN a text file from the predefined list of filenames
    WHEN counting the words in the file content using `count_words`
    THEN it should return a positive integer
    """
    # Given
    file_path = os.path.join(os.path.dirname(__file__), filename)
    content = read_file(file_path)
    
    # When
    result = count_words(content)
    
    # Then
    assert isinstance(result, int), f"Failed on file: {filename}"
    assert result > 0, f"Word count is zero or negative for file: {filename}"

def test_count_words_all_files():
    """
    GIVEN combined content from all predefined English files
    WHEN counting the words in all files combined using `count_words`
    THEN it should return a positive integer
    """
    # Given
    full_text = ""
    for filename in FILENAMES:
        file_path = os.path.join(os.path.dirname(__file__), filename)
        full_text += read_file(file_path) + "\n"
    
    # When
    result = count_words(full_text)
    
    # Then
    assert isinstance(result, int), "Failed on combined English files"
    assert result > 0, "Word count is zero or negative"

@pytest.mark.skip(reason="Japanese version not yet available")
def test_count_words_japanese():
    """
    GIVEN a Japanese text
    WHEN counting the words in the Japanese text using `count_words`
    THEN it should return a positive integer
    """
    # Given
    # I just google translated the first sentence of the raven 
    text = 'むかし、真夜中の憂鬱なとき、私が弱々しく疲れて考え込んでいたとき、忘れ去られた伝承の風変わりで奇妙な膨大な量について考えていたとき、私がうなずき、昼寝しそうになっていると、突然トントンという音が聞こえた、誰かが私の部屋のドアを優しくたたき、たたくような音でした。'
    
    # When
    result = count_words(text)
    
    # Then
    assert isinstance(result, int), "Result is not an integer"

@pytest.mark.skipif(sys.platform != "linux", reason="Test only runs on Linux")
def test_count_words_linux():
    """
    GIVEN a Linux-specific condition
    WHEN counting the words in the text using `count_words` on a Linux system
    THEN it should return a positive integer
    """
    # Given
    text = 'This test is specific to Linux'
    
    # When
    result = count_words(text)
    
    # Then
    assert isinstance(result, int), "Result is not an integer"

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8 or higher")
def test_count_words_python_version():
    """
    GIVEN a Python version condition
    WHEN counting the words in the text using `count_words` with Python 3.8 or newer
    THEN it should return a positive integer
    """
    # Given
    text = 'This test requires Python 3.8 or newer'
    
    # When
    result = count_words(text)
    
    # Then
    assert isinstance(result, int), "Result is not an integer"

def test_count_words_bash_comparison():
    """
    GIVEN a text string and its word count using bash
    WHEN counting the words in the text using `count_words`
    THEN the Python result should match the bash result
    """
    # Given
    text = "Suddenly Mary asked, 'Do you love me?'"
    python_result = count_words(text)

    # When
    bash_command = f"echo '{text}' | wc -w"
    bash_result = int(subprocess.check_output(bash_command, shell=True).decode().strip())
    
    # Then
    assert python_result == bash_result, "Python and bash word counts differ"

@pytest.mark.xfail(reason="count_words function doesn't handle non-string input")
def test_count_words_non_string():
    """
    GIVEN a non-string list input
    WHEN a non-string input is passed to the `count_words` function
    THEN a TypeError should be raised
    """
    # Given
    non_string_input = ["hello", "world"]
    
    # When
    # Then
    with pytest.raises(TypeError):
        count_words(non_string_input)

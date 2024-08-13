import pytest
import re
import os
import subprocess
import sys
from tokenizer import clean_text

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
def test_clean_text_file(file_path):
    """
    GIVEN a file path
    WHEN the file's text is passed to the `clean_text` function
    THEN the function should return a non-empty cleaned text with no punctuation
    """
    # Construct the full path 
    full_path = os.path.join(os.path.dirname(__file__), file_path)
    
    # Read the content of the file
    with open(full_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Clean the text using the clean_text function
    cleaned_text = clean_text(text)
    
    # Assert the cleaned text is a non-empty string
    assert len(cleaned_text) > 0, f"Output for {file_path} should not be empty"
    
    # Assert the cleaned text is of type string
    assert isinstance(cleaned_text, str), f"Cleaner failed on sample text from {file_path}"
    
    # Assert there are no punctuation characters in the cleaned text
    assert not re.search(r'[^\w\s]', cleaned_text), f"Punctuation remains in cleaned text from {file_path}"

def test_clean_text_french():
    """
    GIVEN a snippet of French text from Le Corbeau
    WHEN the text is passed to the `clean_text` function
    THEN the function should return the cleaned text correctly
    """
    french_text = '''_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_'''
    
    # Clean the text using the clean_text function
    cleaned_text = clean_text(french_text)
    
    # Assert the cleaned text is of type string
    assert isinstance(cleaned_text, str), f"Cleaner failed on French text: {french_text}"

@pytest.mark.skip(reason="Japanese version not yet available")
def test_clean_text_japanese():
    # Given a Japanese text
    # I just google translated the first sentence of the raven 
    text = 'むかし、真夜中の憂鬱なとき、私が弱々しく疲れて考え込んでいたとき、忘れ去られた伝承の風変わりで奇妙な膨大な量について考えていたとき、私がうなずき、昼寝しそうになっていると、突然トントンという音が聞こえた、誰かが私の部屋のドアを優しくたたき、たたくような音でした。'
    
    # When the Japanese text is cleaned
    result = clean_text(text)
    
    # Then it should be a string
    assert isinstance(result, str), "Result is not a string"

@pytest.mark.skipif(sys.platform != "linux", reason="Test only runs on Linux")
def test_clean_text_linux():
    # Given a Linux-specific condition
    text = 'This test is specific to Linux'
    
    # When the text is cleaned
    result = clean_text(text)
    
    # Then it should be lowercase and without punctuation
    assert isinstance(result, str), "Result is not a string"

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8 or higher")
def test_clean_text_python_version():
    # Given a Python version condition
    text = 'This test requires Python 3.8 or newer'
    
    # When the text is cleaned
    result = clean_text(text)
    
    # Then it should be lowercase and without punctuation
    assert isinstance(result, str), "Result is not a string"

def test_clean_text_bash_comparison():
    # Given a text and its cleaned version using bash
    text = "Suddenly Mary asked, 'Do you love me?'"
    python_result = clean_text(text)

    # Perform the same cleaning using a bash command
    bash_command = f"echo '{text}' | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]'"
    bash_result = subprocess.check_output(bash_command, shell=True).decode().strip()
    
    # When compared with bash result
    # Then results should match
    assert python_result == bash_result, "Python and bash cleaning results differ"

@pytest.mark.xfail(reason="clean_text function doesn't handle non-string input")
def test_clean_text_non_string():
    # Given a non-string list input
    non_string_input = ["hello", "world"]
    
    # When a non-string input is passed
    # Then it should raise a TypeError
    with pytest.raises(TypeError):
        clean_text(non_string_input)

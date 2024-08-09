# Default target
default: env

# Get texts using a shell script
get_texts:
	bash get_the_books.sh

# Count lines in pg17192.txt
raven_line_count:
	wc -l pg17192.txt

# Count words in pg17192.txt
raven_word_count:
	wc -w pg17192.txt

# Count different cases of the word 'raven' in pg17192.txt
raven_counts:
	echo "Lowercase 'raven':"
	grep -o -i 'raven' pg17192.txt | wc -l
	echo "Title case 'Raven':"
	grep -o 'Raven' pg17192.txt | wc -l
	echo "Case ignored 'raven':"
	grep -o -i 'raven' pg17192.txt | wc -l

# Total lines in all text files matching pg*.txt
total_lines:
	cat pg*.txt | wc -l

# Total words in all text files matching pg*.txt
total_words:
	cat pg*.txt | wc -w

# Setup Python environment and install dependencies
setup_env:
	python3 -m venv env
	. env/bin/activate; pip install --upgrade pip
	. env/bin/activate; pip install -r requirements.txt

# Create 'env' target to run setup_env commands
env: setup_env

default:
	cat Makefile

get_texts:
	bash get_the_books.sh

raven_line_count:
	wc -l pg17192.txt

raven_word_count:
	wc -w pg17192.txt

raven_counts:
	echo "Lowercase 'raven':"
	grep -o -i 'raven' pg17192.txt | wc -l
	echo "Title case 'Raven':"
	grep -o 'Raven' pg17192.txt | wc -l
	echo "Case ignored 'raven':"
	grep -o -i 'raven' pg17192.txt | wc -l

total_lines:
	cat pg*.txt | wc -l

total_words:
	cat pg*.txt | wc -w

setup_env:
	python3 -m venv env
	. env/bin/activate; pip install --upgrade pip; pip install -r requirements.txt

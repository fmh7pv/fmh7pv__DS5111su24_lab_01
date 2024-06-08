.DEFAULT_GOAL := default

default:
        cat Makefile

get_texts: get_the_books.sh
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

.PHONY: default get_texts raven_line_count raven_word_count

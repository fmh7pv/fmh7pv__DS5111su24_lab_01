book_ids=(
2147  # Volume 1
2148  # Volume 2
2149  # Volume 3
2150  # Volume 4 
2151  # Volume 5
1063  # The Cask of Amontillado
932    # The Fall of the House of Usher
1064  # The Masque of the Red Death
32037  # Eureka: A Prose Poem
1065 # The Raven) 

for id in "${book_ids[@]}"; do
        wget "https://www.gutenberg.org/cache/epub/$id/pg$id.txt"
done

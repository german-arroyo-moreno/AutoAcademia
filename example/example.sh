#!/bin/sh

dir="$(dirname "$(realpath "$0")")"
tex="$dir/tex"
html="$dir/html"

# LaTeX
"$dir/../"academia.py "$dir/"list_publications.txt -hd "$tex/"header.txt -ft "$tex/"footer.txt -t "$tex/"template.txt -rules "$tex/"rules.txt -o /tmp/paper.tex --mode tex --reverse-sort-by "year"

#HTML
"$dir/../"academia.py "$dir/"list_publications.txt -hd "$html/"header.txt -ft "$html/"footer.txt -t "$html/"template.txt -rules "$html/"rules.txt -o /tmp/index.html --reverse-sort-by "year"


#HTML only journals
"$dir/../"academia.py "$dir/"list_publications.txt -hd "$html/"header.txt -ft "$html/"footer.txt -t "$html/"template.txt -rules "$html/"rules.txt -o /tmp/journals.html --reverse-sort-by "year" --filter-by '$journal is not None'

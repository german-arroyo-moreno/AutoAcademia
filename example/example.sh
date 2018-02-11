#!/bin/sh

# LaTeX
../academia.py example/list_publications.txt -hd example/tex/header.txt -ft example/tex/footer.txt -t example/tex/template.txt -rules example/tex/rules.txt -o /tmp/paper.tex --mode tex

#HTML
../academia.py example/list_publications.txt -hd example/html/header.txt -ft example/html/footer.txt -t example/html/template.txt -rules example/html/rules.txt -o /tmp/index.html

# AutoAcademia

*Have you ever despaired of filling hundreds of resumes by copying the list of publications and projects over and over again?*

This software allows you to save a considerable amount of time by replacing a list of publications, projects, etc. by means of a template. 
The software allows you to insert a header and a footer, and it is able to deal with regular expressions to eliminate fields that are not used.

An example is provided in the folder **example** for LaTeX and HTML output.

A good start point is installing python3 (no other dependencies are required).
The execute from your favourite console and some help will be displayed:

*python3 academia.py --help*

**
usage: academia.py [-h] [-hd HEADER] [-ft FOOTER] [-t TEMPLATE] [-tk TOKENS]
                   [-rules PRERERULES] [--append] [-o OUTPUT] [-m {plain,tex}]
                   [-c]
                   text_file

positional arguments:
  text_file             File given as input with a formated list of works.

optional arguments:
  -h, --help            show this help message and exit
  -hd HEADER, --header HEADER
                        A file with the header.
  -ft FOOTER, --footer FOOTER
                        A file with the footer.
  -t TEMPLATE, --template TEMPLATE
                        A file with the template.
  -tk TOKENS, --tokens TOKENS
                        A file with the tokens separated by commas ','.
  -rules PRERERULES, --preReRules PRERERULES
                        A file with regular expressions to replace empty
                        tokens.
  --append              Force to append text to the output, default is
                        overwrite.
  -o OUTPUT, --output OUTPUT
                        An output file.
  -m {plain,tex}, --mode {plain,tex}
                        Replacement mode.
  -c, --colors          For terminals with colors.
**
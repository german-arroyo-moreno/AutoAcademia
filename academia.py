#!/usr/bin/env python3
# coding: utf-8

""" Author: Germán Arroyo """

""" Esta herramienta permite convertir desde un formato simple en txt
a bibtex, o a latex. """

# Note that:
# After you run bibtex, you can copy the contents of the .bbl
# file into your document.


import argparse,sys

from AutoAcademicCV import Parser
from AutoAcademicCV import openListFile
from AutoAcademicCV import openTxtFile
from AutoAcademicCV import saveTxtFile

parser = argparse.ArgumentParser()
parser.add_argument("text_file", help="File given as input with a formated list of works.", type=str)
parser.add_argument("-hd", "--header", help="A file with the header.", type=str)
parser.add_argument("-ft", "--footer", help="A file with the footer.", type=str)
parser.add_argument("-t", "--template", help="A file with the template.", type=str)
parser.add_argument("-tk", "--tokens",
                    help="A file with the tokens separated by commas ','.",
                    type=str)
parser.add_argument("-rules", "--preReRules",
                    help="A file with regular expressions to replace empty tokens.",
                    type=str)
parser.add_argument("--append",
                    help="Force to append text to the output, default is overwrite.",
                    action="store_true")
parser.add_argument("-o", "--output", help="An output file.", type=str)
parser.add_argument("-m", "--mode", help="Replacement mode.",
                    choices=["plain", "tex"])
parser.add_argument("-c", "--colors", help="For terminals with colors.", action="store_true")

args = parser.parse_args()

if args.tokens is not None:
    token_list = openListFile(args.tokens)
else:
    token_list = []

p = Parser(mode=args.mode, token_list=token_list, colors=args.colors)
p.parse(args.text_file)

if args.preReRules is not None:
    p.regularExpr(args.preReRules)

if args.header is not None:
    header_text = openTxtFile(args.header)
else:
    header_text = ""

if args.footer is not None:
    footer_text = openTxtFile(args.footer)
else:
    footer_text = ""

if args.template is not None:
    template_text = openTxtFile(args.template)
    out_text = p.template(header_text=header_text,
                          footer_text=footer_text,
                          template_text=template_text)
    if args.output:
        saveTxtFile(args.output, out_text, args.append)
        print("File '" + args.output + "' saved.")
    else:
        print(out_text)
else:
    template_text = ""
    # Print the works if no template is given
    ret = "\r\n"
    if args.template is None:
        out_text = ""
        out_text += ret
        out_text += "No template so, WORKS are:" + ret + ret
        line = 0
        for work in p.works:
            line += 1
            out_text += " - Work #" + str(line) + ":" + ret
            for field in sorted(work):
                out_text += "   " + str(field) + " --> " + str(work[field]) + ret
            out_text += ret
        out_text += ret
        if args.output:
            saveTxtFile(args.output, out_text, not args.overwrite)
            print("File '" + args.output + "' saved.")
        else:
            print(out_text)
        sys.exit(0)

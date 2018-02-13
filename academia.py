#!/usr/bin/env python3
# coding: utf-8

"""

Copyright 2018 (c) Germán Arroyo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

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
parser.add_argument("--sort-by",
                    help="Sort the works following a list of fields separated by comma ','",
                    type=str)
parser.add_argument("--reverse-sort-by",
                    help="Sort the works following a list of fields separated by comma ',' in reverse order.",
                    type=str)
parser.add_argument("--filter-by",
                    help="Filter the output to that works that fulfill the given expression.",
                    type=str)
parser.add_argument("-mod", "--module",
                    help="Load a given file as a module that is executed in python as a function that return a dictionary, a work. The only parameters of the function are: a dictionary (work), its index in the list (index_work), and the complete list (works)..",
                    type=str)


args = parser.parse_args()

if args.tokens is not None:
    token_list = openListFile(args.tokens)
else:
    token_list = []

p = Parser(mode=args.mode, token_list=token_list, colors=args.colors)

p.parse(args.text_file,filterby=args.filter_by)

if args.module is not None:
    p.execMod(args.module)

if args.sort_by is not None or args.reverse_sort_by is not None:
    if args.reverse_sort_by is not None:
        raw_fields = args.reverse_sort_by.split(",")
        rev = True
    else:
        rev = False
        raw_fields = args.sort_by.split(",")
    fields = []
    [fields.append(f.strip()) for f in raw_fields]
    p.sort(fields, rev)

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

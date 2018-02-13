# encoding: utf-8

"""

Copyright 2018 (c) Germán Arroyo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""


import sys

def openFile(fileName):
    """
    " Open a file or exit of the program,
    " return the handler of the file
    """
    try:
        finput = open(fileName, 'r')
    except IOError:
        print("Error loading file '" + fileName + "'. ABORT.")
        sys.exit(-1)
    return finput

def openTxtFile(fileName):
    """
    " Open a file or exit of the program,
    " return the text of the file
    """
    try:
        finput = open(fileName, 'r')
    except IOError:
        print("Error loading text file '" + fileName + "'. ABORT.")
        sys.exit(-1)
    text = finput.read()
    finput.close()
    return text

def openLinesTxtFile(fileName):
    """
    " Open a file or exit of the program,
    " return a list of lines of text of the file
    """
    try:
        finput = open(fileName, 'r')
    except IOError:
        print("Error loading text file '" + fileName + "'. ABORT.")
        sys.exit(-1)
    text = finput.readlines()
    finput.close()
    return text


def saveTxtFile(fileName, text, append=False):
    """
    " Open a file or exit of the program,
    " return the text of the file
    """
    try:
        if append:
            foutput = open(fileName, 'a')
        else:
            foutput = open(fileName, 'w')
    except IOError:
        print("Error loading text file '" + fileName + "'. ABORT.")
        sys.exit(-1)
    foutput.write(text)
    foutput.close()
    return



def openListFile(fileName, delim=','):
    """
    " Open a file or exit of the program,
    " return a list separated by delim
    """
    try:
        finput = open(fileName, 'r')
    except IOError:
        print("Error loading text file '" + fileName + "'. ABORT.")
        sys.exit(-1)
    text = finput.read()
    listT = text.split(delim)
    listT = [item.replace('\n', '').replace('\r','').strip() for item in listT]
    finput.close()
    return listT


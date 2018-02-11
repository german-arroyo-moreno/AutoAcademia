# encoding: utf-8

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


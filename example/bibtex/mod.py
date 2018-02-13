import os
import sys, re
from sys import exit
# input parameters are: work, index_work, works

# work is a dictionary with all the defined fields
# index_work is some unique number for each work
# works is a list with all the elements in the dictonary

# This module create a new field named idtex that contains the index of the bibtex paper
if work["authors"] is not None:
	authors=work["authors"].split(",")
	surname = authors[0].strip().split()[-1]
	# remove accents in LaTeX format:
	surname = re.sub(r"[\{\}\'\\]", "", surname)
	year=work["year"]
	work['idtex'] = surname + ":" + year + ":" + str(index_work + 1)
exit(1)
return work



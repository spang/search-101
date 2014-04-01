import sys

from whoosh.index import open_dir

import IPython

try:
    ix = open_dir('ex_index')
    print "{} documents in index `ix`".format(ix.doc_count())

    r = ix.reader()

    IPython.embed(banner1="""
Got index reader in `r`.

Play around with the contents of the index!
See http://pythonhosted.org/Whoosh/api/reading.html for help.
""")
except OSError:
    print >>sys.stderr, "Can't find index in 'ex_index'. Create it first!"

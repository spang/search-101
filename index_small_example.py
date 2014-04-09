#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
from __future__ import unicode_literals

import os

from whoosh import index
from whoosh.fields import Schema, ID, TEXT

# Ultra-simple example index.

schema = Schema(id=ID(unique=True), content=TEXT)

docs = [u"Ce matin j'ai boivé un café.",
        u"I've been emailing all day long.",
        u"http://www.python.org/",
        u"I love Python!",
        u"I never want to send another email ever again.",
        u"Email email email. Sooo many emails.",
        ]

INDEX_DIR = "ex_index"

if not os.path.exists(INDEX_DIR):
    os.mkdir(INDEX_DIR)

if index.exists_in(INDEX_DIR):
    ix = index.open_dir(INDEX_DIR)
    print "updating existing index in '{}'".format(INDEX_DIR)
else:
    ix = index.create_in(INDEX_DIR, schema)
    print "creating index in '{}'".format(INDEX_DIR)
writer = ix.writer()

for i, d in enumerate(docs):
    print "processing document {0}; document contents: {1}".format(i, d)
    writer.update_document(id=unicode(i), content=d)
writer.commit()

print "done!"

#!/usr/bin/env python
import os
import json

from datetime import datetime
from glob import glob

from whoosh import index
from whoosh.fields import Schema, ID, TEXT, DATETIME

schema = Schema(id=ID(unique=True), title=TEXT(stored=True),
                author=TEXT(stored=True), release_date=DATETIME, language=TEXT,
                content=TEXT)

INDEX_DIR = "index"

if not os.path.exists(INDEX_DIR):
    os.mkdir(INDEX_DIR)

if index.exists_in(INDEX_DIR):
    ix = index.open_dir(INDEX_DIR)
    print "updating existing index in '{}'".format(INDEX_DIR)
else:
    ix = index.create_in(INDEX_DIR, schema)
    print "creating index in '{}'".format(INDEX_DIR)
writer = ix.writer()

for filename in glob('gutentexts/*.json'):
    print "processing", filename
    data = json.load(file(filename, 'r'), encoding='utf-8')
    data['release_date'] = datetime.fromtimestamp(int(data['release_date']))
    writer.update_document(**data)
writer.commit()

print "done!"

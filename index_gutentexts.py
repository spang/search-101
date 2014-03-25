#!/usr/bin/env python
import json

from datetime import datetime
from glob import glob

from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, DATETIME

schema = Schema(title=TEXT(stored=True), author=TEXT(stored=True),
                release_date=DATETIME, language=TEXT, content=TEXT)
ix = create_in("indexdir", schema)
writer = ix.writer()

# load documents: each document is a meta dict, plus add the 'content' field
# pointing to the text. also we have to make sure to decode the text properly.
for filename in glob('gutentexts/*.json'):
    data = json.load(file(filename, 'r'), encoding='utf-8')
    data['release_date'] = datetime.fromtimestamp(int(data['release_date']))
    writer.add_document(**data)
writer.commit()

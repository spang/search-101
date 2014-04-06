import os
import sys

from whoosh.qparser import QueryParser
from whoosh.index import open_dir

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

INDEX_DIR = 'gutenindex'


@app.route("/")
def index():
    return render_template('index.html')


def _search(q):
    """ Returned search results are ordered by score (highest first.) """
    ix = open_dir(INDEX_DIR)
    print "{} documents in index".format(ix.doc_count())

    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(q)
        results = [i.fields() for i in searcher.search(query)]
    return results


@app.route('/_search', methods=['GET'])
def search():
    q = request.args.get('query')
    results = _search(q)
    print "found {} matches:".format(len(results))
    print results
    return jsonify({'results': results})


if __name__ == "__main__":
    if not os.path.exists(INDEX_DIR):
        print >>sys.stderr, \
            "Can't find index, run `python index_gutentexts.py` first."
        sys.exit(1)
    # enable reloading on code changes
    app.debug = True
    app.run()

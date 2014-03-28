from whoosh.qparser import QueryParser
from whoosh.index import open_dir

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


def _search(q):
    """ Returned search results are ordered by score (highest first.) """
    ix = open_dir('index')
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
    app.run()

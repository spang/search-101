Search 101: An Introduction to Information Retrieval
====================================================

Hi, and welcome to the introductory Python search tutorial airing at PyCon 2014
in Montreal!

# How to get set up

If you don't already have Python installed and your preferred text editor
up and running, refer to the [Boston Python
Workshop](https://openhatch.org/wiki/Boston_Python_Workshop_6/Friday)
installation instructions for Windows, Mac, and Linux. *Note that this
tutorial currently only supports Python 2.7. Patches for Python 3 support
accepted, but unless you want to do that, please make sure to use Python
2.7!*

In addition to Python 2.7 and your favourite text editor, you should install
[virtualenv](http://www.virtualenv.org/) on your machine using `pip install
virtualenv` (Mac and Linux users will need to prefix the command with `sudo`,
or Linux users can install using your distro's package manager, `sudo apt-get
install python-virtualenv` on Debian/Ubuntu.)

From there:

* `git clone https://github.com/spang/search-101.git`
* `cd search-101`
* `virtualenv .`
* `source bin/activate`
* `pip install -r requirements.txt`

As our main search corpus, we'll be using a subset of public domain ebooks
from [Project Gutenberg](http://www.gutenberg.org/). You'll want to
pregenerate the search index for this corpus before you show up, since it
takes a few minutes to run:

* `python extract_metadata.py && python index_gutentexts.py`

If this works, you should then be ready to go!

# The handout

We've provided a digital copy of the paper handout in the form of an IPython
notebook. You can run it locally by running this command in this folder:

    ipython notebook --pylab inline

It will print out something like:

    2014-04-01 16:45:04.834 [NotebookApp] The IPython Notebook is running at: http://127.0.0.1:8888/

You can then access the handout by opening up `http://127.0.0.1:8888/` in
your browser.

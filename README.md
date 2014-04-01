Search 101: An Introduction to Information Retrieval
====================================================

Hi, and welcome to the search tutorial airing at PyCon 2014 in Montreal!

# How to get set up

If you don't already have Python installed and your preferred text editor
up and running, refer to the [Boston Python
Workshop](https://openhatch.org/wiki/Boston_Python_Workshop_6/Friday)
installation instructions for Windows, Mac, and Linux.

In addition to Python and your favourite text editor, you should install
[http://www.virtualenv.org/](http://www.virtualenv.org/) virtualenv on
your machine using `pip install virtualenv` (Mac and Linux users will need to
prefix the command with `sudo`, or Linux users can install using your distro's
package manager, `sudo apt-get install python-virtualenv` on Debian/Ubuntu.)

From there:

* `git clone https://github.com/spang/search-101.git`
* `cd search-101`
* `virtualenv .`
* `source bin/activate`
* `pip install -r requirements.txt`

You should then be ready to go!

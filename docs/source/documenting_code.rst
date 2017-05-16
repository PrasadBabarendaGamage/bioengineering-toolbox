****************
Documenting code
****************

.. toctree::
   :maxdepth: 2

.. TEMPLATE: `link <link>`_

*restructuredText* is a lightweight markup language (file format) that is
commonly used to create documentation. The langauge is designed to be both:
(a) processable by documentation-processing software such as Docutils, and
(b) easily readable by human programmers who are reading and writing source
code.

See this `link <http://rest-sphinx-memo.readthedocs.io/en/latest/ReST.html>`_
for a guide to the rst file format.

To find out about the differences between reST, docutils, readthedocs,
sphinx, and extensions, see this `link <http://www.git-pull.com/code_explorer/rst-docutils-sphinx-readthedocs.html#rest-docutils-sphinx-readthedocs>`_.

`Sphinx: force rebuild of html, including autodoc <http://stackoverflow.com/questions/21019505/sphinx-force-rebuild-of-html-including-autodoc>`_
-----------------------------------------------------------------------

  .. code-block:: python

    html -E -a


`Table width fix for Read the Docs Sphinx theme <http://rackerlabs.github.io/docs-rackspace/tools/rtd-tables.html>`_
-----------------------------------------------------------------------


`My ReadTheDocs project isn’t building <http://docs.readthedocs.io/en/latest/faq.html#my-project-isn-t-building-with-autodoc>`_

First, you should check out the Builds tab of your project. That records all
of the build attempts that RTD has made to build your project. If you see
``ImportError`` messages for custom Python modules, you should enable the
virtualenv feature in the Admin page of your project, which will install your
project into a virtualenv, and allow you to specify a ``requirements.txt`` file
 for your project.

You can create this file using the following steps

.. note::

   The following steps assume you have successfully built the Sphinx
   documentation on your local machine (i.e. that all the required modules
   are installed on your machine).

Open the conf.py of your sphinx documentation (usually located inside the
``docs`` folder), and navigate to the extensions section (an example of
which  is shown below)

  .. code-block:: python

   # Add any Sphinx extension module names here, as strings. They can be
   # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
   # ones.
   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.doctest',
       'sphinx.ext.intersphinx',
       'sphinx.ext.todo',
       'sphinx.ext.coverage',
       'sphinx.ext.imgmath',
       'sphinx.ext.viewcode',
       'sphinxcontrib.bibtex'
   ]

The Extensions (or in other words - the python modules) that inbuilt into
Sphinx are denoted by ``the sphinx.`` prefix. The other python modules will
need to be installed when ReadTheDocs builds the documentation on their server.

To see what python modules are currently installed on your machine use the
following command in a terminal:

  .. code-block:: bash

   pip freeze > requirements.txt

Search in this file for the items that match the other python modules
required by ReadTheDocs (in the example above, search for ``sphinxcontrib``)
.  Move these lines to the top of the file and delete the remaining lines.

Move the ``requirements.txt`` file in the documentation directory of
your repository (commonly labelled ``docs``).

Add the location of this file
to the ReadTheDocs project admin page and rebuild the documentation on
ReadTheDocs.
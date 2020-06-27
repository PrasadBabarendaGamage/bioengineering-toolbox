*******************
ReST and Sphinx FAQ
*******************

.. toctree::
   :maxdepth: 2

.. TEMPLATE: `link <link>`_

*restructuredText* is a lightweight markup language (file format) that is
commonly used to create documentation. The langauge is designed to be both:
(a) processable by documentation-processing software such as Docutils, and
(b) easily readable by human programmers who are reading and writing source
code.

See these links for a guide to the rst file format.

- `guide <http://rest-sphinx-memo.readthedocs.io/en/latest/ReST.html>`_
- `cheatsheet <https://docs.typo3.org/m/typo3/docs-how-to-document/master/en-us/WritingReST/CheatSheet.html>`_

To find out about the differences between reST, docutils, readthedocs,
sphinx, and extensions, see this `link <http://www.git-pull.com/code_explorer/rst-docutils-sphinx-readthedocs.html#rest-docutils-sphinx-readthedocs>`_.

`Guide to setting up a sphinx project <https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html>`_.
---------------------------------------------

Examples of well documented code repositories
---------------------------------------------

- http://libcellml.readthedocs.io/
- http://morphic.readthedocs.io/

`Sphinx: force rebuild of html, including autodoc <http://stackoverflow.com/questions/21019505/sphinx-force-rebuild-of-html-including-autodoc>`_
-----------------------------------------------------------------------

  .. code-block:: python

    html -E -a


`Table width fix for Read the Docs Sphinx theme <http://rackerlabs.github.io/docs-rackspace/tools/rtd-tables.html>`_
-----------------------------------------------------------------------

Inline code block with syntax highlighting
------------------------------------------
First define a custom role. e.g.:

  .. code-block:: bash

    .. role:: bash(code)
       :language: bash

This then allows use inline code e.g.

  .. code-block:: bash

    Here is some awesome bash code :bash:`a = b + c`.




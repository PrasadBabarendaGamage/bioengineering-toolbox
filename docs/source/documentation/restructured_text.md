# Restructured text FAQ

*restructuredText* is a lightweight markup language (file format) that is
commonly used to create documentation. The langauge is designed to be both:
(a) processable by documentation-processing software such as Docutils, and
(b) easily readable by human programmers who are reading and writing source
code.

See these links for a guide to the rst file format.

- [guide](http://rest-sphinx-memo.readthedocs.io/en/latest/ReST.html)
- [cheatsheet](https://docs.typo3.org/m/typo3/docs-how-to-document/master/en-us/WritingReST/CheatSheet.html)

To find out about the differences between reST, docutils, readthedocs,
sphinx, and extensions, see this [link](http://www.git-pull.com/code_explorer/rst-docutils-sphinx-readthedocs.html#rest-docutils-sphinx-readthedocs).

[Guide to setting up a sphinx project](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)

## Examples of well documented code repositories

- http://libcellml.readthedocs.io/
- http://morphic.readthedocs.io/

## Inline code block with syntax highlighting
First define a custom role. e.g.:

```rest
.. role:: bash(code)
   :language: bash
```

This then allows use inline code e.g.

```rest
Here is some awesome bash code :bash:`a = b + c`.
```

[Add images](http://sphinx-doc.org/rest.html?highlight=image#images)

Use the image directive, for example:

```rest
.. image:: example.png
```

The path to the image is relative to the file. See the Sphinx documentation for more information.

## Creating tables

- [Programtically within .rst files](https://sublime-and-sphinx-guide.readthedocs.io/en/latest/tables.html)
- [Load from csv files](https://tables-with-sphinx.readthedocs.io/en/latest/csv-table.html)

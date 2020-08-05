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

## [Commenting restructuredText files](https://stackoverflow.com/questions/4783814/how-to-comment-a-string-in-restructured-text)
```rest
..
   _This: is a comment!

..
   [and] this!

..
   this:: too!

..
   |even| this:: !
```
Avoid putting comments on the same line as the double dots:
```rest
.. Avoid this type of comment
```
This is considered bad practice since it may lead to unintended consequences if the comment matches a proper markup construct.

## [Hyperlinks and cross-referencing](https://docs.typo3.org/m/typo3/docs-how-to-document/master/en-us/WritingReST/Hyperlinks.html)

### Hyperlinking
```rest
`anchor text <url>`__
```
### Referencing section headings
Add `sphinx.ext.autosectionlabel` to extensions in :file:`conf.py`.
Add the following to :file:`conf.py`.
```python
# True to prefix each section label with the name of the document it is in, followed by a colon. For example, index:Introduction for a section called Introduction that appears in document index.rst. Useful for avoiding ambiguity when the same section heading appears in different documents.
autosectionlabel_prefix_document = True
```
Example usage:
```rest
A Plain Title
-------------

This is the text of the section.

It refers to the section title, see :ref:`A Plain Title`.

To reference section headings in other files:
:ref:`path/to/file:Section heading`


```

### Cross-Referencing within a document
```rest
:ref:`anchor text <link-target>`
```
### Cross-Referencing between documents
```rest
:ref:`anchor text <document-tag:link-target>`
```
Whenever you use the cross-referencing mechanism, you should create a link target for a section chapter, by adding a label before the section header:
```rest
.. _link-target:

Headline
========
```
### Referencing external files
Reference files and paths
Use the following syntax to reference files and paths:
```rest
:file:`myfile.txt`
```
This will output: :file:`myfile.txt`.

You can reference paths in the same way:
```rest
:file:`path/to/myfile.txt`
```
This will output: :file:`path/to/myfile.txt`.

### Reference an element in a GUI
Use the following syntax to direct a user to click a link or look to a certain area of the GUI:
```rest
:guilabel:`Main Menu`
```
This will output: :guilabel:`Main Menu`.

### External files
Text snippets, large blocks of downloadable code, and even zip files or other binary sources can all be included as part of the documentation. To include files as part of the build process, use the following syntax:
```rest
:download:`An external file <readme.txt>`
```

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

## [Notes and warnings](http://udig.refractions.net/files/docs/latest/user/docguide/sphinxSyntax.html#notes-and-warnings)
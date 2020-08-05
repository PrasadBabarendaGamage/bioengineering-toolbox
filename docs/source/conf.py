# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'bioengineering-toolbox'
copyright = '2020, Thiranja Prasad Babarenda Gamage'
author = 'Thiranja Prasad Babarenda Gamage'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx_copybutton', 'recommonmark', 'sphinx.ext.autosectionlabel',
]

# True to prefix each section label with the name of the document it is in,
# followed by a colon. For example, index:Introduction for a section called
# Introduction that appears in document index.rst. Useful for avoiding
# ambiguity when the same section heading appears in different documents.
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Set the root rst to load. This is required to be named contents to allow
# readthedocs to host the docs using its default configuration.
master_doc = 'index'

# Configures Sphinx to read all files with the extensions .md and .rst.
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

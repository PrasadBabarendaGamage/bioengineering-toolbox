# Sphinx FAQ

## [Force rebuild of html, including autodoc](http://stackoverflow.com/questions/21019505/sphinx-force-rebuild-of-html-including-autodoc)
```bash
html -E -a
```
## Adding a sphinx build configuration to pycharm
In Run/Debug Configurations

1. Click the + button and selected `python docs` -> `sphinx` and complete the following fields:

  a. Name: `Sphinx`
  b. Input: Select the source directory in the documentation folder
  c. Output: Select the build directory in the documentation folder
  d. Python interpretor: Select your interpreter
  e. Options: `-E -a` (This options forces rebuild of html)

2. Click ok.

## Adding jupyter notebook code to sphinx
https://nbsphinx.readthedocs.io/en/0.7.1/

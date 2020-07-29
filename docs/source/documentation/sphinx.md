# Sphinx FAQ

## [Force rebuild of html, including autodoc](http://stackoverflow.com/questions/21019505/sphinx-force-rebuild-of-html-including-autodoc)
```bash
html -E -a
```
## Adding a sphinx build configuration to pycharm
1. Open Pycharm.
2. File -> Open -> Navigate to your project folder -> Click Ok.
3. Run -> Edit configurations. 
4. Click the + button and selected `python docs` -> `sphinx` and complete the 
following fields:
    1. Name: `Sphinx`
    2. Input: Select the source directory in the documentation folder
    3. Output: Select the build directory in the documentation folder
    4. Python interpretor: Select your interpreter
    5. Options: `-E -a` (This options forces rebuild of html)
5. Click ok.

## Adding jupyter notebook code to sphinx
https://nbsphinx.readthedocs.io/en/0.7.1/

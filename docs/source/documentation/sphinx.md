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

## Sphinx and Jupyter notebooks
### Linking to Jupyter notebooks in Sphinx
https://nbsphinx.readthedocs.io/en/0.7.1/

### Embedding Jupyter code into Sphinx Restructured Text
https://jupyter-sphinx.readthedocs.io/en/latest/
```rest
.. jupyter-execute::

  name = 'world'
  print('hello ' + name + '!')
```
### [Linking to notebooks outside of sphinx doc folder](https://github.com/vidartf/nbsphinx-link)

## Updating logo for sphinx_rtd_theme
```python
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = 'logo.svg'
```

## Updating sphinx_rtd_theme colours
You can change the theme colors by adding a custom CSS file to _static. To actually have Sphinx use that file, add this to your `conf.py`:
```python
# Update navigation background colour.
def setup (app):
    app.add_css_file('custom.css')
```

Create a custom.css file to the `docs/source/_static` folder with the following:
```css
.wy-side-nav-search, .wy-nav-top {
    background: #0b750a;
}
```

## Graphs in Sphinx/RestructuredText
Add `sphinx.ext.graphviz` to extensions in `conf.py`
Add `graphviz_output_format = "svg"` in `conf.py`
Example (see output [here](https://so-tools.readthedocs.io/en/latest/index.html))
```rest
.. graphviz::

   digraph foo {
      rankdir="BT";
      graph [fontname="avenir", fontsize=10];
      node [fontname="avenir", fontsize=10, target="_blank" shape=rectangle, style=filled, fillcolor=darkseagreen2];
      edge [fontname="avenir", fontsize=10, style=dashed, arrowhead=onormal];
      Thing [label="SO:Thing", href="https://schema.org/Thing"];
      CreativeWork [href="https://schema.org/CreativeWork"];
      Dataset [href="https://schema.org/Dataset"];
      MediaObject [href="https://schema.org/MediaObject"];
      DataDownload [href="https://schema.org/DataDownload"];
      Intangible [href="https://schema.org/Intangible"];
      PropertyValue [href="https://schema.org/PropertyValue"];
      Place [href="https://schema.org/Place", target="_blank"];
      Person [href="https://schema.org/Person", target="_blank"];
      Organization [href="https://schema.org/Organization"];

      CreativeWork -> Thing;
      Intangible -> Thing;
      Place -> Thing;
      Person -> Thing;
      Organization -> Thing;
      Dataset -> CreativeWork;
      MediaObject -> CreativeWork;
      DataDownload -> MediaObject;
      PropertyValue -> Intangible;
   }
```
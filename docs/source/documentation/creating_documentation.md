# Creating documentation

This section describes how sphinx documentation can be created for your
project. Typically this documentation would be generated within a code 
repository.

## Getting started
Follow the quick-start instructions on the [official sphinx documentation page](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html#quick-start)
During this process, it will ask `Separate source and build directories (y/n)`.
Select yes.

## Markdown
By default, sphinx recognises [RestructuredText](https://en.wikipedia.org/wiki/ReStructuredText). 
Markdown is an alternative, and relatively simpler plain text format for 
writing structured documents. Sphinx supports an unambiguous version of Markdown 
called [CommonMark](https://commonmark.org/) which addresses many of 
[Markdown's limitations](https://www.ericholscher.com/blog/2016/mar/15/dont-use-markdown-for-technical-docs/).

### Markdown best practices
A guide to best practices when using Markdown can be found in the following
[link](https://www.markdownguide.org/basic-syntax/).

### Adding support for Markdown files
CommonMark can be enabled in Sphinx by including the `Recommonmark` extension 
in the Sphinx `conf.py`. See 
[official sphinx documentation page]( 
https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html#using-markdown-with-sphinx)
for instructions on how to enable this sphinx extension.

### Adding new markdown files
A new markdown file can be added to your project as described below (ensure 
that the `Recommonmark` Sphinx extension has been enabled as described in the 
previous section).

1. Create a new text file with the `.md` extension in appropriate folder 
within the standard sphinx `docs/source` folder, e.g. 
`docs/source/my/folder/file.md`.
2. This new file can be added to the main Sphinx table of contents by 
adding the filename to the `index.rst` file in the `docs/source/` folder as 
shown below:
    ```rest
    ===========================
    Welcome to my documentation
    ===========================

    .. toctree::
       :maxdepth: 2
       :caption: Contents:

       my/folder/file
    ```

## Building documentation

### Building documentation from the command line
Change directory to the folder where the sphinx documentation was generated 
(typically `/path/to/docs/`) in the terminal, and run the following command: 
```bash
make html
```

### Building documentation using Pycharm
Follow the instructions in the following [link](documentation/sphinx:Adding%20a%20sphinx%20build%20configuration%20to%20pycharm). Python provides a markdown plugin that allows for dynamic
previewing of markdown files as shown in the figure below:
![Pycharm dynamic markdown preview!](/documentation/images/pycharm_dynamic_markdown_preview.png "Philadelphia's Magic Gardens")


## Additional features

### Linking to heading sections in other markdown files
When writing documentation, it might be useful to reference headings sections
in other markdown files. This can be enabled using the following 
[instructions](https://recommonmark.readthedocs.io/en/latest/#linking-to-headings-in-other-files).

For example, to link to a section named `# My subtitle` in a file located in 
`/path/to/file.md`, relative to the `docs/source` folder.
```markdown
[text for the link](/path/to/file:My%20Subtitle)
```
> **_NOTE:_** 
>1. Any spaces in headings need to be replaced by `%20`.
>2. The .md file extension should not be included in the path to the file.
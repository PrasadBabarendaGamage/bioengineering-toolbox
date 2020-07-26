Photo and video FAQ
===================

.. toctree::
   :maxdepth: 2

.. TEMPLATE: `link <link>`_

Click on the links in the headings for more information.

`Create gifs from images (commandline) <https://askubuntu.com/questions/648244/how-to-create-a-gif-from-the-command-line>`_
-----------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: bash

    sudo apt-get install imagemagick
    convert -delay 20 -loop 0 *.jpg myimage.gif
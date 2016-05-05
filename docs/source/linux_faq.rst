Linux FAQ
=========
   
.. toctree::
   :maxdepth: 2

.. TEMPLATE: **text** `link <link>`_

**tar and untar** `link <http://www.simplehelp.net/2008/12/15/how-to-create-and-extract-zip-tar-targz-and-tarbz2-files-in-linux/>`_
  Compress:

  .. code-block:: bash

    tar -zcvf

  Uncompress:

  .. code-block:: bash

    tar -zxvf

**Search for files in directory** `link <http://www.codecoffee.com/tipsforlinux/articles/21.html>`_

  .. code-block:: bash

    find / -name 'program.c'

**Print all the environment variables** `link <http://askubuntu.com/questions/275965/how-to-list-all-variables-names-and-their-current-values>`_

  .. code-block:: bash

    printenv

  To show a list including the "shell variables":

  .. code-block:: bash

    ( set -o posix ; set ) | less

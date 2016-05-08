Linux FAQ
=========
   
.. toctree::
   :maxdepth: 2

.. TEMPLATE: `link <link>`_

`tar/untar or zip/unzip <http://www.simplehelp.net/2008/12/15/how-to-create-and-extract-zip-tar-targz-and-tarbz2-files-in-linux/>`_
-----------------------------------------------------------------------------------------------------------------------------------
  Compress:

  .. code-block:: bash

    tar -zcvf archive_name.tar.gz directory_to_compress
    tar -jcvf archive_name.tar.bz2 directory_to_compress
    zip -r archive_name.zip directory_to_compress

  Uncompress:

  .. code-block:: bash

    tar -zxvf archive_name.tar.gz
    tar -jxvf archive_name.tar.bz2 -C /tmp/extract_here/
    unzip archive_name.zip

`Search for files in directory <http://www.codecoffee.com/tipsforlinux/articles/21.html>`_
------------------------------------------------------------------------------------------

  .. code-block:: bash

    find / -name 'program.c'

`Print all environmental variables <http://askubuntu.com/questions/275965/how-to-list-all-variables-names-and-their-current-values>`_
-------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: bash

    printenv

  To show a list including the "shell variables":

  .. code-block:: bash

    ( set -o posix ; set ) | less

`Download file from the internet <http://www.thegeekstuff.com/2009/09/the-ultimate-wget-download-guide-with-15-awesome-examples/>`_
-----------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: bash

    wget http://www.openss7.org/repos/tarballs/strx25-0.9.2.1.tar.bz2

***
Git
***

.. toctree::
   :maxdepth: 2

.. `link <link>`_


===========================
CLI (command line interface
===========================

`Backup untracked files <http://gitready.com/beginner/2009/01/16/cleaning-up-untracked-files.html>`_
----------------------------------------------------------------------------------------------------

To copy untracked files into a separate directory outside the git repository before cleaning up, use

  .. code-block:: bash

    git ls-files --others --exclude-standard -z -m - d | cpio -pmd0 .
    ./untracked-backup/

Options used:

* ``--others`` lists untracked files
* ``--exclude-standard`` uses .gitignore and the default git excludes
* ``-z`` null-delimited output
* ``-p`` pass-through (=copy)
* ``-m`` preserve modification times
* ``-d`` create missing directories
* ``-0`` null-delimited input

These commands might be useful when migrating repositories e.g. from bitbucket
to github. This allows the untracked changes to be move to a separate folder
which can then be copied over to the new location where the new repo is
located.


`Getting git on a server <https://git-scm.com/book/en/v2/Git-on-the-Server-Getting-Git-on-a-Server>`_
-----------------------------------------------------------------------------------------------------

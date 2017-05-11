***
Git
***

.. toctree::
   :maxdepth: 2

.. `link <link>`_


======
GitHub
======

`How to link to a specific line number on GitHub <http://stackoverflow.com/questions/23821235/how-to-link-to-specific-line-number-on-github>`_
--------------------------------------------------------------------------

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

`Determine the URL that a local Git repository was originally cloned from? <http://stackoverflow.com/questions/4089430/how-can-i-determine-the-url-that-a-local-git-repository-was-originally-cloned-fr>`_
-----------------------------------------------------------------------------------------------------
- If referential integrity is intact, use: ``git remote show origin``
- If referential integrity has been broken, use ``git config --get remote
  .origin.url``


`Change an existing local git repository's remote URL from HTTPS to SSH <http://stackoverflow.com/questions/7438313/pushing-to-git-returning-error-code-403-fatal-http-request-failed/>`_
----------------------------------------------------------------------------------------------------
Cloning/pushing to a repository using a HTTPS remote URL's (e.g.
https://github.com/PrasadBabarendaGamage/iron.git ) requires a password.
This can be avoided by cloning any new repository using a SSH remote URL (e.g.
git@github.com:PrasadBabarendaGamage/iron.git), or by changing the
remote URL for an existing local repository to use the SSH remote URL.

To change a existing local git repository's remote URL from HTTPS to SSH:

1. Edit the .git/config file under the root directory of the repository.

2. Find ``url=entry`` under section ``[remote "origin"]``

3. Change it from ``url=https://github.com/PrasadBabarendaGamage/iron
   .git`` to ``url=ssh://git@github.com:PrasadBabarendaGamage/iron.git``.
   that is, change all the texts before the ``@`` symbol to ``ssh://git``

4. Save config file and quit.

Now you can use ``git push origin your_branch`` to sync with your remote repo.

Note that before you can push to your remote repo, you will need to have
setup a ssh key pair e.g. in on github.

`Adding ssh key to GitHub <https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/>`_
----------------------------------------------------------------------------------------------------

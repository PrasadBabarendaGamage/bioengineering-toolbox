Linux FAQ
=========
   
.. toctree::
   :maxdepth: 2

.. TEMPLATE: `link <link>`_

Click on the links in the headings for more information.

`Find files in a terminal <https://askubuntu.com/questions/144698/find-a-file-by-name-using-command-line>`_
-----------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: bash

    find / -type f -iname "*postgis-2.0.0*"

where:

* ``./`` indicates that you want to search in the current directory. This
  can be replaced with the directory you want to start your search from.

* ``f`` can be replaced with d if you're searching for a directory instead of a
  file

* ``-iname`` can be replaced with -name if you want the search to be case
  sensitive

* ``*`` in the search term can be omitted if you don't want the wildcards in
  the search. In this case, ``*`` indicates that any number of different
  characters could be present where the ``*`` is located in the string. See
  this
  `link <http://tldp.org/LDP/GNU-Linux-Tools-Summary/html/x11655.htm/>`_ for
  more information on wildcards


The ``grep`` command can be used to simplify things further:

  .. code-block:: bash

    find . | grep -i "screen"

where ``-i`` indicates the search term is case insensitive. see this `link <http://droptips.com/using-grep-and-ignoring-case-case-insensitive-grep/>`_ for further
details about the ``grep`` command.

`Change file permissions <http://linuxcommand.org/lts0070.php>`_
-----------------------------------------------------------------------------------------------------------------------------------
Change permissions :

  .. code-block:: bash

    chmod -R 755 your_directory

+-------+---------------------------------------------------------------------+
|Value  | Description                                                         |
+=======+=====================================================================+
|755    | (rwxr-xr-x) The file's owner may read, write, and execute the file. |
|       | All others may read and execute the file. This setting is common for|
|       | programs that are used by all users.                                |
+-------+---------------------------------------------------------------------+

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

`Find size of directory <http://unix.stackexchange.com/questions/185764/how-do-i-get-the-size-of-a-directory-on-the-command-line>`_
-----------------------------------------------------------------------------------

  .. code-block:: bash

    du -sh folder

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


`Restart network manager (Ubuntu 16.04) <https://askubuntu.com/questions/320921/having-dns-issues-when-connected-to-a-vpn-in-ubuntu-13-04>`_
--------------------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: bash

    sudo systemctl restart NetworkManager


  This is useful if you VPN disconnects and you get the following error when
   trying to connect.

  .. code-block:: bash

    psam012@pc:~$ ssh psam012@bioeng10.bioeng.auckland.ac.nz
    ssh: Could not resolve hostname bioeng10.bioeng.auckland.ac.nz: Temporary failure in name resolution

GUI utility to mount remote filesystems over SSH
-----------------------------------------------------------------------------------------------------------------------------------------------------

`Older versions of Ubuntu (<11.10) <http://askubuntu.com/questions/4625/is-there-a-gui-utility-to-mount-remote-filesystems-over-ssh>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
By default the GVFS in GNOME supports SSH connections. Click on the nautilus
icon (the folder with the house on it) it will launch the file manager.

.. image:: images/ssh-remote_mount-file-manager.png

Then go to File -> "Connect to server":

.. image:: images/ssh-remote_mount-dialog.png

Paste in the following:

=========  ==============================
Sever:     bioeng10.bioeng.auckland.ac.nz
Folder:    /hpc/upi
UserName:  upi
=========  ==============================

Click connect and put in your password (ask it to forget immediately for now)

This will mount the remote SSH server in a folder you can access from the file
manager. If you need to access the mount in the command line it's in .gvfs.

You can also mount it in Nautilus. Just hit CTRL+L and in the address bar
type: ``ssh://server-ip/somepath/``

`Newer versions of Ubuntu (>11.10) <http://askubuntu.com/questions/34768/where-is-connect-to-server-for-ssh-connections-in-unity>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
press Alt+F2 and type nautilus-connect-server as shown below.

.. image:: images/ssh-remote_mount-unity-step1.png
.. image:: images/ssh-remote_mount-unity-step2.png


`Adding menu items in gnome <http://askubuntu
.com/questions/34768/where-is-connect-to-server-for-ssh-connections-in-unity>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
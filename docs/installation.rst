============
Installation
============

.. note:: Mac and Linux users may need to use "sudo" before the install commands. But
   use `virtualenv`_ if you don't want to sudo -- it's great.

.. _`virtualenv`: http://www.virtualenv.org/en/latest/

Best Method: Pip
-----------------

This will download and install Complexity::

    $ pip install complexity

This method requires an installer tool called `pip`, which you can get from
http://www.pip-installer.org/.

Don't worry, you can later uninstall Complexity like this::

    $ pip uninstall complexity

Alternate Method 1: Setup.py
-------------------------------

If you can't use `pip` to install Complexity, download the latest Complexity
release from https://pypi.python.org/pypi/complexity.

Then unzip and install Complexity::

    $ tar xzvf <name of file>
    $ cd <name of unzipped dir>
    $ python setup.py install


Alternate Method 2: Easy Install
--------------------------------

If neither of the above methods work for some reason, try this::

    $ easy_install complexity

And if that doesn't work, see :doc:`troubleshooting`.

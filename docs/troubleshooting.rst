===============
Troubleshooting
===============

Installation Problems
---------------------

Problem: Pip Fails
~~~~~~~~~~~~~~~~~~~~

Don't worry if `pip` fails like this::

    $ pip install complexity
    ...
    error: could not create '/Library/Python/2.7/site-packages/complexity': 
    Permission denied

We've got a couple of solutions for that.

Best Solution: Use Virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Install virtualenv systemwide with `pip`::

    $ sudo pip install virtualenv

2. Create a virtualenv for Complexity::

    $ virtualenv complexity-env
    $ source complexity-env/bin/activate  
            (or complexity-env/Scripts/activate.bat on Windows)
    (complexity-env) $

3. Install Complexity into the virtualenv::

    (complexity-env) $ pip install complexity
    
Alternate Solution: Install Systemwide
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Install Complexity systemwide with `pip`::

    $ sudo pip install complexity

2. If that doesn't work, you can use `easy_install` instead::

    $ sudo easy_install complexity

Site Generation Problems
------------------------

Problem: Site Generation Fails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you get an error like this::

    jinja2.exceptions.TemplateSyntaxError: Unexpected end of template. Jinja
    was looking for the following tags: 'endblock'. The innermost block that
    needs to be closed is 'block'.
    
Then check your templates carefully and make sure that you've closed all
blocks properly with `{% endblock %}`.

Still Having Problems?
----------------------

`File an issue here`_ with the following info:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the problems.

.. _`File an issue here`: https://github.com/audreyr/complexity/issues/new

==========
Complexity
==========

A refreshingly simple static site generator, for those who like to work in HTML.

Of course, @pydanny (https://twitter.com/pydanny) came up with the name for this.

Documentation
-------------

The full documentation is at http://complexity.rtfd.org.

Quickstart
----------

Using Complexity is easy! Try it out::

    $ pip install complexity
    $ git clone git@github.com:audreyr/complexity-example.git my_project
    $ cd my_project
    $ complexity

Open a web browser to http://127.0.0.1:9090 to see your newly generated Complexity static site.

Features
--------

* Takes simple HTML templates as input.
* Template inheritance, filters, etc. (Brought to you by Jinja2.)
* Data from .json files turns into template context data.

Best Used With
--------------

Complexity is designed to be used with these packages:

* `Simplicity`_: Converts ReStructuredText into JSON, which Complexity can use
  as input.
* `A Lot of Effort`_: Deploys a static website (e.g. the output of Complexity)
  to Amazon S3.
* `Cookiecutter`_: Creates projects from project templates.

Sure, they could have all been built into Complexity, but decoupling them
seemed like a nice thing to do.

.. _`Simplicity`: https://github.com/pydanny/simplicity
.. _`A Lot if Effort`: https://github.com/audreyr/alotofeffort
.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter

Dependencies
------------

* Jinja2

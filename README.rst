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
* Can output to Amazon S3. Well, not yet, but that's half of the plan.

Dependencies
------------

* Jinja2

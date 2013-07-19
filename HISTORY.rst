.. :changelog:

History
-------

0.4.1 (2013-07-19)
++++++++++++++++++

* Fix reading of JSON files from `json/`.

0.4 (2013-07-19)
++++++++++++++++++

* Project layout is now::

    my_repo/
    ├── project/       <--------- input
    │   ├── assets/
    │   │   ├── css/
    │   │   ├── js/
    │   │   └── img/
    │   ├── json/
    │   │   └── stuff.json
    │   └── templates/
    │       ├── base.html
    │       ├── index.html
    │       └── about.html
    └── www/          <---------- output (generated)
        ├── index.html
        ├── about/
        │   └── index.html
        ├── css/
        ├── js/
        └── img/

* Assets are copied over to `www/` during site generation.
* If the `www/` directory was previously created, it prompts the user and then
  deletes it before site regeneration.
* Templates starting with `base` are not generated as individual pages. They
  are meant to be extended in other templates.

0.3 (2013-07-18)
++++++++++++++++++

* Graceful shutdown/restart of dev server.
* Required input and output dir arguments.
* Optional port argument.
* Improved server start/stop messages.
* Major internal refactor.

0.2.1 (2013-07-15)
+++++++++++++++++++

* Fixes to setup.py.

0.2.0 (2013-07-15)
+++++++++++++++++++

* Data from .json files now gets read as template context data.
* Tested (and passing!) on Python 2.6, 2.7, 3.3, PyPy.

0.1.1 (2013-07-10)
++++++++++++++++++

* First release on PyPI.

.. :changelog:

History
-------

0.9.1 (2013-12-02)
++++++++++++++++++

* Depend on Jinja2 >= 2.4, not == 2.7.

0.9.0 (2013-08-28)
++++++++++++++++++

* CONFIG CHANGE: Configuration is now via a `complexity.yml` file inside the
  project, instead of a `complexity.json` file.
* Support for an `unexpanded_templates` config option (#23).
* Support for non-HTML files in `templates/` (or whatever you set
  `templates_dir` to be).

See https://complexity.readthedocs.io/en/latest/advanced_usage.html#config-using-complexity-yml
for more info.

0.8.0 (2013-08-10)
++++++++++++++++++

* USAGE CHANGE: At the command line, Complexity no longer takes an output_dir
  argument. It now assumes that your output_dir is `www/` by default, but you
  can customize it in `complexity.json`.
* Support for configuration via `complexity.json`: you can specify any or all
  of the following key/value pairs:

  - `output_dir`
  - `templates_dir`
  - `assets_dir`
  - `context_dir`

See https://complexity.readthedocs.io/en/latest/advanced_usage.html#config-using-complexity-json
for more info.

0.7 (2013-08-05)
++++++++++++++++

A couple of small but important renames. If you rely on either of the following
defaults, you will need to rename them in your Complexity project.

* Directory parameter for .json files to be turned into context data has been
  renamed from `json_dir` to `context_dir`.
* Default context directory value `json/` has been changed to `context/`.

Sometimes you want your .json files to be turned into context variables, and
sometimes you don't. This rename alleviates confusion when working with
non-context .json files.

0.6 (2013-07-26)
++++++++++++++++

* Support for multi-level template directories. (Upgrade to at least 0.6 if
  you want to have folders within folders and beyond in `templates/`.)
* Skip non-HTML files in `templates/` rather than raising `NonHTMLFileException`.

0.5 (2013-07-25)
++++++++++++++++

* Improved static site generation API - better parameters are used.
* Files in the root of `assets/` (or the asset directory) now get copied over to the output.
* Much more documentation.

0.4.2 (2013-07-21)
++++++++++++++++++

* Make reading of JSON files from `json/` optional.

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

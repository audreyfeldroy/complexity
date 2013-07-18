========
Tutorial
========

Overview
--------

This is the directory structure for a Complexity site::

    my_repo/
    ├── project/       <--------- input
    │   ├── assets/
    │   │   ├── stylesheets/
    │   │   ├── js/
    │   │   ├── img/
    │   │   └── ico/
    │   │   
    │   └── templates/
    │       ├── base.html
    │       ├── index.html
    │       └── about.html
    │
    └── www/          <---------- output
        ├── index.html
        ├── about/
        │   └── index.html
        ├── css/
        ├── js/
        ├── img/
        └── ico/
 
Part 1: Setup
-------------

Create a `project/` directory with subfolders for your work:

* In `templates/`, create templates.

* Put static files into the `stylesheets/`, `js/`, and `img/` directories of
`assets/`. 

* Creating additional directories in `assets` like `ico/` is fine; they'll get
copied over to www without modification.

At the same level as `project/`, a `www/` directory will be auto-generated.
It will contain your final rendered templates and optimized static assets.

When you're done, you should have a project structure like that in
https://github.com/audreyr/complexity-example.

Part 2: Generate the Site and Serve It Locally
----------------------------------------------

Run the `complexity` command, passing it input and output directories::

    $ complexity project/ www/

This results in the following:

* Templates are rendered and output to files.
* CSS is minified and concatenated.
* JS is minified, concatenated, and obfuscated.
* A lightweight server starts up locally, serving your site so that you can see
  how it looks and check that everything works.

Open a web browser to http://127.0.0.1:9090. You should see your newly generated site!

Part 3: Upload the Site to Amazon S3
-------------------------------------

Use the "alotofeffort" tool::

    $ pip install alotofeffort
    $ alotofeffort www/ your-s3-bucketname

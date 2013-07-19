========
Tutorial
========

Part 0: Overview
----------------

This is the directory structure for a minimal Complexity site::

    my_repo/
    ├── project/       <--------- input
    │   ├── assets/
    │   │   ├── css/
    │   │   ├── js/
    │   │   └── img/
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
        └── img/
 
Part 1: Setup
-------------

First, grab a copy of the example Complexity site::

    git clone https://github.com/audreyr/complexity-example.git

Open everything in a text editor. You should see a main `project/` directory
with subfolders for your work:

* Study the template files in `templates/`. Notice how `index.html` and 
  `about.html` both share a common parent template, `base.html`.

* Notice the `assets/` directory. That is where you put your static files.

* Creating additional directories in `assets/` (e.g. `ico/`) is fine; they'll get
  copied over to `www/` without modification.

At the same level as `project/`, a `www/` directory will be auto-generated.
It will contain your final rendered templates and optimized static assets.

When you're done, you should have a project structure like that in
https://github.com/audreyr/complexity-example.

Part 2: Generate the Site and Serve It Locally
----------------------------------------------

Run the `complexity` command, passing it input and output directories::

    $ complexity project/ www/

This results in the following:

* Templates are rendered and output to files smartly:

    * Any templates starting with "base" are assumed to be parent templates
      and not rendered on their own (e.g. `base.html`, `base_section.html`)
    * Templates named `index.html` are output to the same corresponding
      locations in `www/`.
    * Other templates are expanded in order to hide the ".html" extension.
      For example, `about.html` is expanded to `about/index.html`.

* A lightweight server starts up locally, serving your site so that you can see
  how it looks and check that everything works.
  
Open a web browser to http://127.0.0.1:9090. You should see your newly generated site!

In an upcoming release, the following will also occur during Complexity's
generation process:

* CSS will be minified and concatenated.
* SCSS and/or LESS will compiled to CSS, then minified and concatenated.
* JS will minified, concatenated, and obfuscated.

Development is happening at a rapid pace, so stay tuned. To keep updated, watch
and star https://github.com/audreyr/complexity on GitHub.

Part 3: Upload the Site to Amazon S3
-------------------------------------

Use the "alotofeffort" tool::

    $ pip install alotofeffort
    $ alotofeffort www/ your-s3-bucketname

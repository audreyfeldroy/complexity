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

* Study the template files in `templates/`. We'll go over them shortly.

* Notice the `assets/` directory. That is where you put your static files.

* Creating additional directories in `assets/` (e.g. `ico/`) is fine; they'll get
  copied over to `www/` without modification.

At the same level as `project/`, a `www/` directory will be auto-generated.
It will contain your final rendered templates and optimized static assets.

When you're done, you should have a project structure like that in
https://github.com/audreyr/complexity-example.

Part 2: What's in a Complexity Site?
------------------------------------

Here's what a very simple Complexity site looks like:

`project/templates/base.html`:

.. code-block:: html+jinja

    <!DOCTYPE html>
    <html>
    <head>
        <title>{% block title %}{% endblock %} - Built with Complexity</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Bootstrap -->
        <link href="/css/bootstrap.min.css" rel="stylesheet" media="screen">
    </head>
    <body>
        <div class="container">
            <div class="navbar">
                <div class="navbar-inner">
                    <a class="brand" href="#">Complexity</a>
                    <ul class="nav">
                        <li><a href="/">Home</a></li>
                        <li><a href="/about/">About</a></li>
                    </ul>
                </div>
            </div>

            {% block content %}
            {% endblock %}
        </div>

    <script src="http://code.jquery.com/jquery.js"></script>
    <script src="/js/bootstrap.min.js"></script>
    </body>
    </html>

`project/templates/index.html`:

.. code-block:: html+jinja

    {% extends "base.html" %}

    {% block title %}Home{% endblock %}

    {% block content %}
    <div class="row">
        <div class="span12">
            <h1>Home</h1>
            <p>This is the Home page of your website.</p>
        </div>
    </div>
    {% endblock %}

`project/templates/about.html`:

.. code-block:: html+jinja

    {% extends "base.html" %}

    {% block title %}About{% endblock %}

    {% block content %}
    <div class="row">
        <div class="span12">
            <h1>About</h1>
            <p>This is the About page of your website.</p>
        </div>
    </div>
    {% endblock %}

Notice how `index.html` and `about.html` both share a common parent template,
`base.html`.

Part 3: Generate the Site and Serve It Locally
----------------------------------------------

Run the `complexity` command, passing it input and output directories::

    $ complexity project/

This results in the following:

* A `www/` directory gets created, containing your generated static HTML site.

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

Part 4: Upload the Site to Amazon S3
-------------------------------------

For site deployment we'll use the "alotofeffort" tool. It is designed for
use with Complexity, but it works with non-Complexity sites just as well.

Install it::

    $ pip install alotofeffort

Save the following in `~/.boto`::

    [Credentials]
    aws_access_key_id = ...
    aws_secret_access_key = ...
    
Replace `...` with your AWS access credentials, of course.

Then deploy the `www/` directory to any S3 bucket that you own::

    $ alotofeffort www/ your-s3-bucketname

Your site is now live! Go to the URL that `alotofeffort` prints out after
it finishes uploading.

Point your domain name at that URL, and you'll be done.

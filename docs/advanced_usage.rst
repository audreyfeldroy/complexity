===============
Advanced Usage
===============

In the tutorial, you saw an example of a minimal Complexity project layout.
Now here is an example of a more advanced Complexity site::

    my_repo/
    ├── project/       <--------- input
    │   ├── assets/
    │   │   ├── css/
    │   │   ├── js/
    │   │   ├── img/
    │   │   ├── ico/
    │   │   └── robots.txt
    │   ├── context/
    │   │   ├── books.json
    │   │   └── movies.json
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── index.html
    │   │   └── about.html
    │   └── complexity.yml
    │
    └── www/          <---------- output
        ├── index.html
        ├── about/
        │   └── index.html
        ├── css/
        ├── js/
        ├── img/
        └── ico/

Let's explore some of Complexity's advanced features.

Config Using complexity.yml
----------------------------

You can configure a Complexity project with a `complexity.yml` file like
this:

.. code-block:: yaml

    # Config file for a Complexity project

    # Directories are relative to current (project) dir
    templates_dir: "templates"
    assets_dir: "assets"
    context_dir: "context"
    output_dir: "../www"

    # List of templates that should not be expanded to pretty-format URLs
    unexpanded_templates:
     - "404.html"
     - "500.html"

Put `complexity.yml` in your project root (e.g. in project/).

Here is what you can configure:

* `templates_dir`: Directory containing templates. Anything that needs to be
  templated goes here.
* `assets_dir`: Directory containing static assets (to be copied over without
  templating).
* `context_dir`: Directory containing `.json` files to be turned into context
  variables for the templates.
* `output_dir`: Directory where the generated website will be output.
* `unexpanded_templates`: List of HTML templates for which you want to keep
  the URLs unexpanded (e.g. `404.html` instead of `404/index.html`).

All of the above are optional.

Complexity uses sensible defaults. If you don't specify a `complexity.yml`,
this is the assumed default config:

.. code-block:: yaml

    templates_dir: "templates"
    assets_dir: "assets"
    context_dir: "context"
    output_dir: "../www"

JSON Auto-Loading
----------------------

Data from .json files in your context directory automatically turns into
template context data.

For example, suppose you have this in `context/books.json`:

.. code-block:: javascript

  [
    {
      "url": "http://www.amazon.com/Two-Scoops-Django-Best-Practices/dp/1481879707/",
      "title": "Two Scoops of Django"
    },
    {
      "url": "http://www.amazon.com/Very-Magical-Caterpillar-Tale-Butterfly/dp/1453714081/",
      "title": "A Very Magical Caterpillar Tale"
    }
  ]

Then you can refer to the books in a template like this:

.. code-block:: html+jinja

    {% extends 'base.html' %}

    {% block title %}Index{% endblock %}

    {% block content %}
        <p>Here are my books:</p>
        {% for book in books %}
            <a href="{{ book.url }}">{{ book.title }}</a>
        {% endfor %}
    {% endblock %}
    
The contents of `books.json` get turned into `{{ books }}`, which in this case
is a list that you can iterate over.

What About Static JSON Files?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have .json files that you want served as static assets rather than
turned into context data, that's fine. 

Just put them in `assets/js/` (or anywhere in `assets/`), and they'll get
copied over to the output directory like any other static asset.

Other Asset Directories and Files
---------------------------------

You can create any type of asset directory or file that you want in `assets/`
(or your desired assets directory).

All assets will get copied over to `www/` when you generate your site.

.. note:: Better handling/processing of assets will be implemented in an
   upcoming release, including CSS/JS minification, image optimization,
   and SASS and/or LESS compilation.

Using Complexity as a Library
------------------------------

Complexity can be used just like any other Python package.

You can simply call the Complexity API like this:

.. code-block:: python

    from complexity.main import complexity
    
    complexity('project/', 'www/')

Calling other Complexity API functions is just as straightforward:

.. code-block:: python

    from complexity import generate

    # Optionally generate context if you need to
    context = generate_context(context_dir='project/context/')

    # Generate HTML from your templates (and context, if you have it)
    generate.generate_html(templates_dir='project/templates/', output_dir='www/', context=context)

    # Copy assets over
    generate.copy_assets(assets_dir='project/assets/', output_dir='www/')

This allows you to use Complexity as a dependency in your own Python projects.

.. note:: As of this release, the API works, but it is subject to change.
   Please pin your dependencies if you need this to be stable, and keep an eye
   on this section for changes when you upgrade.

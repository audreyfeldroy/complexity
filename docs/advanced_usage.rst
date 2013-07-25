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
    │   │   └── ico/
    │   ├── json/
    │   │   ├── books.json
    │   │   └── movies.json
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

Let's explore some of Complexity's advanced features.

JSON Auto-Loading
----------------------

Data from .json files automatically turns into template context data.

For example, suppose you have this in `books.json`:

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

Other Asset Directories
-----------------------

You can create any type of asset directory that you want in `assets/` and
it will get copied over to `www/` when you generate your site.

.. note:: Better handling/processing of assets will be implemented in an
   upcoming release, including CSS/JS minification, image optimization,
   and SASS and/or LESS compilation.

Using Complexity as a Library
------------------------------

Complexity can be used just like any other Python package.

You can simply call the Complexity API like this:

.. code-block:: python

    from complexity import complexity
    
    complexity('project/', 'www/')

Calling other Complexity API functions is just as straightforward:

.. code-block:: python

    from complexity import generate

    # Optionally generate context if you need to
    context = generate_context(json_dir='project/json/')

    # Generate HTML from your templates (and context, if you have it)
    generate.generate_html(input_dir='project/', output_dir='www/', context=context)

    # Copy assets over
    generate.copy_assets(input_dir='project/', output_dir='www/')

This allows you to use Complexity as a dependency in your own Python projects.

.. note:: As of this release, the API works, but it is subject to change.
   Please pin your dependencies if you need this to be stable, and keep an eye
   on this section for changes when you upgrade.

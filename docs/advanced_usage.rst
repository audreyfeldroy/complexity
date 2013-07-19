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

For example, suppose you have this in `books.json`::

    [
        {
            'title': 'Two Scoops of Django',
            'url': 'http://www.amazon.com/Two-Scoops-Django-Best-Practices/dp/1481879707/'
        },
        {
            'title': 'A Very Magical Caterpillar Tale',
            'url': 'http://www.amazon.com/Very-Magical-Caterpillar-Tale-Butterfly/dp/1453714081/'
        }
    ]

Then you can refer to the books in a template like this::

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


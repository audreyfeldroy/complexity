#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import errno
import http.server
import os
import socketserver

from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            return False
    return True


def serve_static_site():
    # Serve the output directory
    os.chdir('output/')
    PORT = 9090
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("serving at port", PORT)
    httpd.serve_forever()


def generate_html(pages, input_dir='input/'):
    env = Environment()
    env.loader = FileSystemLoader(input_dir)

    for page in pages:
        tmpl = env.get_template('{0}.html'.format(page))
        rendered_html = tmpl.render()

        # Put index in the root. It's a special case.
        if page == 'index':
            with open('output/index.html', 'w') as fh:
                fh.write(rendered_html)

        # Put other pages in page/index.html, for better URL formatting.
        else:
            make_sure_path_exists('output/{0}/'.format(page))
            with open('output/{0}/index.html'.format(page), 'w') as fh:
                fh.write(rendered_html)


def command_line_runner():
    """ Entry point for the package, as defined in setup.py. """

    # List the stem of each file in input/
    pages = [f.split('.')[0] for f in os.listdir('input/')]

    # Generate and serve the HTML site
    generate_html(pages)
    serve_static_site()


if __name__ == '__main__':
    command_line_runner()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import errno
import http.server
import os
import socketserver

from jinja2 import FileSystemLoader
from jinja2.environment import Environment

pages = ('index', 'about')

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def serve_static_site():
    # Serve the output directory
    PORT = 9090
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("serving at port", PORT)
    httpd.serve_forever()

env = Environment()
env.loader = FileSystemLoader('input/')

for page in pages:
    tmpl = env.get_template('{0}.html'.format(page))
    rendered_html = tmpl.render()

    # Put index in the root. It's a special case.
    if page == 'index':
        with open('output/index.html','w') as fh:
            fh.write(rendered_html)

    # Put other pages in page/index.html, for better URL formatting.
    else:
        make_sure_path_exists('output/{0}/'.format(page))
        with open('output/{0}/index.html'.format(page),'w') as fh:
            fh.write(rendered_html)

os.chdir('output/')
serve_static_site()

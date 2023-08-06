# #############################
# The web server's external API
# #############################

import pkg_resources

from os import path

from ..config import config
from flask import Flask
from .routes import *


app = None

try:
    rel_template_dir = config['templates']['rel_dir'].get(str)
    rel_static_dir =  config['static']['rel_dir'].get(str)

    abs_template_dir = pkg_resources.resource_filename(f'web.{rel_template_dir}', 'index.html')
    abs_static_dir = pkg_resources.resource_filename(f'web.{rel_static_dir}', 'static.css')

    print("template dir ", path.dirname(abs_template_dir))
    print("static dir ", path.dirname(abs_static_dir))

    templates_dir = path.abspath(path.dirname(abs_template_dir))
    static_dir = path.abspath(path.dirname(abs_static_dir))


    app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
    app.register_blueprint(routes)

except Exception as e:
    print("Error while fetching template and/or static directories paths. Either values do not exist or are of the wrong type.")
    print(f'Error : {e}')



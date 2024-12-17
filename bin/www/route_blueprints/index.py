# This file is the index blueprint
# Author: Chase Quinn | ShadowCoding

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

index = Blueprint('index', __name__, template_folder="templates")

@index.route('/', methods=["GET"])
def login():
    try:
        return render_template('index.html', website_title="xps")
    except TemplateNotFound:
        abort(404)
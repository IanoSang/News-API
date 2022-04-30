from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources


@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """

    sources = get_sources()
    title = 'News Sources'

    return render_template('index.html', title=title, sources=sources)

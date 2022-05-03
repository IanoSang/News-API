from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_articles


@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """

    sources = get_sources()
    title = 'News Sources'

    return render_template('index.html', title=title, sources=sources)


@main.route('/articles/<sources_id>')
def articles(sources_id):
    """
    View articles page function that returns the  article details page and its data
    """
    articles = get_articles(sources_id)

    return render_template('articles.html', articles=articles)
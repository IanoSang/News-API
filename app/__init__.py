from flask import Flask
from config import config_options


def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Will add the views and forms

    return app


class Config:
    """
    General configuration parent class
    """
    NEWS_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'


def app():
    return None
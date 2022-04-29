from app import app
import urllib.request, json
from .models import Sources

# Getting api key
api_key = None
# Getting the news base url
base_url = None


def configure_request(app):
    global api_key, base_url, news_api_sources_url
    api_key = app.config['NEWS_API_KEY']
    news_api_sources_url = app.config['NEWS_API_SOURCES_URL']


def get_sources(category):
    """
    Function that gets the json response to our url request
    """
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['results']:
            sources_results_list = get_sources_response['results']
            sources_results = process_results(sources_results_list)

    return sources_results

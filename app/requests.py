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


def process_results(sources_list):
    """
    Function  that processes the news sources result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain sources details

    Returns :
        sources_results: A list of sources objects
    """
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        category = sources_item.get('category')
        description = sources_item.get('description')

        if id:
            sources_object = Sources(id, name, category, description)
            sources_results.append(sources_object)

        return sources_results

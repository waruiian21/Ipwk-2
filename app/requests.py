# from app import a
import urllib.request,json
from .models import Source, Article
from maya import parse

# Getting api key, all sources url and source url
api_key = None
all_sources_url = None
source_url = None


def configure_request(app):
    global api_key, all_sources_url, source_url
    all_sources_url = app.config['ALL_SOURCES_URL']
    source_url = app.config['SOURCE_URL']
    api_key = app.config['API_KEY']


def get_sources():
    get_sources_url = all_sources_url.format(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        sources_raw_data = url.read()
        sources_response = json.loads(sources_raw_data)

    sources_list = None

    if sources_response['sources']:
        new_list = []
        for source in sources_response['sources']:
            id = source['id']
            name = source['name']
            description = source['description']
            new_source = Source(id,name,description)
            new_list.append(new_source)

        sources_list = new_list


    return sources_list

def get_specific_source(source_id):
    get_source_url = source_url.format(source_id, api_key)
    with urllib.request.urlopen(get_source_url) as url:
        source_raw_data = url.read()
        source_response = json.loads(source_raw_data)

    articles_list = None

    if source_response['articles']:
        new_list = []
        for article in source_response['articles']:
            title = article['title']
            author = article['author']
            image_url = article['urlToImage']
            source = article['source']
            date_published= parse(article['publishedAt']).datetime()
            article_url= article['url']

            if image_url:
                new_article = Article(title, author, image_url, date_published, article_url,source)
                new_list.append(new_article)

        articles_list = new_list


    return articles_list

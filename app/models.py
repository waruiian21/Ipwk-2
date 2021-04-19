class Source:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.desc = description


class Article:
    def __init__(self, title, author, image_url, date_published, article_url, source):
        self.title = title
        self.author = author
        self.date_published = date_published
        self.article_url = article_url
        self.image_url = image_url
        self.source = source

class Sources:
    """
    Sources class to define News Sources Objects
    """

    def __init__(self, id, name, category, description):
        self.id = id
        self.name = name
        self.category = category
        self.description = description


class Articles:
    """
    News Articles class to define news articles objects
    """
    def __init__(self,title,urlToImage,content,author,publishedAt,url):
        self.title = title
        self.urlToImage = urlToImage
        self.content = content
        self.author = author
        self.publishedAt= publishedAt
        self.url=url


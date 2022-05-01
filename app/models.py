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
    Articles class to define News Articles Objects
    """

    def __int__(self, title, image, content, author, time, url):
        self.title = title
        self.image = image
        self.content = content
        self.author = author
        self.time = time
        self.url = url


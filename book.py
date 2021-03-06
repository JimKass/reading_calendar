"""

"""


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "{} by {}; pages: {}".format(self.title, self.author, self.pages)

    def sort(self):
        self.pages.sort()

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book(Title: {self.title}, Author: {self.author}, Pages: {self.pages})"

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.pages!r})"

    def __del__(self):
        print(f"Book(Title: {self.title}, Author: {self.author}, Pages: {self.pages}) is being deleted")

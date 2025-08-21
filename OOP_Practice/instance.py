# Using an instance method
class Book:
    total_books = 0

    def display_total_books(self):
        return f"Total books: {Book.total_books}"
    

# Using class method
class Book:
    total_books = 0

    @classmethod
    def display_total_books(cls):
        return f"Total books: {cls.total_books}"
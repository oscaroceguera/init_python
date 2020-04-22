class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}>"

    @classmethod
    def hardcover(cls, name, page_weight):
        # return Book(name, Book.TYPES[0], page_weight + 100)
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        # return Book(name, Book.TYPES[1], page_weight)
        return cls(name, cls.TYPES[1], page_weight)


book = Book("El principito", "hardcover", 15000)

print(book)

harry = Book.hardcover("Harry Potter", 1500)
print(harry)

light = Book.paperback("Python 101", 600)
print(light)

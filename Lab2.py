class Book:
    def __init__(self, id, name, pages):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id={self.id}, name={repr(self.name)}, pages={self.pages})'

class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

# Пример пользования данным классом
book1 = Book(id=1, name="test_name_1", pages=200)
book2 = Book(id=2, name="test_name_2", pages=300)

library = Library()
library.books.append(book1)
library.books.append(book2)

print(library.get_next_book_id())
print(library.get_index_by_book_id(2))

# Попробуем получить индекс несуществующей книги
try:
    print(library.get_index_by_book_id(3))
except ValueError as e:
    print(e)
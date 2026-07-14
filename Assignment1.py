class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = {}     
        self.patrons = {}    

    def add_book(self, book_id, title, author):
        self.books[book_id] = Book(book_id, title, author)

    def register_patron(self, patron_id, name):
        self.patrons[patron_id] = Patron(patron_id, name)

    def borrow_book(self, patron_id, book_id):
        patron = self.patrons.get(patron_id)
        book = self.books.get(book_id)
        
        if book and patron and book.available:
            book.available = False
            patron.borrowed_books.append(book)

    def return_book(self, patron_id, book_id):
        patron = self.patrons.get(patron_id)
        book = self.books.get(book_id)
        
        if book and patron and book in patron.borrowed_books:
            book.available = True
            patron.borrowed_books.remove(book)

library = Library()
library.add_book("B02", "Harry Potter", "J. K. Rowling")
library.register_patron("P100", "Tanishka")

print("--- START LIBRARY TRANSACTION ---")

print(f"Is 'Harry Potter' available on the shelf? {library.books['B02'].available}")

library.borrow_book("P100", "B02")
backpack_contents = library.patrons["P100"].borrowed_books[0].title
print(f"Tanishka borrowed a book.")
print(f"Current item in Tanishka's backpack: {backpack_contents}")

print(f"Is 'Harry Potter' available on the shelf now? {library.books['B02'].available}")

library.return_book("P100", "B02")
print("Tanishka returned the book.")

print(f"Is 'Harry Potter' available again? {library.books['B02'].available}")

#OUTPUT : 
#--- START LIBRARY TRANSACTION ---
#Is 'Harry Potter' available on the shelf? True
#Tanishka borrowed a book.
#Current item in Tanishka's backpack: Harry Potter
#Is 'Harry Potter' available on the shelf now? False
#Tanishka returned the book.
#Is 'Harry Potter' available again? True

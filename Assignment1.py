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

    def display_books(self):
        for book in self.books.values():
            print(book.book_id, book.title, book.author, book.available)

    def display_patrons(self):
        for patron in self.patrons.values():
            print(patron.patron_id, patron.name, [b.title for b in patron.borrowed_books])

library = Library()

while True:
    print("\n LIBRARY MANAGEMENT SYSTEM")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Patrons")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        library.add_book(book_id, title, author)

    elif choice == "2":
        patron_id = input("Enter Patron ID: ")
        name = input("Enter Patron Name: ")
        library.register_patron(patron_id, name)

    elif choice == "3":
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")
        library.borrow_book(patron_id, book_id)

    elif choice == "4":
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")
        library.return_book(patron_id, book_id)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        library.display_patrons()

    elif choice == "7":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")

#OUTPUT
"""
 LIBRARY MANAGEMENT SYSTEM
1. Add Book
2. Register Patron
3. Borrow Book
4. Return Book
5. Display Books
6. Display Patrons
7. Exit
Enter your choice: 1
Enter Book ID: 100
Enter Book Title: Harry Potter
Enter Author Name: J. K. Rowling

 LIBRARY MANAGEMENT SYSTEM
1. Add Book
2. Register Patron
3. Borrow Book
4. Return Book
5. Display Books
6. Display Patrons
7. Exit
Enter your choice: 2
Enter Patron ID: 25
Enter Patron Name: Tanishka Gidde

 LIBRARY MANAGEMENT SYSTEM
1. Add Book
2. Register Patron
3. Borrow Book
4. Return Book
5. Display Books
6. Display Patrons
7. Exit
Enter your choice: 3
Enter Patron ID: 25
Enter Book ID: 100

 LIBRARY MANAGEMENT SYSTEM
1. Add Book
2. Register Patron
3. Borrow Book
4. Return Book
5. Display Books
6. Display Patrons
7. Exit
Enter your choice: 4
Enter Patron ID: 25
Enter Book ID: 100

 LIBRARY MANAGEMENT SYSTEM
1. Add Book
2. Register Patron
3. Borrow Book
4. Return Book
5. Display Books
6. Display Patrons
7. Exit
Enter your choice: 5
100 Harry Potter J. K. Rowling True

 LIBRARY MANAGEMENT SYSTEM
1. Add Book
2. Register Patron
3. Borrow Book
4. Return Book
5. Display Books
6. Display Patrons
7. Exit
Enter your choice: 6
25 Tanishka Gidde []

 LIBRARY MANAGEMENT SYSTEM
1. Add Book
2. Register Patron
3. Borrow Book
4. Return Book
5. Display Books
6. Display Patrons
7. Exit
Enter your choice: 7
Thank you for using Library Management System!
"""

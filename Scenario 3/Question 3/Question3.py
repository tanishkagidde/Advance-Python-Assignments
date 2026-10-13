import csv
import re


def display_books(filename):
  """Displays all book records from the CSV file."""
  try:
    with open(filename, mode='r', encoding='utf-8') as file:
      reader = csv.reader(file)
      print('\n--- All Library Books ---')
      for row in reader:
        print(' | '.join(row))
  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")


def search_books_by_title(filename, keyword):
  """Searches for books whose title starts with the keyword using regular expressions."""
  try:
    with open(filename, mode='r', encoding='utf-8') as file:
      reader = csv.reader(file)
     
      pattern = re.compile(rf'^{re.escape(keyword)}', re.IGNORECASE)

      print(f"\n--- Books Starting With '{keyword}' ---")
      found = False

      for row in reader:
        if len(row) > 1:
          title = row[1].strip()
          if pattern.match(title):
            print(' | '.join(row))
            found = True

      if not found:
        print(f"No books found starting with '{keyword}'.")
  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")


if __name__ == '__main__':
  filename = 'books.csv'

  while True:
    print('\n=== Library Book Search System ===')
    print('1. Display All Books')
    print('2. Search Books by Title Starting Keyword (Regex)')
    print('3. Exit')
    choice = input('Enter your choice (1-3): ').strip()

    if choice == '1':
      display_books(filename)
    elif choice == '2':
      keyword = input('Enter starting keyword for the book title: ').strip()
      search_books_by_title(filename, keyword)
    elif choice == '3':
      print('Exiting program. Goodbye!')
      break
    else:
      print('Invalid choice. Please enter 1, 2, or 3.')

'''
OUTPUT :

=== Library Book Search System ===
1. Display All Books
2. Search Books by Title Starting Keyword (Regex)
3. Exit
Enter your choice (1-3): 1

--- All Library Books ---
101 | The Alchemist | Paulo Coelho | Fiction
102 | The Great Gatsby | F. Scott Fitzgerald | Classic
103 | To Kill a Mockingbird | Harper Lee | Classic
104 | Python Programming | John Zelle | Education
105 | The Hobbit | J.R.R. Tolkien | Fantasy

=== Library Book Search System ===
1. Display All Books
2. Search Books by Title Starting Keyword (Regex)
3. Exit
Enter your choice (1-3): 2
Enter starting keyword for the book title: The

--- Books Starting With 'The' ---
101 | The Alchemist | Paulo Coelho | Fiction
102 | The Great Gatsby | F. Scott Fitzgerald | Classic
105 | The Hobbit | J.R.R. Tolkien | Fantasy

=== Library Book Search System ===
1. Display All Books
2. Search Books by Title Starting Keyword (Regex)
3. Exit
Enter your choice (1-3): 3
Exiting program. Goodbye!
'''

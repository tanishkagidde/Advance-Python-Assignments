import csv
import sys


def display_employees(filename):
  """Displays all employee records from the CSV file."""
  try:
    with open(filename, mode='r', encoding='utf-8') as file:
      reader = csv.reader(file)
      print('\n--- All Employee Records ---')
      for row in reader:
        print(' | '.join(row))
  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")


def search_employee(filename, emp_id):
  """Searches for an employee by their Employee ID (assumed to be in the first column)."""
  try:
    with open(filename, mode='r', encoding='utf-8') as file:
      reader = csv.reader(file)
      found = False
      for row in reader:
        if row and row[0].strip() == emp_id.strip():
          print('\n--- Employee Found ---')
          print(' | '.join(row))
          found = True
          break
      if not found:
        print(f"Employee with ID '{emp_id}' not found.")
  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")


if __name__ == '__main__':
 
  if len(sys.argv) < 2:
    print('Usage: python employee_manager.py <filename.csv>')
    sys.exit(1)

  filename = sys.argv[1]

  while True:
    print('\n=== Employee Record Management System ===')
    print('1. Display All Employees')
    print('2. Search Employee by ID')
    print('3. Exit')
    choice = input('Enter your choice (1-3): ').strip()

    if choice == '1':
      display_employees(filename)
    elif choice == '2':
      emp_id = input('Enter Employee ID to search: ').strip()
      search_employee(filename, emp_id)
    elif choice == '3':
      print('Exiting program. Goodbye!')
      break
    else:
      print('Invalid choice. Please enter 1, 2, or 3.')

'''
OUTPUT :
=== Employee Record Management System ===
1. Display All Employees
2. Search Employee by ID
3. Exit
Enter your choice (1-3): 1

--- All Employee Records ---
1 | Alice Smith | HR | 50000
2 | Bob Jones | Engineering | 65000
3 | Charlie Brown | Marketing | 55000

=== Employee Record Management System ===
1. Display All Employees
2. Search Employee by ID
3. Exit
Enter your choice (1-3): 2
Enter Employee ID to search: 2

--- Employee Found ---
2 | Bob Jones | Engineering | 65000

=== Employee Record Management System ===
1. Display All Employees
2. Search Employee by ID
3. Exit
Enter your choice (1-3): 3
Exiting program. Goodbye!
'''

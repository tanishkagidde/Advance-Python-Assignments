'''
Employee Payroll Management System
Design a Python program for an Employee Payroll Management System.
CO1 – Object-Oriented Programming (10 Marks)
Create the following classes:
Employee
Data members: Employee Name, Employee ID, Basic Salary 
Constructor to initialize employee details. 
Implement a method to calculate the employee grade based on salary: 
Grade A: Salary ≥ ₹80,000 
Grade B: Salary ≥ ₹60,000 
Grade C: Salary ≥ ₹40,000 
Grade D: Salary < ₹40,000 
Implement display() and __str__() methods. 
Company
Store a list of employees. 
Implement methods to add and display employee records. 
CO2 – Dynamic Programming (10 Marks)
Implement Fibonacci using Memoization (Top-Down DP) to generate the first N Fibonacci numbers.
'''

class Employee:
    def __init__(self, emp_id: str, name: str, basic_salary: float):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_grade(self) -> str:
        """Calculates employee grade based on basic salary criteria."""
        if self.basic_salary >= 80000:
            return "Grade A"
        elif self.basic_salary >= 60000:
            return "Grade B"
        elif self.basic_salary >= 40000:
            return "Grade C"
        else:
            return "Grade D"

    def display(self):
        """Displays employee details directly."""
        print(self)

    def __str__(self) -> str:
        return f"ID: {self.emp_id:<8} | Name: {self.name:<15} | Basic Salary: ₹{self.basic_salary:,.2f} | Grade: {self.calculate_grade()}"


class Company:
    def __init__(self, company_name: str):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, emp_id: str, name: str, basic_salary: float):
        """Creates and adds a new employee record to the company."""
        employee = Employee(emp_id, name, basic_salary)
        self.employees.append(employee)
        print(f"Added: {name} (ID: {emp_id})")

    def display_all_employees(self):
        """Displays all employee records in the company."""
        print(f"\n--- {self.company_name} Employee Directory ---")
        if not self.employees:
            print("No employees found.")
            return

        print("-" * 75)
        for emp in self.employees:
            emp.display()
        print("-" * 75)

if __name__ == "__main__":
    company = Company("Tech Corp Solutions")

    company.add_employee("EMP101", "Aarav Sharma", 85000)  # Grade A
    company.add_employee("EMP102", "Priya Patel", 65000)   # Grade B
    company.add_employee("EMP103", "Rohan Mehta", 45000)   # Grade C
    company.add_employee("EMP104", "Ananya Sen", 32000)    # Grade D

    # Displaying employee details
    company.display_all_employees()
    
def fibonacci_memoization(n, dp):

    if n <= 1:
        return n
    if dp[n] != -1:

        return dp[n]

    dp[n] = fibonacci_memoization(n - 1, dp) + fibonacci_memoization(n - 2, dp)
    return dp[n]

n = int(input("Enter value : "))

dp = [-1] * (n + 1)
memoization_result = fibonacci_memoization(n, dp)
print("\nMemoization Answer :", memoization_result)

'''
OUTPUT : 
Added: Aarav Sharma (ID: EMP101)
Added: Priya Patel (ID: EMP102)
Added: Rohan Mehta (ID: EMP103)
Added: Ananya Sen (ID: EMP104)

--- Tech Corp Solutions Employee Directory ---
---------------------------------------------------------------------------
ID: EMP101   | Name: Aarav Sharma    | Basic Salary: ₹85,000.00 | Grade: Grade A
ID: EMP102   | Name: Priya Patel     | Basic Salary: ₹65,000.00 | Grade: Grade B
ID: EMP103   | Name: Rohan Mehta     | Basic Salary: ₹45,000.00 | Grade: Grade C
ID: EMP104   | Name: Ananya Sen      | Basic Salary: ₹32,000.00 | Grade: Grade D
---------------------------------------------------------------------------
Enter value : 10

Memoization Answer : 55
'''

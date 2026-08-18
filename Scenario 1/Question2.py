"""
	2. Employee Management System					
						
	Develop a Python application to maintain employee information.					
						
	Requirements					
	Create an Employee class with:					
		Employee ID				
		Name				
		Salary				
	Categorize employees as:					
		High Salary (≥ ₹70,000)				
		Medium Salary (₹40,000–69,999)				
		Low Salary (< ₹40,000)				
	Create a Company class.					
	Add employee details.					
	Display all employee information.					
						
"""
class Employee:
    def __init__(self, emp_id: str, name: str, salary: float):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def get_category(self) -> str:
        """Categorize employee based on salary range."""
        if self.salary >= 70000:
            return "High Salary"
        elif 40000 <= self.salary < 70000:
            return "Medium Salary"
        else:
            return "Low Salary"

    def __str__(self) -> str:
        return f"ID: {self.emp_id:<8} | Name: {self.name:<15} | Salary: ₹{self.salary:,.2f} | Category: {self.get_category()}"


class Company:
    def __init__(self, company_name: str):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, emp_id: str, name: str, salary: float):
        """Creates and adds a new employee to the company."""
        employee = Employee(emp_id, name, salary)
        self.employees.append(employee)
        print(f"Added: {name} (ID: {emp_id})")

    def display_all_employees(self):
        """Displays all employee details formatted nicely."""
        print(f"\n--- {self.company_name} Employee Directory ---")
        if not self.employees:
            print("No employees found.")
            return

        print("-" * 65)
        for emp in self.employees:
            print(emp)
        print("-" * 65)


#Example Usage
if __name__ == "__main__":
    tech_corp = Company("Tech Corp Solutions")

    # Adding employee details
    tech_corp.add_employee("EMP101", "Aarav Sharma", 85000)
    tech_corp.add_employee("EMP102", "Priya Patel", 52000)
    tech_corp.add_employee("EMP103", "Rohan Mehta", 32000)
    tech_corp.add_employee("EMP104", "Ananya Sen", 70000)

    # Displaying employee details and categories
    tech_corp.display_all_employees()

"""
OUTPUT : 

Added: Aarav Sharma (ID: EMP101)
Added: Priya Patel (ID: EMP102)
Added: Rohan Mehta (ID: EMP103)
Added: Ananya Sen (ID: EMP104)

--- Tech Corp Solutions Employee Directory ---
----------------------------------------------------------------------------------
ID: EMP101   | Name: Aarav Sharma    | Salary: ₹85,000.00 | Category: High Salary
ID: EMP102   | Name: Priya Patel     | Salary: ₹52,000.00 | Category: Medium Salary
ID: EMP103   | Name: Rohan Mehta     | Salary: ₹32,000.00 | Category: Low Salary
ID: EMP104   | Name: Ananya Sen      | Salary: ₹70,000.00 | Category: High Salary
----------------------------------------------------------------------------------
"""

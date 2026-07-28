def report_header(func):
    def wrapper(*args, **kwargs):
        print("=" * 20)
        print(" STUDENT REPORT")
        print("=" * 20)
        func(*args, **kwargs)
    return wrapper

class Report:
    college = "ABC Engineering College"
  
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    # Class method
    @classmethod
    def change_college(cls, new_name):
        cls.college = new_name

    # Magic method
    def __str__(self):
        return f"Name : {self.name}\nRoll No : {self.roll}\nMarks : {self.marks}"

    # Decorator used
    @report_header
    def display_report(self):
        print(f"College : {Report.college}")
        print(self)
        if self.marks >= 40:
            print("Result : PASS")
        else:
            print("Result : FAIL")

student1 = Report("Rahul", 101, 85)
student1.display_report()

print()

Report.change_college("XYZ Institute of Technology")

student2 = Report("Priya", 102, 35)
student2.display_report()

#OUTPUT
'''
====================
 STUDENT REPORT
====================
College : ABC Engineering College
Name : Rahul
Roll No : 101
Marks : 85
Result : PASS

====================
 STUDENT REPORT
====================
College : XYZ Institute of Technology
Name : Priya
Roll No : 102
Marks : 35
Result : FAIL
'''

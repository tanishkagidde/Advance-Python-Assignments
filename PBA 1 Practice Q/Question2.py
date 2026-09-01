'''
College Admission Management System
Develop a Python application to manage student admission records.
CO1 – Object-Oriented Programming
Create the following classes:
Applicant
Applicant Name 
Application ID 
Entrance Examination Score 
Categorize applicants as:
Merit List 
Waiting List 
Not Eligible 
Implement methods to display applicant details.
College
Add applicant records. 
Display all admission records. 
CO2 – Dynamic Programming
Implement the Longest Common Subsequence (LCS) algorithm using Dynamic Programming to determine the length of the longest common subsequence between two given strings.
'''
class Applicant:
    def __init__(self, applicant_name: str, application_id: str, entrance_score: float):
        self.applicant_name = applicant_name
        self.application_id = application_id
        self.entrance_score = entrance_score

    def get_admission_status(self) -> str:
        """Categorizes applicant based on entrance examination score."""
        if self.entrance_score >= 85:
            return "Merit List"
        elif 60 <= self.entrance_score < 85:
            return "Waiting List"
        else:
            return "Not Eligible"

    def display(self):
        """Displays applicant details directly."""
        print(self)

    def __str__(self) -> str:
        return f"ID: {self.application_id:<8} | Name: {self.applicant_name:<15} | Score: {self.entrance_score:<5.1f} | Status: {self.get_admission_status()}"


class College:
    def __init__(self, college_name: str):
        self.college_name = college_name
        self.applicants = []

    def add_applicant(self, applicant_name: str, application_id: str, entrance_score: float):
        """Creates and adds a new applicant record."""
        applicant = Applicant(applicant_name, application_id, entrance_score)
        self.applicants.append(applicant)
        print(f"Added: {applicant_name} (ID: {application_id})")

    def display_all_records(self):
        """Displays all admission records formatted nicely."""
        print(f"\n--- {self.college_name} Admission Directory ---")
        if not self.applicants:
            print("No applicant records found.")
            return

        print("-" * 75)
        for applicant in self.applicants:
            applicant.display()
        print("-" * 75)

if __name__ == "__main__":
    my_college = College("Apex Institute of Technology")

    my_college.add_applicant("Aarav Sharma", "APP101", 92.5)  
    my_college.add_applicant("Priya Patel", "APP102", 74.0)   
    my_college.add_applicant("Rohan Mehta", "APP103", 48.5)   
    my_college.add_applicant("Ananya Sen", "APP104", 85.0)    

    # Displaying all admission records
    my_college.display_all_records()

def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i = m
    j = n
    lcs = ""

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs = str1[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs, dp[m][n]

sequence1 = input("Enter the first sequence: ")
sequence2 = input("Enter the second sequence: ")

lcs, length = longest_common_subsequence(sequence1, sequence2)

print("\nLongest Common Subsequence:", lcs)
print("Length of LCS:", length)

'''
OUTPUT :
Added: Aarav Sharma (ID: APP101)
Added: Priya Patel (ID: APP102)
Added: Rohan Mehta (ID: APP103)
Added: Ananya Sen (ID: APP104)

--- Apex Institute of Technology Admission Directory ---
---------------------------------------------------------------------------
ID: APP101   | Name: Aarav Sharma    | Score: 92.5  | Status: Merit List
ID: APP102   | Name: Priya Patel     | Score: 74.0  | Status: Waiting List
ID: APP103   | Name: Rohan Mehta     | Score: 48.5  | Status: Not Eligible
ID: APP104   | Name: Ananya Sen      | Score: 85.0  | Status: Merit List
---------------------------------------------------------------------------
Enter the first sequence: abcdef
Enter the second sequence: defghi

Longest Common Subsequence: def
Length of LCS: 3
'''

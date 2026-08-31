file1 = open("input.txt", "r")
lines = file1.readlines()

print("Number of lines: ",len(lines))

first_two_lines = lines[:2]

file1.close()

file2 = open("output.txt","w")
file2.writelines(first_two_lines)
file2.close()

print("First two lines written to output.txt")

'''
OUTPUT :
Number of lines:  4
First two lines written to output.txt

output.txt:
This is the first line.
This is the second lin
'''

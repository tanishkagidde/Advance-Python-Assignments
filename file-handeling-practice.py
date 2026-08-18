print("1. WRITE OPERATION")
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.write("Hello \n")
file1.writelines(L)
file1.close()
print("Data written successfully.")

print("\n2. CHECKING FILE PROPERTIES")
f = open("myfile.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed before close():", f.closed)
f.close()
print("Is Closed after close():", f.closed)

print("\n3. READ OPERATION)")
file1 = open("myfile.txt", "r+")
print("Output of Read function is:")
print(file1.read())
file1.close()

print("4. READLINE() OPERATION")
file1 = open("myfile.txt", "r")
print("Output of Readline function is:")
print(file1.readline())
file1.close()

print("5. READLINES() OPERATION")
file1 = open("myfile.txt", "r")
print("Output of Readlines function is:")
print(file1.readlines())
file1.close()

print("\n6. FILE POINTER MOVEMENTS USING seek() AND tell()")
file1 = open("myfile.txt", "r")
print("Current pointer position:", file1.tell())
file1.seek(0)
print("Output of Read(9) function is:")
print(file1.read(9))
print("Pointer position after read(9):", file1.tell())
file1.close()

print("\n7. READ FILE LINE BY LINE USING LOOP")
file1 = open("myfile.txt", "r")
for line in file1:
    print(line.strip())
file1.close()

print("\n8. APPEND OPERATION ('a' mode)")
file1 = open("myfile.txt", "a")
file1.write("Today \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after appending:")
print(file1.readlines())
file1.close()

print("\n9. AUTOMATIC CLOSING WITH 'with' STATEMENT")
with open("myfile.txt", "r") as file:
    content = file.read()
    print(content)

print("10. EXCEPTION HANDLING (try...finally)")
try:
    file = open("myfile.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()
"""
OUTPUT : 
1. WRITE OPERATION
Data written successfully.

2. CHECKING FILE PROPERTIES
Filename: myfile.txt
Mode: r
Is Closed before close(): False
Is Closed after close(): True

3. READ OPERATION)
Output of Read function is:
Hello 
This is Delhi 
This is Paris 
This is London 

4. READLINE() OPERATION
Output of Readline function is:
Hello 

5. READLINES() OPERATION
Output of Readlines function is:
['Hello \n', 'This is Delhi \n', 'This is Paris \n', 'This is London \n']

6. FILE POINTER MOVEMENTS USING seek() AND tell()
Current pointer position: 0
Output of Read(9) function is:
Hello 
Th
Pointer position after read(9): 10

7. READ FILE LINE BY LINE USING LOOP
Hello
This is Delhi
This is Paris
This is London

8. APPEND OPERATION ('a' mode)
Output of Readlines after appending:
['Hello \n', 'This is Delhi \n', 'This is Paris \n', 'This is London \n', 'Today \n']

9. AUTOMATIC CLOSING WITH 'with' STATEMENT
Hello 
This is Delhi 
This is Paris 
This is London 
Today 

10. EXCEPTION HANDLING (try...finally)
Hello 
This is Delhi 
This is Paris 
This is London 
Today 
"""

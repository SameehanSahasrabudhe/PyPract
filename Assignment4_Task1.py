# Assignment 4

# Task 1: Read a File and Handle Errors
try:
    file = open('Sample1.txt', 'r')
    content = file.read()
    print(content)
    file.close()

except Exception as e:
    if isinstance(e, FileNotFoundError):
        print("The file 'Sample1.txt' was not found.")
    else:
        print("Error:", e)
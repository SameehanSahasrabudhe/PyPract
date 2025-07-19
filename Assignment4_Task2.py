# Assignment4_Task2

# Task 2: Write and Append Data to a File

# Writing data to a file
input_data = input("Enter a text to write to the file: ")
try:
    with open('Output.txt', 'w') as file:
        file.write(input_data + '\n')
        print("Data written to Output.txt successfully.")
except Exception as e:
    print("Error:", e)


# Appending the data to the same file
next_input = input("Enter the next line to append in the file: ")

try:
    with open('Output.txt', 'a') as file:
        file.write(next_input)
        print("Data successfully appended.")
except Exception as e:
    print("Error:", e)


# Reading the content of the file to verify
try:
    with open('Output.txt', 'r') as file:
        content = file.read()
        print("content of Output.txt:\n", content)
except Exception as e:
    print("Error while rading the file:", e)


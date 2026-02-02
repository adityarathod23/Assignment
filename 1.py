# Task 1: Read a File and Handle Errors

file_name = "sample.txt.txt"

try:
    # Try to open and read the file
    with open(file_name, "r") as file:
        print("Reading file content:")
        
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")

except FileNotFoundError:
    # Handle the error if file does not exist
    print(f"Error: The file '{file_name}' was not found.")








# Task 2: Write and Append Data to a File

file_name = "output.txt"

# Step 1: Take input from the user and write to the file
text_to_write = input("Enter text to write to the file: ")

with open(file_name, "w") as file:
    file.write(text_to_write + "\n")

print("Data successfully written to output.txt.")

# Step 2: Take additional input and append to the same file
text_to_append = input("\nEnter additional text to append: ")

with open(file_name, "a") as file:
    file.write(text_to_append + "\n")

print("Data successfully appended.")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")

with open(file_name, "r") as file:
    content = file.read()
    print(content)

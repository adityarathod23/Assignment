 #Task 1

students = {
    "Yash": 85,
    "Govind": 78,
    "Aditya": 92
}
name = input("Enter the student's name: ")
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")



#Task 2

numbers = [1,2,3,4,5,6,7,8,9,10]
first_five = numbers[0:5]
reversed_list = first_five[::-1]

print("Original list:", numbers)
print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reversed_list)

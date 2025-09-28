# Task 1
num=int(input("Enter a number: "))

if num%2==0:
    print(f"\n{num} is an even number.")
else:
    print(f"\n{num} is an odd number. ")


# Task 2
a=0

for num in range(1,51):
    a+=num

print("the sum of numbers from 1 to 50: ",a)
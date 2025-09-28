# Task 1
def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial((n-1))
result=factorial(5)
print(result)

num=int(input("Enter a number: "))
print(f"factorial of {num} is: {factorial(num)}")


# Task 2
import math

num=float(input("Enter a number: "))


print(f"square root: {math.sqrt(num)}")
print(f"logarithm: {math.log(num)}")
print(f"sine: {math.sin(num)}")
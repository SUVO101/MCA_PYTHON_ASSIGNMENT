# 6. Write a python program to check whether the input integer is Fibonacci or not. 
# logic - Perfect Square Check
import math as m
# define check_perfect_square(number) function
def check_perfect_square(number):
    if number<=0:
        result=True
    else:
        root=int(m.sqrt(number))
        result=True if root*root==number else False
    return result
# define is_fibonacci_number(number) function
def is_fibonacci_number(number):
    condition1=5*(number*number)+4
    condition2=5*(number*number)-4
    status1=check_perfect_square(condition1)
    status2=check_perfect_square(condition2)
    return status1 or status2

number=int(input("Enter a number : "))
if(is_fibonacci_number(number)):
    print(f"{number} is a fibonacci number")
else:
    print(f"{number} is not a fibonacci number")
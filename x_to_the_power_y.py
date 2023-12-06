# 11.Write a python program to find the value of x to the power y using recursion with minimum 
# complexity and the values of x and y are given by the user. 

def calculate_power(x,y):
    if y<1:
        return 1
    else:
        return x*calculate_power(x,y-1)
    
print(calculate_power(6,3))

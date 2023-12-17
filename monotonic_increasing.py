# 7. Write a python program to check whether the input array is monotonic increasing or not. 
# 1,2,3....n is monotonic
# 2,5,4 is not monotonic
def check_monotonic_increasing(list):
    for index in range(0,len(list)-1):
        if list[index] <= list[index+1]:
            pass
        else:
            break
    else:
        return True
    return False

list=[]
n=int(input("Enter the number of elements : "))
for i in range(0,n):
    value=int(input(f"Enter {i+1} elements : "))
    list.append(value)
message="The input array is monotonic increasing" if check_monotonic_increasing(list) else "The input array is not monotonic increasing"
print(message)
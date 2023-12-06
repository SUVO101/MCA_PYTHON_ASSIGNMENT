# 8. Write a python program to find the duplicate elements from a list.

def find_duplicate_elements(list):
    duplicate_list=[]
    for item in list:
        list.remove(item)
        if item in list and item not in duplicate_list:
            duplicate_list.append(item)
    return duplicate_list

list=[1,2,3,4,4,5,1,3,3,7,7]
print(f"Actual list : {list}\nduplicate elements list : {find_duplicate_elements(list)}")

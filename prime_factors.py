# 9. Write a python program to find the prime factors of an integer. 
def prime_check(number):
    if number>=2:
        for i in range(2,number//2+1):
            if number%i==0:
                break 
        else:
            return True
    return False

def factor_calculate(number):
    prime_numbers=""
    for i in range(2,number):
        # we check whether the number is divisible by 'i' and verify if 'i' is a prime number 
        if number%i==0 and prime_check(i):
            prime_numbers+=str(i)+","
    return prime_numbers


n=int(input("Enter a number: "))
print(f"prime factors of {n} are - ",end="")
if(factor_calculate(n)==""):
    print(None) 
else:
    print(factor_calculate(n))          
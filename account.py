# 3. Write a program which will use the class “Account”. In this class, you have to use deposit() , 
# withdraw() and balance_enq(). 

class Account:
    def __init__(self):
        self.balence=0
    def deposit(self,amount):
        self.balence+=amount
        print(f"You have successfully deposited Rs. {amount}/-.")
    def withdraw(self,amount):
        self.balence-=amount
        print(f"You have successfully withdrawn Rs. {amount}/-.")
    def balance_enq(self):
        print(f"Total Amount : {self.balence} /-\n")

amit=Account()
amit.deposit(13000)
amit.withdraw(2000)
amit.balance_enq()
amit.withdraw(4000)
amit.balance_enq()

amit=Account()
amit.deposit(40000)
amit.withdraw(2000)
amit.balance_enq()
amit.withdraw(4000)
amit.balance_enq()
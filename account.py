# 3. Write a program which will use the class “Account”. In this class, you have to use deposit() , 
# withdraw() and balance_enq(). 

class Account:
    def __init__(self,name,no):
        self.holder_name=name
        self.account_no=no
        self.balence=0
    def deposit(self,amount):
        self.balence+=amount
        print(f"You have successfully deposited Rs. {amount}/-.")
    def withdraw(self,amount):
        self.balence-=amount
        print(f"You have successfully withdrawn Rs. {amount}/-.")
    def balance_enq(self):
        print(f"Total Amount : {self.balence} /-")

amit=Account('Amit sen','74100001203')
amit.deposit(13000)
amit.withdraw(2000)
amit.balance_enq()
amit.withdraw(4000)
amit.balance_enq()

amit=Account('Subhankar nath','74100001456')
amit.deposit(40000)
amit.withdraw(2000)
amit.balance_enq()
amit.withdraw(4000)
amit.balance_enq()
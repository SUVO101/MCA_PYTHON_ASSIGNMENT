#5. Write a python program that will accept the code and price of 5 items in a list. User will give the
# quantity as input. Display the total billing as like: 
# Item Price Quantity Total_amount
def calculate_bill(item_codes,item_price,item_quantity):
    all_total=0
    print(f"{'-'*58}")
    print(f"| {'Item':<15} | {'Price':<10} | {'Quantity':<3} | {'Total Amount':<8} |")
    print(f"+{'-'*17}+{'-'*12}+{'-'*10}+{'-'*14}+")
    for i in range(len(item_codes)):
        print(f"| {item_codes[i]:<15} | {item_price[i]:<10} | {item_quantity[i]:<8} | {item_price[i]*item_quantity[i]:<12} |")
        all_total+=item_price[i]*item_quantity[i]
    print(f"{'-'*58}")
    print(f"{'-'*34} {'Total Price : '}{round(all_total,2)}{' /-': <5}")

item_codes=['#item001','#item002','#item003','#item004','#item005']
item_price=[245.30,455.02,40,85,96.37]
item_quantity=[]
for item in item_codes:
    quantity=int(input("Enter the quantity for item - {item}: "))
    item_quantity.append(quantity)
calculate_bill(item_codes,item_price,item_quantity)
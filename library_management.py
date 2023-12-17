# 4. Write a python program which will keep track of the stock of books available in the library. In this 
# program, you will have to use the add() to add the books and also the display().
class library:
    def __init__(self):
        self.books_in_stock={}
    def add(self,book_name):
        if book_name in self.books_in_stock:
            self.books_in_stock[book_name] += 1
        else:
            self.books_in_stock[book_name] = 1
    def display(self):
        print(f"| {'Book':<15} | {'Stock':<10} |")
        print(f"+{'-'*17}+{'-'*12}+")
        for name,stock in self.books_in_stock.items():
            # print(f"Book - > {name}  , Stock - > {stock}")
            print(f"| {name:<15} | {stock:<10} |")

obj=library()
obj.add('Harry potter')
obj.add('Harry potter')
obj.add('python')
obj.add('learn c')
obj.add('learn c++')
obj.add('learn c')
obj.display()
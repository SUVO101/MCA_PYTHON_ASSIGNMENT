# 2. Write a python program which has the class “Circle”. Use a class variable to define the value of 
# constant “Pi”. Calculate the area and circumference of the circle with specified value. 
class circle:
    pi=3.14159
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return round((self.radius**2)*circle.pi,2)
    def circumference(self):
        return round(self.radius*2*circle.pi,2)

circle1=circle(1.3)
print(f"\nRadius = {circle1.radius}\nArea = {circle1.area()}\nCircumference = {circle1.circumference()}\n")

circle2=circle(3.2)
print(f"\nRadius = {circle2.radius}\nArea = {circle2.area()}\nCircumference = {circle2.circumference()}\n")
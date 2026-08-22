class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def calculate_area(self):
        return self.length*self.width

rect = Rectangle(length=10,width=3)
area = rect.calculate_area()
print(f"Area:{area}")
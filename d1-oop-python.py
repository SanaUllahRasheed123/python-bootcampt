# Github repository for OOP in Python:created today 22/08/2026

# print("Hello World")
            # ******OOP Day First *****************
# class Car:
#     def __init__(self,color,model,year):
#         self.color = color
#         self.model = model
#         self.year = year
        
#     def start(self):
#         return f"{self.model} is starting."

#     def stop(self):
#         return f"{self.model} is stopping."
    
    
# myCar = Car(color="red",model="Toyota",year=2020)

# print(myCar.color)
# print(myCar.model)
# print(myCar.start())
 

            # ******OOP Day First *****************

# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
        
#     def calculate_area(self):
#         return self.length*self.width

# rect = Rectangle(length=10,width=3)
# # print(rect.calculate_area())
# area = rect.calculate_area()
# print(f"Area:{area} answer")


            # ******OOP Day two *****************
            
# class Dog:
#     def __init__(self,name,brand):
#         self.name = name
#         self.brand = brand
        
#     def bark(self):
#         return f"{self.name} says woof"
    
# my_dog =Dog(name="Budyy",brand="Golden Retriever")
# print(my_dog.bark())



# class Dog:
#     def __init__(self,name,breed):
#         self.name=name
#         self.breed=breed
#     def bark(self):
#         return f"{self.name} say wolf"
    
# myDog=Dog(name="Buddy",breed="Golden Retriever")

# print(myDog.bark())
# print(f"Name of brand is: {myDog.breed}" )


# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
        
#     def area(self):
#         return 3.14 * self.radius **2
    
# my_circle = Circle(5)
 
# print("Area ", my_circle.area())

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def cal_area(self):
#         return 3.14 * self.radius
# my_circle=Circle(radius=10)

# print(my_circle.cal_area())



# class Dog:
#     # The Constructor method to initialize attributes
#     def __init__(self, name, breed):
#         self.name = name        # Instance attribute
#         self.breed = breed      # Instance attribute

#     # A Method (function inside a class)
#     def bark(self):
#         return f"{self.name} says Woof!"

# # Creating an object (instantiating the class)
# my_dog = Dog(name="Buddy", breed="Golden Retriever")

# # Accessing attributes and methods
# print(my_dog.name)        # Output: Buddy
# print(my_dog.bark())      # Output: Buddy says Woof!

# In Python, a class is a reusable blueprint or template used to create objects. It bundles together data (called attributes) and behaviors (called methods) into a single package.

# The Core Concept
# Class: The blueprint (e.g., a structural design for a house).Object: 
# The actual instance built from the blueprint (e.g., a physical house).
# Basic Syntax and ExampleHere is how you define a class and create an object from it using the standard class keyword

# class Dog:
#     # The Constructor method to initialize attributes
#     def __init__(self, name, breed):
#         self.name = name        # Instance attribute
#         self.breed = breed      # Instance attribute

#     # A Method (function inside a class)
#     def bark(self):
#         return f"{self.name} says Woof!"

# # Creating an object (instantiating the class)
# my_dog = Dog(name="Buddy", breed="Golden Retriever")

# # Accessing attributes and methods
# print(my_dog.name)        # Output: Buddy
# print(my_dog.bark())      # Output: Buddy says Woof!


# Key Components Explained__init__ Method: This is a special method known as a constructor. It runs automatically whenever you create a new object from the class, and it is used to assign values to the object's properties.self Parameter: This represents the specific instance of the object you are currently creating or modifying. You must include it as the first parameter in your class methods so Python can track which object is calling the function.Attributes: Variables bound to the class or object.Instance attributes: Unique to each object (like self.name above).Class attributes: Variables shared across every single instance of a class.Methods: Regular functions defined inside a class that dictate what actions the object can perform.Core Concepts of Object-Oriented Programming (OOP)Python classes allow you to use advanced OOP features to organize complex projects:1. InheritanceA new class can inherit variables and methods from an existing class. This helps you avoid repeating code.


# 1. InheritanceA new class can inherit variables and methods from an existing class. This helps you avoid repeating code.
# Parent Class
# class Animal:
#     def eat(self):
#         return "Eating..."

# # Child Class inherits from Animal
# class Cat(Animal):
#     def meow(self):
#         return "Meow!"

# my_cat = Cat()
# print(my_cat.eat())   # Output: Eating... (Inherited method)
# print(my_cat.meow())  # Output: Meow!

# class Animal:
#     def __init__(self,name, voice):
#         self.name= name
#         self.voice=voice
#     def eat(self):
#         return f"{self.voice} eating"
# class Cat(Animal):
#     def meow(self):
#         return f"{self.name} says meoow meow"
# my_cat = Cat(name="Milano",voice="Meat")

# print(my_cat.eat())
# print(my_cat.meow())




# 2. PolymorphismDifferent classes can share the same method names but act out behaviors differently.

# class Duck:
#     def sound(self): return "Quack!"

# class Cow:
#     def sound(self): return "Moo!"
# class Dog:
#     def sound(self): return "wow wow!"

# # A single loop can call the same method on completely different objects
# for animal in [Duck(), Cow(),Dog()]:
#     print(animal.sound())

# class Duck:
#     def sound(self):
#         return "Quack Qucak Quack!"
# class Cow:
#     def sound(self):
#         return "ehehe!"
# class Dog:
#     def sound(self):
#         return "barking.. g."
# for animal in [Duck(),Cow(),Dog()]:
#     print(animal.sound())


# Understanding the init method
# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model = model
        
#     def description(self):
#         return f"This car is a {self.brand} {self.model}"
    
# my_car = Car("Toyoto","Corrolla")
# print(my_car.description())

# class Book:
#     def __init__(self,title,author="Unknown"):
#         self.title = title
#         self.author = author
        
#     def details(self):
#         return f"{self.title} by {self.author}"
    
# my_book = Book("1984","George Orwell")
# author_book = Book("Untitled")

# print(my_book.details())
# print(author_book.details())

# Creating and using Objects

# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
        
    
# my_car=Car("Totyota","Camry")
# print(my_car.brand)

# my_car.model="Corrola"
# print(my_car.model)


# Multiple objects
# class Student:
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade
        
#     def introduce(self):
#         return f"My name is {self.name} , and I am in grade {self.grade}."
    
# student1 = Student("Alice","10th")
# student2= Student("Bob","12th")

# print(student1.introduce())
# print(student2.introduce())


# class vs instance variables

# class Dog:
#     species= "Canis Familiaris"
    
#     def __init__(self,name,age):
#         self.name= name
#         self.age=age
# dog1=Dog("Buddy",5)
# dog2=Dog("Milo",3)


# print(dog1.name)
# print(dog2.age)

# print(dog1.species)

# class Car:
#     wheels = 4
    
#     def __init__(self,brand,model):
#         self.brand= brand
#         self.model=model
        
# car1 =Car("Totyota","Camry")
# car2 = Car("Honda","Accord")

# car1.wheels = 3

# print(car1.wheels)
# print(car2.wheels)
# print(Car.wheels)


# ****** Understanding Methods

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance +=amount
#         return f"New balance: ${self.balance}" 
    
# account =BankAccount("John",1000)

# print(account.deposit(500))

# class Person:
#     _count = 0
    
#     def __init__(self,name):
#         self.name=name
#         Person._count += 1
        
        
#     @classmethod
        
#     def get_count(cls):
#         return cls._count
        
# p1 = Person("Jemill")
# p2 = Person("Nimra")
# print(p1.name)
# print(Person.get_count())
# print((Person.get_count()))

# class methods and clasmethod
# class Temperature:
#     def __init__(self,celsius):
#         self.celsius = celsius
        
#     @classmethod
    
#     def from_fahrenheit(cls,fahrenheit):
#         celsius=(fahrenheit-32)*5/9
#         return cls(celsius)
    
# temp = Temperature.from_fahrenheit(98.6)
# print(temp.celsius)


# static methods and staticmethod 

# class MathsUtils:
    
#     @staticmethod
    
#     def add(x,y):
#         return x+y
    
# result = MathsUtils.add(77,21)

# print(result)


# class TemperatureConverter:
    
#     @staticmethod
    
#     def celsius_to_farnheit(celsius):
#         return (celsius * 9/5) +32
    
# temp_fahrenheit=TemperatureConverter.celsius_to_farnheit(25)
# print(temp_fahrenheit)

# Method Overloading and Overrding

# class MathOperation:
#     def add(self,a,b=0,c=0):
#         return a+b+c
# math_op=MathOperation()

# print(math_op.add(2))
# print(math_op.add(2,3))
# print(math_op.add(2,3,4))

# class Animal:
#     def sound(self):
#         return "Some generic sound"
    
# class Dog(Animal):
#     def sound(self):
#         return "Bark"
    
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
    
# animals=[Animal(),Dog(),Cat()]
# for animal in animals:
#     print(animal.sound())


# *******Inheritence and Polymorphism
# class Animal:
    
#     def __init__(self,name):
#         self.name=name
        
#     def speak(self):
#         return f"{self.name} makes a sound"
    
# class Dog(Animal):
    
#     def speak(self):
#         return f"{self.name} barks"
    
# dog=Dog("Buddy")
# print(dog.speak())

# single and multiple inheritence

# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
        
#     def description(self):
#         return f"{self.brand} {self.model}"
# class Car(Vehicle):
#     def wheels(self):
#         return 4
    
# my_car =Car(brand="Toyota",model="Corolla")
# print(my_car.description())
# print(my_car.wheels())


#  Method Resolution Order(MRO)

# class A:
#     def greet(self):
#         return "Hello from A"
    
# class B(A):
#     pass

# class C(B):
#     pass

# obj = C()

# print(obj.greet())
# print(C.__mro__)


# class X:
#     def greet(self):
#         return "Hello from X"
# class Y:
#     def greet(self):
#         return "Hello from Y"
    
# class Z(X,Y):
#     pass

# obj =Z()

# print(obj.greet())
# print(Z.__mro__)


# **** Polymorphisim and Method Overriding

# class Bird:
#     def fly(self):
#         return "Bird is flying"
    
# class Sparrow(Bird):
#     def fly(self):
#         return "Sparrow is flying"
    
# class Ostrich(Bird):
#     def fly(self):
#         return "Ostrich is flying"
    
# def make_fly(bird):
#     print(bird.fly())
    
# sparrow=Sparrow()
# ostrich=Ostrich()

# make_fly(sparrow)
# make_fly(ostrich)


# class Animal:
#     def sound(self):
#         return "Some Generic animal sound"
    
# class Dog(Animal):
#     def sound (self):
#         return "bark"
    
# class Cat(Animal):
#     def sound(self):
#         return "Meow "
    
# def make_sound(animal):
#     print(animal.sound())
    


# dog=Dog()
# cat = Cat()

# make_sound(dog)
# make_sound(cat)


# Undersanding Encapsulation

# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance
        
#     def deposit(self,amount):
#         if amount > 0:
#          self.__balance+=amount
        
#     def withdraw(self,amount):
#         if amount <= self.__balance:
#             self.__balance-=amount
              
#     def get_balance(self):
#         return self.__balance
    
# account = BankAccount(10000)
# account.deposit(5000)
# account.withdraw(3000)

# print(account.get_balance())


# Public Protected and Private Attributes
    
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self._salary=salary
        
#     def display(self):
#         return f"Name: {self.name}, Salary: {self._salary}"
    
# class Manager(Employee):
#     def __init__(self,name,salary,department):
#         super().__init__(name,salary)
#         self.department=department
        
#     def display_manager(self):
#         return f"Manager Name : {self.name},Department:{self.department},Salary: {self._salary}"
    
# emp = Employee("John",5000)
# mgr=Manager("Alice",800000, "HR")

# print(emp.display())
# print(mgr.display_manager())

# print(emp.name)
# print(mgr._salary)

# Implementing abstraction with abstract base classes ABCs
    
# from abc import ABC,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
    
#     @abstractmethod
#     def perimeter(self):
#         pass
    
# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
        
#     def area(self):
#         return self.width*self.height

#     def perimeter(self):
#         return 2*(self.width+self.height)
        
# rect= Rectangle(5,10)

# print(f"Area of Rectangle: {rect.area()}")
# print(f"Perimeter of Rectangle : {rect.perimeter()}")

# Practical example of Encapsulation and Abstraction
# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.__balance=balance
        
#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance +=amount
#             print(f"Deposited: {amount}. New Balance: {self.__balance}")
#     def withdraw(self,amount):
#         if 0 < amount <=self.__balance:
#          self.__balance-=amount
#          print(f"Withdraw:{amount}.New Balance: {self.__balance}")
        
#         else:
#             print("Insufficient Function Invalid Amount")
#     def get_balance(self):
#         return self.__balance
    
# account=BankAccount("Junny",60000)
# account.deposit(40000)
# account.withdraw(20000)
# print(account.get_balance())


# from abc import ABC,abstractmethod
# from queue import Full

# class Employee(ABC):
#     def __init__(self,name):
#         self.name=name
        
#         @abstractmethod
        
#         def calculate_salary(self):
#             pass
        
        
# class FullTimeEmployee(Employee):
#     def __init__(self,name,salary):  
#         super().__init__(name)
#         self.salary=salary
        
#     def calculate_salary(self):
#         return self.salary
    
# emp = FullTimeEmployee("Bobi",40000)
# print(f"Salary of {emp.name}:{emp.calculate_salary()}")

# Module 6 Advanced OOP concepts
# Understanding Magic methods Operator Overloading

# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     def __str__(self):
#         return f"{self.title} by {self.author}"
    
# book1 = Book("1984","George Orwell")
# print(book1)

# class Vector:
#     def __init__(self,x,y):
#         self.x= x
#         self.y= y
        
#     def __add__(self, other):
#         return Vector(self.x+other.x,self.y+other.y)
    
#     def __str__(self):
#         return f"Vector({self.x},{self.y})"
    
# v1= Vector(2,3)
# v2 =Vector(4,5)

# v3=v1+v2
# print(v3)


# Creating custom Iterators and Generators

# class CountDown:
#     def __init__(self,start):
#         self.start = start
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current <=0:
#             raise StopIteration
#         else:
#             self.current -= 1
#             return self.current +1
    
# countdown = CountDown(5)
# for number in countdown:
#     print(number)


# def fibonacci(n):
#     a,b = 0,1
#     for _ in range(n):
#         yield a 
#         a,b=b,a+b
        
    
# fib = fibonacci(7)
# for num in fib:
#     print(num)

# Understanding composition vs Inheritence

# class Animal:
#     def __init__(self,name):
#         self.name = name
        
#     def speak(self):
#         return f"{self.name} makes a sound"
    
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} barks."
    
# dog = Dog("Buddy")
# print(dog.speak())


# class Engine:
#     def start(self):
#         return "Engine starts. "
    
# class Car:
#     def __init__(self,model):
#         self.model = model
#         self.engine = Engine()
        
#     def start(self):
#         return f"{self.model}: {self.engine.start()}"
    
# car = Car("Toyota")
# print(car.start()) 

# class Order:
#     def __init__(self,items):
#         self.items=items
        
#     def calculate_total(self):
#         return sum(self.items)
# class OrderPrinter: 
#     def print_order(self,order):
#         for item in order.items:
#             print(f"Item:{item}")
            
# order = Order([10,20,30])
# printer = OrderPrinter()

# print("Total:",order.calculate_total())
# printer.print_order(order) 
    
# Creating a GUI Application using OOP

# import tkinter as tk

# class MainWindow:
#     def __init__(self,root):
#         self.root=root
#         self.root.title("Simple GUI")
#         self.root.geometry("300x200")
        
#         self.label=tk.Label(root,text="Welcome for creating new python GUI")
#         self.label.pack()
        
# root = tk.Tk()
# app= MainWindow(root)
# root.mainloop()

# import tkinter as tk
# class MainWindow:
#     def __init__(self,root):
        
#         self.root=root
#         self.root.title("Interactive GUI")
#         self.root.geometry("300x200")
        
#         self.label = tk.Label(root,text="Click the button!")
#         self.label.pack()
        
#         self.button = tk.Button(root,text="Click Me",command=self.on_button_click)
#         self.button.pack()
#     def on_button_click(self):
#         self.label.config(text="Button Clicked")
        
# root= tk.Tk()
# app = MainWindow(root)
# root.mainloop()


# Project Building a Simple OOPBased Calculator 

class Character:
    def __init__(self,name,health):
        self.name=name
        self.health=health
        
    def display_info(self):
        print(f"Character:{self.name}")
        print(f"Health:{self.health}")
player=Character("Hero",100)
player.display_info()

class Enemy(Character):
    def __init__(self,name,health,damage):
        super().__init__(name,health)
        self.damage=damage
    
    def attack(self,other):
        other.health -=self.damage
        print(f"{self.name} attacks {other.name} for {self.damage} damages!")
        print(f"{other.name}'s health is now {other.health}")
        
player=Character("Hero",100)
enemy=Enemy("Goblin",50,10)

    
player.display_info()
enemy.display_info()

enemy.attack(player)
player.display_info()

# BY BY oop

# 31-08-2026 OOP completed
            
            
        
        
    

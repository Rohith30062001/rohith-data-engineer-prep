# Classes & Objects
# 	•	Class → A blueprint for creating objects. Defines attributes and methods.
# 	•	Object → An instance of a class.

class Employee:
    company = 'ABC Tech'
    def __init__(self, emp_id, emp_name):
        print('Constructor invoked')
        print(f'Emp id: {emp_id}')
        print(f'Emp name: {emp_name}')
        print(f'Company: {self.company}')

    def fun(self, salary):
        self.salary=salary
        print(f'salary: {self.salary}')

    def newfun(self, new_salary):
        self.salary = new_salary
        self.company = 'XYZ'
        print(self.salary)
        print(self.company)
    def check_company(self):
        print(self.company)
        
Employee.company='New_tech'

e = Employee(1,'rohith')
e.fun(100)
e.newfun(200)
e.check_company()
# 2. Instance vs Class Variables
# 	•	Instance variable → Belongs to a specific object (self.var).
# 	•	Class variable → Shared across all instances (defined directly in class).

# 3. Inheritance

# Allows one class to reuse properties/methods of another.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog()
dog.speak()  # inherited
dog.bark()

class Father:
    def skill(self): print("Gardening")

class Mother:
    def skill(self): print("Cooking")

class Child(Father, Mother):  # inherits both
    pass

c = Child()
c.skill()  # Output depends on MRO (Method Resolution Order)

# 4. Encapsulation
# 	•	Public (default) → accessible anywhere.
# 	•	Protected (_var) → convention: meant for subclass access.
# 	•	Private (__var) → name mangling prevents direct access.

class BankAccount:
    def __init__(self, balance):
        self._balance = balance   # protected
        self.__pin = 1234         # private
    
    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        if new_balance > 0:
            self._balance = new_balance

acc = BankAccount(1000)
print(acc.get_balance())   # 1000
print(acc._balance)        # Not recommended, but possible
# print(acc.__pin)  # Error (private)

# 6. Polymorphism

# Means “many forms” → Same interface, different implementations.


# Abstraction in Python

# 📖 Definition:
# 	•	Abstraction means hiding implementation details and exposing only essential features to the user.
# 	•	It lets you focus on what an object does instead of how it does it.

# In Python, abstraction is mainly achieved using the abc (Abstract Base Class) module.
from abc import ABC, abstractmethod

class Vehicle(ABC):  # abstract base class
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with key")
    
    def stop_engine(self):
        print("Car engine stopped")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with kick")
    
    def stop_engine(self):
        print("Bike engine stopped")

# Abstract class cannot be instantiated:
# v = Vehicle()  ❌

vehicles = [Car(), Bike()]
for v in vehicles:
    v.start_engine()
    v.stop_engine()
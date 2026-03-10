# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:18:00 2026

@author: hirwa
"""

class Counter: 
    def init(self):
        self.count = 0 
        def increment(self): 
            self.count += 1
            c = Counter() 
            c.increment()
            print(c.count)


class Dog:
    # Class attribute
    species = "Canis"

    # Constructor (__init__) to initialize object attributes
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

    # Another instance method
    def description(self):
        return f"{self.name} is {self.age} years old."

class GoldenRetriever(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.color = color  # New attribute for GoldenRetriever

    # Override a method (optional)
    def bark(self):
        return f"{self.name} says Happy Woof!"

    def retrieve(self, item):
        return f"{self.name} retrieves the {item}."


# Create a GoldenRetriever object
my_golden = GoldenRetriever("Max", 5, "Golden")
print(f"\nSpecies: {my_golden.species}")
print(my_golden.description())
print(f"Color: {my_golden.color}")
print(my_golden.bark())         # Calls the overridden method
print(my_golden.retrieve("ball"))
# Class decorator to add greet method
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Apply the class decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        return f"My name is {self.name}"

# Creating an instance of Person
person = Person("Alice")

# Calling the greet method added by the decorator
print(person.greet())  # Output: Hello from Decorator!
print(person.say_name())  # Output: My name is Alice

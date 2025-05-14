class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Create an object of Multiplier
double = Multiplier(2)
triple = Multiplier(3)

# Check if the object is callable
print("Is 'double' callable?", callable(double))  # Output: True

# Use the object like a function
print("double(5):", double(5))  # Output: 10
print("triple(5):", triple(5))  # Output: 15

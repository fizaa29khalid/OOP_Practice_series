from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        # Abstract method, must be implemented by subclasses
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # Implement the abstract method
        return self.width * self.height

# Example usage
rectangle = Rectangle(5, 3)
print(f"The area of the rectangle is: {rectangle.area()}")

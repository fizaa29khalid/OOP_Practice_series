class Car:
    # Public variable
    brand = "Toyota"

    def start(self):
        # Public method
        print(f"The {self.brand} car has started.")


# Example usage
my_car = Car()  # Create an instance of the Car class

# Accessing public variable and method from outside the class
print(f"Car brand: {my_car.brand}")  # Accessing the public variable
my_car.start()  # Calling the public method

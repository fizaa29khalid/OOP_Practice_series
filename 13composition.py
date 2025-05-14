class Engine:
    def __init__(self, engine_type, horsepower):
        self.engine_type = engine_type
        self.horsepower = horsepower

    def start_engine(self):
        return f"{self.engine_type} engine with {self.horsepower} horsepower is starting."

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        # The Car class has an Engine object as a composition
        self.engine = engine

    def start_car(self):
        engine_status = self.engine.start_engine()
        return f"The {self.brand} car is ready to go! {engine_status}"

# Example usage
engine1 = Engine("V8", 450)  # Creating an Engine object
car1 = Car("Ford Mustang", engine1)  # Passing the Engine object to the Car

# Starting the car
print(car1.start_car())

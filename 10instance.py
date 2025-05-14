class Dog:
    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed

    def bark(self):
        # Instance method that prints a message with the dog's name
        print(f"{self.name} says: Woof! Woof!")

# Example usage
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Bella", "Beagle")

dog1.bark()  # Output: Buddy says: Woof! Woof!
dog2.bark()  # Output: Bella says: Woof! Woof!

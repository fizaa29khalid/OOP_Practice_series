class Counter:
    # Class variable to keep track of object count
    object_count = 0

    def __init__(self):
        # Each time a new object is created, increment the counter
        Counter.object_count += 1

    @classmethod
    def display_count(cls):
        # Class method to display the object count
        print(f"Total objects created: {cls.object_count}")


# Example usage
counter1 = Counter()  # Creates first object
counter2 = Counter()  # Creates second object
counter3 = Counter()  # Creates third object

# Displaying the count
Counter.display_count()  # Should print: Total objects created: 3

class Person:
    def __init__(self, name):
        # Constructor to initialize the name
        self.name = name

    def display(self):
        # Method to display the person's name
        print(f"Name: {self.name}")


class Teacher(Person):
    def __init__(self, name, subject):
        # Using super() to call the base class constructor (Person)
        super().__init__(name)
        self.subject = subject

    def display(self):
        # Overriding the display method to show both name and subject
        super().display()  # Calls Person's display method
        print(f"Subject: {self.subject}")


# Example usage
teacher = Teacher("John Doe", "Mathematics")
teacher.display()

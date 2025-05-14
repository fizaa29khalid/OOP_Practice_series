class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

# This part is necessary to actually run something
student1 = Student("Aamir", 85)
student1.display()

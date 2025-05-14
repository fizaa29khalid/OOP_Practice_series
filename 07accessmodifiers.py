class Employee:
    def __init__(self, name, salary, ssn):
        # Public variable
        self.name = name
        
        # Protected variable (typically intended for internal use)
        self._salary = salary
        
        # Private variable (should not be accessed outside the class)
        self.__ssn = ssn

    def display(self):
        # Display function to access all variables internally
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

# Example usage
employee = Employee("John Doe", 50000, "123-45-6789")

# Accessing public variable
print(f"Public (name): {employee.name}")

# Accessing protected variable
print(f"Protected (salary): {employee._salary}")

# Attempting to access private variable
try:
    print(f"Private (SSN): {employee.__ssn}")  # This will raise an error
except AttributeError as e:
    print(f"Error: {e}")

# Calling display method (accessing all variables internally)
employee.display()

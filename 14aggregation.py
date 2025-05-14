class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        return f"Employee: {self.name}, Position: {self.position}"

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        # Department holds a reference to Employee (aggregation)
        self.employee = employee

    def show_department_info(self):
        return f"Department: {self.department_name}, {self.employee.get_details()}"

# Example usage
emp1 = Employee("John Doe", "Software Engineer")  # Create an Employee object
dept1 = Department("IT Department", emp1)  # Department stores reference to Employee object

# Display department and employee details
print(dept1.show_department_info())

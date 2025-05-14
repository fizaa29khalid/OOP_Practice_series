class MathUtils:
    @staticmethod
    def add(a, b):
        # Static method to return the sum of a and b
        return a + b


# Example usage
result = MathUtils.add(5, 3)  # Using static method without creating an instance
print(f"The sum is: {result}")

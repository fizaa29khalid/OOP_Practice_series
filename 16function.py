# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")  # Log before function execution
        func()  # Call the original function
    return wrapper

# Function to which the decorator is applied
@log_function_call
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()

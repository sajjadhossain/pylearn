# Define a decorator function
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Apply the decorator to a function
@log_execution
def add(a, b):
    return a + b

# Call the decorated function
result = add(3, 5)
print(f"Result: {result}")

# Define a decorator that accepts arguments
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Apply the decorator with arguments
@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

# Call the decorated function
greet("Alice")
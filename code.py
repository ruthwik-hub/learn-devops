"""
A simple dummy script for testing purposes.
"""

def greet_user(name="Developer"):
    return f"Hello, {name}! This script is running perfectly."

def countdown(n):
    print(f"Starting a quick countdown from {n}:")
    for i in range(n, 0, -1):
        print(f"  {i}...")
    print("Done!")

if __name__ == "__main__":
    # 1. Test the greeting
    message = greet_user("User")
    print(message)

    # 2. Test the logic
    countdown(3)

    # 3. Simple math check
    result = 10 + 5
    print(f"Quick math: 10 + 5 = {result}")
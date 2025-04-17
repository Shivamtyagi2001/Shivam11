# multiply_two_numbers.py

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = multiply(num1, num2)
        print(f"The result of {num1} * {num2} is: {result}")
    except ValueError:
        print("Please enter valid numbers.")

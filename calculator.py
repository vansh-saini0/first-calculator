# -------------------------------
# 📌 Simple Python Calculator
# -------------------------------
# Supports: +, -, *, /, %, **, // with menu
# Made for GitHub Projects

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❗ Error: Division by Zero"
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def floor_division(a, b):
    if b == 0:
        return "❗ Error: Division by Zero"
    return a // b


def main():
    print("\n🔹 Simple Python Calculator 🔹")
    print("--------------------------------")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Floor Division (//)")
    print("0. Exit")
    print("--------------------------------")

    while True:
        choice = input("\nEnter choice (0-7): ")

        if choice == "0":
            print("👋 Exiting the calculator... Goodbye!")
            break

        if choice not in ['1','2','3','4','5','6','7']:
            print("❗ Invalid choice, try again!")
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        operations = {
            '1': ("Addition", add(a,b)),
            '2': ("Subtraction", subtract(a,b)),
            '3': ("Multiplication", multiply(a,b)),
            '4': ("Division", divide(a,b)),
            '5': ("Modulus", modulus(a,b)),
            '6': ("Power", power(a,b)),
            '7': ("Floor Division", floor_division(a,b)),
        }

        name, result = operations[choice]
        print(f"📌 {name} Result = {result}")

if __name__ == "__main__":
    main()

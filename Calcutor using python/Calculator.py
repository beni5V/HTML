print("=================================")
print("       Welcome to My Calculator")
print("=================================")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    result = num1 + num2
    print("The answer is:", result)

elif choice == "2":
    result = num1 - num2
    print("The answer is:", result)

elif choice == "3":
    result = num1 * num2
    print("The answer is:", result)

elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print("The answer is:", result)
    else:
        print("Sorry! You cannot divide by zero.")

else:
    print("Invalid choice. Please select a number from 1 to 4.")

print("\nThank you for using my calculator!")
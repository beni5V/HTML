# Dictionary
student = {
    "name": "Ali",
    "age": 15,
    "grade": "9th",
    "city": "Lahore"
}

# Ask the user to enter a key
key = input("Enter the key: ")

# Find and display the value
if key in student:
    print("Value:", student[key])
else:
    print("Key not found!")
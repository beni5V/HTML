# Python Quiz Program

print("===================================")
print("      Welcome to Python Quiz")
print("===================================\n")

score = 0

# Question 1
print("1. What is the correct file extension for Python files?")
print("a) .py")
print("b) .java")
print("c) .html")
print("d) .cpp")

answer = input("Enter your answer (a/b/c/d): ").lower()

if answer == "a":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is a) .py\n")

# Question 2
print("2. Which function is used to display output in Python?")
print("a) input()")
print("b) print()")
print("c) display()")
print("d) output()")

answer = input("Enter your answer (a/b/c/d): ").lower()

if answer == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is b) print()\n")

# Question 3
print("3. Which symbol is used for comments in Python?")
print("a) //")
print("b) <!-- -->")
print("c) #")
print("d) **")

answer = input("Enter your answer (a/b/c/d): ").lower()

if answer == "c":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is c) #\n")

# Question 4
print("4. Which keyword is used to create a function in Python?")
print("a) function")
print("b) define")
print("c) def")
print("d) fun")

answer = input("Enter your answer (a/b/c/d): ").lower()

if answer == "c":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is c) def\n")

# Question 5
print("5. Which data type is used to store text?")
print("a) int")
print("b) float")
print("c) string")
print("d) bool")

answer = input("Enter your answer (a/b/c/d): ").lower()

if answer == "c":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is c) string\n")

# Final Score
print("===================================")
print("Quiz Completed!")
print("Your Score:", score, "/5")

if score == 5:
    print("Excellent! 🎉")
elif score >= 3:
    print("Good Job! 👍")
else:
    print("Keep Practicing! 📚")
print("===================================")
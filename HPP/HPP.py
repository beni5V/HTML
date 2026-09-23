#for loop for Strings
str = "codingal"
for char in str:
    print(char)

print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

#For loop for Numeric Values
#Range (start_val, end_val+1, step_val)
for i in range(0,16,3):
    print(i)

print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

#Nested for loop
adj = ["red", "healthy","tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

#While loop
i = 1
while i < 10000000:
    print(i)
    i += 1
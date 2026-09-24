#To write the multiplication table of 35.
for i in range(1,11):
    print(f"35x{i}= {35*i}")

#To print no.s 1-20.
for i in range(1,21):
    print(i)

#To check if a number is prime or not.
num = int(input("Enter a number:"))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")



















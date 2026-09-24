# Armstrong number.
num = int(input("Enter a number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

if a**3 + b**3 + c**3 == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
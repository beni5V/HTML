def is_disarium(num):
    temp = num
    digits = str(num)
    total = 0

    for i in range(len(digits)):
        total += int(digits[i]) ** (i + 1)

    if total == num:
        return True
    else:
        return False


# Main Program
number = int(input("Enter a number: "))

if is_disarium(number):
    print(number, "is a Disarium Number.")
else:
    print(number, "is NOT a Disarium Number.")
def read_whole_number(prompt):
    """Return a whole number 0 or more, or None when nothing (or bad text) is typed."""
    try:
        text = input(prompt).strip()
    except EOFError:
        return None
    if text == "":
        return None
    if not text.isdecimal() or len(text) > 1000:
        print("Please type a whole number like 143 (digits only, at most 1000 of them).")
        return None
    return int(text)


def is_armstrong(n):
    """Return (True or False, digit steps). One step = one digit taken off with % 10."""
    d = len(str(n))
    total = 0
    steps = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total = total + digit ** d
        temp = temp // 10
        steps = steps + 1
    return total == n, steps


for n in [0, 1, 9, 10, 153, 154, 370, 371, 407, 9474]:
    ok, steps = is_armstrong(n)
    if ok:
        print(f"{n:>5} is an Armstrong no.    digit steps= {steps}")
    else:
        print(f"{n:>5} is not an Armstrong no.    digit steps= {steps}")
    
print()
n = read_whole_number(" Type a whole number to check (or press Enter to finish):")
if n is None:
    print("No no. checked")
else:
    ok, steps = is_armstrong(n)
    print(n, "is an Armstrong no.:", ok, "   digit steps =", steps)
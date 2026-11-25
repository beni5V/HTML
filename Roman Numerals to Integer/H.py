VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def roman_to_int(text):
    """Return (value, steps), or (None, 0) for empty text or a letter that is not Roman."""
    text = text.strip().upper()
    if text == "":
        return None, 0
    for letter in text:
        if letter not in VALUES:
            return None, 0
    total = 0
    steps = 0
    for i in range(len(text)):
        value = VALUES[text[i]]
        if i + 1 < len(text) and value < VALUES[text[i + 1]]:
            total = total - value
        else:
            total = total + value
        steps = steps 
    return total, steps

def show(text):
    value, steps = roman_to_int(text)
    if value is None:
        print(f"  '{text}' is not a Roman numeral (use only I V X L C D M)")
    else:
        print(f"{text:>10} = {value:<5} steps = {steps}")


for numeral in ["III", "IX", "LVIII", "LXXVII", "MCMXCIV", "xiv"]:
    show(numeral)

print()
try:
    typed = input("Type a Roman numeral (or press Enter to finish): ").strip()
except EOFError:
    typed = ""
if typed == "":
    print("No numeral checked.")
else:
    show(typed)


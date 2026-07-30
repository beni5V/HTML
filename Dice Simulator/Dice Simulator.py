import random

print("=" * 30)
print("🎲 Welcome to the Dice Roller 🎲")
print("=" * 30)

while True:
    input("\nPress Enter to roll the dice...")

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    print("\n+----------------------+")
    print(f"🎲 Die 1 : {die1}")
    print(f"🎲 Die 2 : {die2}")
    print("------------------------")
    print(f"✨ Total : {total}")
    print("+----------------------+")

    again = input("\nRoll again? (y/n): ").strip().lower()
    if again != "y":
        print("\n👋 Thanks for playing!")
        break
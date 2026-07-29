import random

choices = ["rock", "paper", "scissors"]

print("===================================")
print("   Rock, Paper, Scissors Game")
print("===================================")

computer = random.choice(choices)

player = input("Enter rock, paper, or scissors: ").lower()

if player not in choices:
    print("Invalid choice! Please enter rock, paper, or scissors.")
else:
    print("\nYou chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("🎉 You win!")

    else:
        print("😔 Computer wins!")

print("===================================")
    
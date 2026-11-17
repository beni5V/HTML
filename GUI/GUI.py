
import tkinter as tk
import random

player_score = 0
computer_score = 0

BG = "#F5F9FF"
TEXT = "#416A9C"
SCORE = "#DCEBFA"
ROCK = "#FFE5CC"
PAPER = "#DFF3E4"
SCISSORS = "#DCEBFA"
RESET = "#FADDE1"

def play_game(player_choice):
    global player_score, computer_score

    choices = ["✊ Rock", "✋ Paper", "✌️ Scissors"]
    computer_choice = random.choice(choices)

    you.config(text="👤 You chose: " + player_choice)
    computer.config(text="🤖 Computer chose: " + computer_choice)

    if player_choice == computer_choice:
        result.config(text="🤝 It's a tie!")

    elif (player_choice == "✊ Rock" and computer_choice == "✌️ Scissors") or \
         (player_choice == "✋ Paper" and computer_choice == "✊ Rock") or \
         (player_choice == "✌️ Scissors" and computer_choice == "✋ Paper"):
        player_score += 1
        result.config(text="🎉 Yay! You won!")

    else:
        computer_score += 1
        result.config(text="😢 Computer won!")

    score.config(text=f"🏆 You: {player_score}   🤖 Computer: {computer_score}")

def reset_game():
    global player_score, computer_score

    player_score = 0
    computer_score = 0

    you.config(text="👤 You chose: -")
    computer.config(text="🤖 Computer chose: -")
    result.config(text="🌟 Let's play!")
    score.config(text="🏆 You: 0   🤖 Computer: 0")

root = tk.Tk()
root.title("Rock Paper Scissors 🎮")
root.geometry("500x550")
root.config(bg=BG)
root.resizable(False, False)

tk.Label(root, text="🎮 ROCK PAPER SCISSORS",
         font=("Arial", 21, "bold"),
         bg=BG, fg=TEXT).pack(pady=25)

score = tk.Label(root, text="🏆 You: 0   🤖 Computer: 0",
                 font=("Arial", 15, "bold"),
                 bg=SCORE, fg=TEXT,
                 padx=15, pady=12)
score.pack(pady=15)

you = tk.Label(root, text="👤 You chose: -",
               font=("Arial", 13), bg=BG, fg=TEXT)
you.pack(pady=10)

computer = tk.Label(root, text="🤖 Computer chose: -",
                    font=("Arial", 13), bg=BG, fg=TEXT)
computer.pack(pady=10)

result = tk.Label(root, text="🌟 Let's play!",
                  font=("Arial", 19, "bold"),
                  bg=BG, fg=TEXT)
result.pack(pady=25)

frame = tk.Frame(root, bg=BG)
frame.pack()

buttons = [
    ("✊ Rock", ROCK),
    ("✋ Paper", PAPER),
    ("✌️ Scissors", SCISSORS)
]

for name, color in buttons:
    tk.Button(frame, text=name, bg=color, fg=TEXT,
              font=("Arial", 12, "bold"),
              width=11, height=3, relief="flat",
              command=lambda x=name: play_game(x)
              ).pack(side="left", padx=5)

tk.Button(root, text="🔄 Play Again",
          font=("Arial", 13, "bold"),
          bg=RESET, fg=TEXT,
          width=18, relief="flat",
          command=reset_game).pack(pady=35)

tk.Label(root, text="✨ Have fun playing! ✨",
         font=("Arial", 12), bg=BG,
         fg=TEXT).pack()

root.mainloop()

import tkinter as tk
import random
from tkinter import messagebox

choices = ["Rock", "Paper", "Scissors"]

player1_score = 0
player2_score = 0
player1_choice = None
mode = "computer"

# Winner Logic
def check_winner(choice1, choice2):
    if choice1 == choice2:
        return "Tie"
    elif (choice1 == "Rock" and choice2 == "Scissors") or \
         (choice1 == "Paper" and choice2 == "Rock") or \
         (choice1 == "Scissors" and choice2 == "Paper"):
        return "Player 1"
    else:
        return "Player 2"

# Play Function
def play(choice):
    global player1_choice, player1_score, player2_score

    if mode == "computer":
        computer = random.choice(choices)
        winner = check_winner(choice, computer)

        if winner == "Player 1":
            player1_score += 1
            result = "You Win!"
        elif winner == "Player 2":
            player2_score += 1
            result = "Computer Wins!"
        else:
            result = "Tie!"

        result_label.config(
            text=f"You: {choice} | Computer: {computer}\n{result}"
        )

    else:
        if player1_choice is None:
            player1_choice = choice
            result_label.config(text="Player 2 Turn")
        else:
            winner = check_winner(player1_choice, choice)

            if winner == "Player 1":
                player1_score += 1
                result = "Player 1 Wins!"
            elif winner == "Player 2":
                player2_score += 1
                result = "Player 2 Wins!"
            else:
                result = "Tie!"

            result_label.config(
                text=f"P1: {player1_choice} | P2: {choice}\n{result}"
            )
            player1_choice = None

    score_label.config(
        text=f"Score: P1 {player1_score} - {player2_score} P2"
    )

# Mode Change
def set_mode(selected):
    global mode
    mode = selected
    messagebox.showinfo("Mode", f"Mode changed to {mode}")

# Window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("700x550")
root.configure(bg="#0A0014")

title = tk.Label(root, text="🎮 ROCK PAPER SCISSORS",
                 font=("Arial", 24, "bold"),
                 bg="#0A0014", fg="#FF00FF")
title.pack(pady=20)

# Mode Buttons
mode_frame = tk.Frame(root, bg="#0A0014")
mode_frame.pack()

tk.Button(mode_frame, text="Vs Computer",
          command=lambda: set_mode("computer"),
          bg="purple", fg="white").pack(side="left", padx=10)

tk.Button(mode_frame, text="2 Player",
          command=lambda: set_mode("2player"),
          bg="blue", fg="white").pack(side="left", padx=10)

score_label = tk.Label(root,
                       text="Score: P1 0 - 0 P2",
                       font=("Arial", 16),
                       bg="#0A0014",
                       fg="white")
score_label.pack(pady=20)

# Choice Buttons
for choice in choices:
    tk.Button(root,
              text=choice,
              command=lambda c=choice: play(c),
              font=("Arial", 18, "bold"),
              bg="#4C1D95",
              fg="white",
              width=15).pack(pady=8)

result_label = tk.Label(root,
                        text="Choose Game Mode",
                        font=("Arial", 18),
                        bg="#0A0014",
                        fg="cyan")
result_label.pack(pady=30)

root.mainloop()
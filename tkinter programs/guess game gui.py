from tkinter import *
import random
import winsound


# Setup main window
root = Tk()
root.title("Guess the Number Game")
root.geometry("350x250")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Track number of attempts
attempts = 0

# Function to check the guess
def check_guess():
    global attempts
    guess = guess_entry.get()
    
    if not guess.isdigit():
        result_label.config(text="❗ Enter a valid number.")
        return
    
    guess = int(guess)
    attempts += 1
    
    if guess < secret_number:
        winsound.MessageBeep(winsound.MB_ICONHAND)  # Beep for wrong
        result_label.config(text="📉 Too low! Try again.")
    elif guess > secret_number:
        winsound.MessageBeep(winsound.MB_ICONHAND)  # Beep for wrong
        result_label.config(text="📈 Too high! Try again.")
    else:
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)  # Beep for correct
        result_label.config(text=f"🎉 Correct! You guessed in {attempts} tries.")
        guess_button.config(state=DISABLED)



# Function to reset the game
def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    result_label.config(text="")
    guess_entry.delete(0, END)
    guess_button.config(state=NORMAL)

# Title label
title_label = Label(root, text="Guess the Number (1-100)", font=("Arial", 14))
title_label.pack(pady=10)

# Entry box
guess_entry = Entry(root, font=("Arial", 12))
guess_entry.pack()

# Guess button
guess_button = Button(root, text="Guess", font=("Arial", 12), command=check_guess)
guess_button.pack(pady=5)

# Result message
result_label = Label(root, text="", font=("Arial", 12))
result_label.pack()

# Reset button
reset_button = Button(root, text="Reset Game", font=("Arial", 10), command=reset_game)
reset_button.pack(pady=10)

# Start GUI loop
root.mainloop()

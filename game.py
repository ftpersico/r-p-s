import random
import os
from dotenv import load_dotenv

#Import the user's name from the .env file
user_name = os.getenv("USER_NAME", default="Player One")

# Start game

print("Welcome", user_name, "to the game!")

print("Rock, Paper, Scissors, Shoot!")

# ask user to input a value
selection = input("Please Select 'Rock', 'Paper', or 'Scissors': ")

# validate that inputs are expected values. If not expected, halt the program.
if (selection != "Rock") and (selection != "Paper") and (selection != "Scissors"):
    print("You've input an invalid value. Please start the game again.")
    exit()

print("Your Choice:", selection)

# Have the computer make a selection for the game
arr = ["Rock", "Paper", "Scissors"]

comp_selection = random.choice(arr)

print("Computer Choice:", comp_selection)

# Compare the results
if (selection == "Rock" and comp_selection == "Rock") or (selection == "Paper" and comp_selection == "Paper") or (selection == "Scissors" and comp_selection == "Scissors"):
    print("It's a tie. Thank you and please play again.")
    exit()

if (selection == "Rock" and comp_selection == "Scissors") or (selection == "Paper" and comp_selection == "Rock") or (selection == "Scissors" and comp_selection == "Paper"):
    print("You won! Thank you and please play again.")
    exit()

if (selection == "Rock" and comp_selection == "Paper") or (selection == "Paper" and comp_selection == "Scissors") or (selection == "Scissors" and comp_selection == "Rock"):
    print("Too bad, you lost. Thank you and please play again.")
    exit()


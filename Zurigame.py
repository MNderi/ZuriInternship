import random

print("Play Rock Paper Sciscors againts the computer")
while True:
  PossiblePicks=['rock','paper','scissors']
  PlayerChoice=input("What is your choice, rock, paper or sissors? ")
  ComputerChoice=random.choice(PossiblePicks)
  if PlayerChoice not in PossiblePicks:
    print("invalid input, Lets try that again?")
  
  if PlayerChoice in PossiblePicks:
    print(f"\nYou chose {PlayerChoice}, computer chose {ComputerChoice}.\n")
    if PlayerChoice ==ComputerChoice:
        print(f"It's a tie! Your answer equal computer's")
    elif PlayerChoice == "rock":
        if ComputerChoice == "scissors":
            print("Rock breaks scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif PlayerChoice == "paper":
        if ComputerChoice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose):")
    elif PlayerChoice == "scissors":
        if ComputerChoice== "paper":
            print("Scissors cut paper! You win!")
        else:
            print("Rock breaks scissors! You lose.")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
      break
   

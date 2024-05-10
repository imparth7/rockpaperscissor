import random

def getUserChoice():
    user = input("Enter  your choice (R: rock | P: paper | S: scissors): ").lower()
    while user not in ['r', 'p', 's']:
        print("Invalid choice! Please enter R:rock | P:paper | S:scissors.")
        user = input("Enter your choice (R: rock | P: paper | S: scissors): ").lower()
    if user == 'r':
        return 'rock'
    elif user == 's':
        return 'scissor'
    elif user == 'p':
        return 'paper'


def getComputerChoice():
    return random.choice(['rock', 'paper', 'scissor'])


def checkResult(user, computer):
    if(user == computer):
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissor') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissor' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer Wins!"


def playGame():
    print("Let's play Rock, Paper, Scissors!")
    while True:
        userChoice = getUserChoice()
        computerChoice = getComputerChoice()
        print(f"You chose: {userChoice}")
        print(f"Computer chose: {computerChoice}")
        print(checkResult(userChoice, computerChoice))
        playAgain = input("Do you want to play again? (yes/no): ").lower()
        if (playAgain == 'no' or playAgain == 'n'):
            print("Thanks for playing!")
            break
        elif (playAgain == 'yes' or playAgain == 'y'):
            print("New game starting...\n")
            continue

playGame()
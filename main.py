import random

#welcome messages
print("Welcome to nptl's Guessing Game")
name = input("Let the game know your name..\n")
print("\nHey..", name, "nice name :)")
print(
    "\nThe game is simple, first you'll choose between a coin and a dice. Then you'll guess the outcome of the coin-toss or dice-roll. We'll see if the outcome matches what you guessed."
)
print("\nSo, let's start", name, "\n----")

#defining variables
guess = ''
gameCount = 0
wins = 0
again = 1

#first choice
choice = input(
    "\nChoose either a Coin or a Dice\nEnter 'c' for coin, 'd' for dice\n")

#checking for correct input
while (choice != 'c' and choice != 'd'):
    choice = input("\nInvalid!\nEnter 'c' for coin, 'd' for dice\n")

#coin toss
while choice == 'c' and again == 1:
    playAgain = ''
    guess = input(
        "\nWe're tossing the coin now. Choose heads or tails\nEnter 'h' for heads, 't' for tails\n"
    )
    while (guess != 'h' and guess != 't'):
        guess = input("\nInvalid!\nEnter 'h' for heads, 't' for tails\n")
    gameCount += 1
    outcome = random.randint(0, 1)

    if outcome == 0:
        if guess == 'h':
            wins += 1
            print("\nHeads it is!\nYou", wins, "Computer", gameCount - wins,
                  "\n")
        else:
            print("\nUh oh..Heads it is.\nYou", wins, "Computer",
                  gameCount - wins, "\n")
    else:
        if guess == 't':
            wins += 1
            print("\nTails it is!\nYou", wins, "Computer", gameCount - wins,
                  "\n")
        else:
            print("\nUh oh..Tails it is.\nYou", wins, "Computer",
                  gameCount - wins, "\n")

    playAgain = input("\nToss the coin again? y/n\n")
    while (playAgain != 'y' and playAgain != 'n'):
        playAgain = input("\nInvalid!\nEnter 'y' for YES, 'n' for NO\n")
    if playAgain == 'y':
        again = 1
    else:
        again = 0

#dice roll
while choice == 'd' and again == 1:
    playAgain = ''
    guess = input(
        "\nWe're rolling the dice now. Enter a no. between 1 to 6.\n")

    while (guess.isdigit() == False) or (int(guess) < 1 or int(guess) > 6):
        guess = input("\nInvalid!\nEnter a no. between 1 to 6.\n")
    gameCount += 1
    outcome = random.randint(1, 6)

    if outcome == int(guess):
        wins += 1
        print("\n", outcome, "it is!\nYou", wins, "Computer", gameCount - wins)
    else:
        print("\nOops, the dice rolled", outcome, "\nYou", wins, "Computer",
              gameCount - wins)

    playAgain = input("\nRoll the dice again? y/n\n")
    while (playAgain != 'y' and playAgain != 'n'):
        playAgain = input("\nInvalid!\nEnter 'y' for YES, 'n' for NO\n")
    if playAgain == 'y':
        again = 1
    else:
        again = 0

#final score
if wins * 2 > gameCount:
    print("\n**********")
    print("\nThat was crazzzzyy", name, "!!!")
    print("Someone has beaten the computer for the first time!")
    print("\nTHE FINAL SCORE:")
    print("You", wins, "Computer", gameCount - wins)
elif wins * 2 == gameCount:
    print("\n**********")
    print("\nOooo that was close", name, "")
    print("Someone has matched the computer for the first time!")
    print("\nTHE FINAL SCORE:")
    print("You", wins, "Computer", gameCount - wins)
elif wins * 2 < gameCount:
    print("\n**********")
    print("\nThanks for playing", name, "")
    print("It's hard to beat the computer :(")
    print("\nTHE FINAL SCORE:")
    print("You", wins, "Computer", gameCount - wins)

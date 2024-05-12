import random

number = random.randint(1,100)

while True:
    userchoice = input("Guess the no or press 'Q' to Quit")
    if userchoice == "Q":
        print("-----Game Over------")
        break

    user = int(userchoice)
    if user == number:
        print("Congratulations you guessed it right!")
        break
    elif user < number:
        print("Guess higher number")
    else:
        print("Guess lower number")

    






import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

player = input("rock paper or scissors ")

print("pc:", computer)

if player == computer:
    print("tie")

elif player == "rock" and computer == "scissors":
    print("YOU win !")

elif player == "paper" and computer == "rock":
    print("YOU win!")

elif player == "scissors" and computer == "paper":
    print("YOU win!")

else:
    print("PC win!")


print (50*"*")


import random
number = random.randint(1, 100)

while True:
    guess = int(input("chos a num 1 to 100: "))

    if guess < number:
        print("go up!")
    elif guess > number:
        print("go down!")
    else:
        print("nice.............................a banana for you ")
        break
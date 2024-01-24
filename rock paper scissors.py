import random
number = 0
timePlayed = 100
while number < timePlayed:
    exit = str(input("type exit to exit:\n> "))
    if exit == "exit":
        quit()
    userMove = str(input("choose your move:\n> "))
    compMove = random.randint(1,3)
    #converts int to a move
    if compMove == 1:
        compMove = "scissors"
    elif compMove == 2:
        compMove = "paper"
    elif compMove == 3:
        compMove = "rock"
    #draw conditions
    print("the computer picked ",compMove)
    if userMove == "scissors" and compMove == "scissors":
        print("you draw")
    elif userMove == "paper" and compMove == "paper":
        print("you draw")
    elif userMove == "rock" and compMove == "rock":
        print("you draw")
    #win conditions
    if userMove == "scissors" and compMove == "paper":
        print("you win")
    elif userMove == "rock" and compMove == "scissors":
        print("you win")
    elif userMove == "paper" and compMove == "rock":
        print("you win")
    #losing conditions
    if userMove == "rock" and compMove == "paper":
        print("you lose")
    elif userMove == "paper" and compMove == "scissors":
        print("you lose")
    elif userMove == "scissors" and compMove == "rock":
        print("you lose")
    number = number
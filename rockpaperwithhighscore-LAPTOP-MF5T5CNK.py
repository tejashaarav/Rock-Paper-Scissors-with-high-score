import os
from os import read
import random


def rockpaperscissor(comp, a):
    if (comp == "scissor" and a == "rock") or (comp == "rock" and a == "paper") or (comp == "paper" and a == "scissor"):
        return False

    elif (comp == a):
        return None

    else:
        return True


game_count = 0
your_score = 0
compscore = 0

rounds = int(input("How many rounds do you wanna play\n"))
while game_count == 0:
    for i in range(rounds):
        a = input("rock/paper/scissor player 1\n")

        randomcomp = ["rock", "paper", "scissor"]
        comp = random.choice(randomcomp)

        if rockpaperscissor(comp, a) == True:
            print("You win")
            game_count += 1
            your_score += 1
        elif rockpaperscissor(comp, a) == False:
            print("You lose")
            game_count += 1
            compscore += 1
        else:
            print("its a draw")
            game_count += 1

        print(f"you chose {a} ;computer chose {comp}")

if your_score < compscore:
    print(
        f"your score is {your_score} and compscore is {compscore}....you lose")
elif your_score > compscore:
    print(
        f"your score is {your_score} and compscore is {compscore}....you win")
else:
    print(
        f"your score is {your_score} and compscore is {compscore}....tied match")


filesize = os.path.getsize("highscore.txt")

if filesize == 0:
    with open('highscore.txt', 'w') as f:
        f.write(str(your_score))


else:
    with open('highscore.txt', 'r') as f:
        highscore = int(f.read())
        if highscore < your_score:
            with open('highscore.txt', 'w') as f:
                f.write(str(your_score))

import random
print("======================================================SNAKE WATER GUN======================================================")

print("\nRULES:")
print("\n☺ Snake vs. Water: Snake drinks the water hence wins.\n")
print("☺ Water vs. Gun: The gun will drown in water, hence a point for water\n")
print("☺ Gun vs. Snake: Gun will kill the snake and win.\n")
print("☺ In situations where both players choose the same object, the result will be a draw.\n")
print('☺ Winning rules of the game SNAKE WATER GUN are:\n'+ "Snake vs Water -> Snake wins \n"+ "Snake vs Gun   -> Gun wins \n"+ "Water vs Gun   -> Water wins \n")

print("1.Snake\n2.Water\n3.Gun\n")
while True:
    ucount = 0
    ccount = 0
    n=int(input("Enter the value for how much round you want to play:"))
    for i in range(n):
        cchoise = random.choice(["snake","gun","water"])
        choice = int(input("\nEnter Your choice: "))
        uchoise = ""
        if(choice == 1):
            uchoise = "snake"
        elif(choice == 2):
            uchoise = "water"
        elif(choice == 3):
            uchoise = "gun"
        else:
            print("invalid input try again\n")

        if(cchoise == uchoise):
            print("\nThis round drawed")
            print("\nUser choise          ->", uchoise)
            print("Computer choise      ->", cchoise)
        elif(cchoise == "snake" and uchoise == "gun") or (cchoise == "gun" and uchoise == "water") or (cchoise == "water" and uchoise == "snake"):
            print("\nYou win the round")
            print("\nUser choise          ->", uchoise)
            print("Computer choise      ->", cchoise)
            ucount += 1
        else:
            print("\nComputer win the round")
            print("\nUser choise          ->", uchoise)
            print("Computer choise      ->", cchoise)
            ccount += 1

    if(ccount == ucount):
        print("\nYou both got same scores. ", ccount)
    elif(ccount > ucount):
        print(f"\nComputer wins this game with {ccount} scores. ")
    else:
        print(f"\nUser wins this game with {ucount} scores. ")
    break
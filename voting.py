#---------------------------------------------------VOTING-----------------------------------------------------------------
print("----------------------------------------Welcome to the Voting-------------------------------------------------------")
x = int(input("Do you want to vote?\nEnter 0 for Yes and 1 for No:"))
match x:
    case 0:
        print("You want to vote!")
        age = int(input("Enter your age: "))
        if (age >= 18):
            print("You can vote.")
            name = int(input("Whom do you want to vote:\n1.Priyanshi\n2.Meera\n3.Riya\n"))
            if (name == 1):
                print("Your vote is registered for Priyanshi!")
            elif (name == 2):
                print("Your vote is registered for Meera!")
            elif (name == 3):
                print("Your name is registered for Riya!")
            else:
                print("Invalid Entry! Try Again.")
        else:
            print("You cannot vote as your age is below 18.")  
    case 1:
        print("As your wish")
import random

while True:
    choises=["rock","paper","scissors"]
    player=None
    computer=random.choice(choises)
 
    while player not in choises: 
        player=input("please choise ROCK,PAPER,SCİSSORS :").lower()

    if player==computer:
        print("It's a tie!")

    elif player=="rock":
        if computer=="scissors":
            print("You win!")
        elif computer=="paper":
            print("Computer wins!")
        
    elif player=="paper":
        if computer=="rock":
            print("You win!")
        elif computer=="scissors":
            print("Computer wins!")    

    elif player=="scissors":
        if computer=="paper":
            print(f"You win! computer choise{computer}")
        elif computer=="rock":
            print("Computer wins!")


    againPlay=input("do you want to again play? (yes/no):").lower()
    if againPlay != "yes":
        break
print("BYE!")
    

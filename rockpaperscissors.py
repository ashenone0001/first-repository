import random
use=0
comp = 0
while True :
    user = input("whats ur choice ? r for rock p for paper s for sicors")
    computer = random.choice(["r","p","s"])
    if user ==computer :
        print("draw")
        q = input("do u want to play more")
        if q == 'no':
            print(f"u have won {use} times and lost {comp} times")
            break
    elif user == 'r' :
        if computer == "p":
            print("sad! u have lost ")
            comp = comp+1
        else :
            print("wow i have won")
            use = use +1
        q = input("do u want to play more")
        if q == 'no':
            print(f"u have won {use} times and lost {comp} times")
            break
    elif user == 'p' :
        if computer == "s":
            print("sad! u have lost ")
            comp = comp+1
        else :
            print("wow i have won")
            use = use +1
        q = input("do u want to play more")
        if q == 'no':
            print(f"u have won {use} times and lost {comp} times")
            break
    elif user == 's' :
        if computer == "r":
            print("sad! u have lost ")
            comp = comp+1
        else :
            print("wow i have won")
            use = use +1
        q = input("do u want to play more")
        if q == 'no':
            print(f"u have won {use} times and lost {comp} times")
            break

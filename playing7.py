while True :
    p1 =input("what is ur move")
    p2 = input("what is ur move")
    if p1 == p2 :
        print("its a draw no one win")
    elif p1 == "rock" :
        if p2 == "scissors" :
            print("player one win")
        else :
            print("player 2 win")
    elif p1 == "paper" :
        if p2 == "scissors" :
            print("player 2 win")
        else :
            print("player one win")
    elif p1 == "scissors" :
        if p2 == "rock" :
            print("player 2 win")
        else :
            print("player one win")
    a = input("do u want to play more ?")
    if a == "no":
        break
    else :
        print("___________________________________________________________________________________________________________________________________________________________________________________________________________________")

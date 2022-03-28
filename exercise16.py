#first things first , the problem is we have to make a password genroetaor
import random
password_range ="a b c d f g h i j k l m n o p q r s t v w x y z 1 2 3 4 5 6 7 8 9 # @ A B C D F G H I J K L M N O P Q R S T V W X Y Z & % "
real_password_range = password_range.split() # i did those 2 steps coz it easier
while True :
    yesornow = input("do u want a new password ? ")
    try :
        if yesornow == 'no' :
            break
        elif yesornow == "yes" :
            long_of_password = int(input("how many charachter u want the passowrd have(please write in numbers) ?  "))
            try :
                num = 0
                password = []
                while long_of_password > num :
                    password.append(random.choice(real_password_range))
                    num = num +1
                print("".join(password))
            except :
                print("invalid input , enter a number")
    except :
        print("invalid input , type yes or no")

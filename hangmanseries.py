import random
with open('word_file2.txt' , 'r') as file:
    file1 = file.read()
file2 = file1.split()
def random_word() :
    return random.choice(file2)
word = random_word()
word = word.upper()
word = list(word) # what we did in those previous 8 lines of code is just take a words from a file and make it a list and take one of them randomly
user_solution = []
for i in range(len(word)):
    user_solution.append("_") #here we make the list we will have the guesses in , filled with "_" as many as the word have
tries = 6
third = [] #this list (i will explain it more later) just in case the word have letters are the same
while tries > 0 :
    print(user_solution)
    num = 0
    guess = input("what letter do u think its there ")
    if guess in word :
        for i in word :
            if guess == i: # if guess == any letter in the word (i) and at the same time its not repated , we will just append it to the user_solution list look line number 40
                if guess in user_solution : #that if the word have 2 similar letters
                    if guess in third : #that if the word have 3 similar letters
                        num +=1 #look under this line
                        for k in range(num,len(word)) : #imagine the word "exercise" when the user guess the first "e" , it will be added to the user_solution list , which its postion is "0"  , the code above that one (num+=1) will make num 1 here , so when the for loop iterate it will start from postion 1 in the word list  , and when the user guess the second e it will append in its correct place and num will became "2" and this process will continue
                            for n in word[num] :
                                if guess == n :
                                    user_solution[num] = guess
                                else :
                                    num +=1
                    third.append(guess)
                    num +=1
                    for k in range(num,len(word)) : # folow the same mechanism above
                        for n in word[num] :
                            if guess == n :
                                user_solution[num] = guess
                            else :
                                num +=1
                try :
                    user_solution[num] = guess
                except :
                    if guess in third and num == len(word): # i forget why i put this xd , but it has fixed a problem
                        print("false ! enter another letter")
                    else:
                        try :
                            num = num -1
                            user_solution[num] = guess
                        except :
                            print("false ! enter another letter")
                print(f"correct ! now ur guessing is {user_solution} " )
                break
            elif guess != i :
                num = num +1
    else :
        tries -=1
        print(f"false ! , u have {tries} tries left enter another letter") # that one if the user did a mistake
    if word == user_solution :
        print (f"u have guessed the word ! and its {user_solution}")
        break
    elif tries == 0 :
        print(f"sad u have lost , and the word was {word}")

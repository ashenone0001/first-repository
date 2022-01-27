sum = 0
number_of_subjects = 0
while True :
    number = input("enter your grades please")
    if number == "done":
        break
    else :
        sum_s = int(number)
        sum = sum + sum_s
        number_of_subjects = number_of_subjects + 1
grades= sum/number_of_subjects
if grades > 25 :
    print ("congrats ! u passed and your grade are is " , grades )
else :
    print (" sad u didnt make it :( but dont give up ! u can make it in the finals , and ur grade is" ,grades )    

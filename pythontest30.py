try :
    number1 = float(input("enter a number "))
    op = input ("enter ur opertion")
    number2 = float(input("enter a number "))
    if op == "+":
	    result =number1+number2
    elif op == "-":
        result =number1-number2
    elif op == '*':
     	result =number1*number2
    elif op == '/':
	    result =number1/number2
    print(result)
except :
	print ("enter a number please")

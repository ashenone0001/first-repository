file_name = input(" what is the file do u want ?")
dic = dict()
try :
    file = open(file_name)
    for lines in file :
        line =lines.rstrip()
        line = line.split()
        for soo in line :
            dic[soo] = dic.get(soo , 0) +1
    count = 0
    words = None
    for soo,sii in dic.items() :
        if sii == 0 or sii > count :
            count = sii
            words = soo
    print (count , words)

except :
    print("there is no file like that")

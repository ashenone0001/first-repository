class players :
    def __init__ (self , name , experience): #sooo , anyway , the __init__ is something like a fact or something we just use < and we use it for the purpse of make kind of input and output
        self.name = name
        self.experience = experience
    def intro (self):
        print("my name is" , self.name ,"and i have played for" , self.experience , "years ")#the (self) is refere to the vairbal it self (wow i use the word self xdd) anyway , so when the comuputer see self it will say okay this boy mean he will
                #use a virabl like he used under this line and give it some input so the (self) refer to the virabl which  is p1 and the (self.name ) refere to (p1.name) ok ??
p1 = players("ashen" ,2 )
#p1.name = 'ashen'
#p1.experience = 2
p2 = players('one ', 3)
#p2.name = 'one'
#p2.experience = 3
p1.intro()
p2.intro()

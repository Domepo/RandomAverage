import random
try:
    from font import welcomescreen
except:
    pass    

class cube():                                   
    
    def __init__(self,begin,end,how_often):
        self.anzahl = how_often     #e.g how often do want to roll the dice?           
        self.list = []              #store each number
        self.begin = begin          #e.g for a cube 1
        self.end = end              #e.g for a cube 6

    def versuche(self):
        for i in range(1,self.anzahl):     
            #range from 1 to "how_often"
            randomrange = random.randint(self.begin,self.end)
            #if you want to roll a dice = 1 , 6
            self.list.append(randomrange)
            #add the number to the list
        return self.list

    def anzahl_der_wuerfe(self):
         return self.anzahl
         #return "how_often" for later divisions

    def first_number(self):
        #for print function
        return self.begin

    def last_number(self):
        #for print function
        return self.end        
#FONT__
try:
    welcomescreen.font()
except:
    pass    
#FONT__

#CONFIG__


begin_number = 1 #beginning
end_number  = 6  #ending
quantity = 1000  #how_often

#####e.g for a dice

#CONFIG__

#CUBE__
wuerfel = cube(begin_number,end_number,quantity)    
#cube config with 1000 trys
summe_der_liste = sum(wuerfel.versuche())
#sum each number of the list
anzahl_der_versuche = wuerfel.anzahl_der_wuerfe()
average =  summe_der_liste / anzahl_der_versuche 
#calculate the average
#CUBE___



print("Randomized",anzahl_der_versuche,"times")
print("First number",wuerfel.first_number())
print("Second number", wuerfel.last_number())

print("------------------------")
print("The average is: ",average)

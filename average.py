import random
from font import welcomescreen

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
    
#FONT__
welcomescreen.font()
#FONT__
#CUBE__
wuerfel = cube(1,6,1000)    
#cube config with 1000 trys
summe_der_liste = sum(wuerfel.versuche())
#sum each number of the list
anzahl_der_versuche = wuerfel.anzahl_der_wuerfe()
average =  summe_der_liste / anzahl_der_versuche 
#calculate the average
#CUBE___


print("The average is: ",average)
print("Randomized",anzahl_der_versuche,"times")

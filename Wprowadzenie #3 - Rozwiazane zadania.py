#import random
#import sys
#import math
#zadanie 1
#A=[1/x for x in range(1,11,1)]
#B=[2 ** i for i in range(11)]
#C=[x for x in B if x % 4 == 0]
#zadanie 2
#m = [[random.randint(0, 9) for x in range (0, 4, 1)] for y in range (0, 4, 1)]
#p = [m[x][y] for x in range (0, 4, 1) for y in range (0, 4, 1) if x == y]
#print(m[0])
#print(m[1])
#print(m[2])
#print(m[3])
#print("Elementy znajdujące się na przekątnej : ",p)
#zadanie 3
#slownik = {'brzoskwinia': 'kg','maliny': 'dag','baton': 'sztuki',}
#slownik_odw = {value: key for key, value in slownik.items()}
#print("Słownik")
#print(slownik)
#print("Słownik odwrócony: ")
#print(slownik_odw)
#zadanie 4
#def monotonicznosc(a):
    #if (a<0):
        #print("Funkcja jest malejąca")
    #elif (a==0):
        #print("Funkcja jest stała")
    #elif (a>0):
        #print("Funkcja jest rosnąca")



#print (monotonicznosc(0))
#print (monotonicznosc(-1))
#print (monotonicznosc(1))
#zadanie 5
#sprawdzanie czy dwie proste są równoległe/prostopadłe
#y1=a1x+b1, y2=a2x+b2
#równoległe a1=a2, prostopadłe gdy a1a2=-1
#def sprawdzanie (a1,a2):
    #if (a1==a2):
        #print("Podane proste są równoległe")
    #elif (a1*a2==-1):
        #print("Podane proste są prostopadłe")
    #else:
        #print("Podane proste nie są równoległe jak i prostopadłe")

#print (sprawdzanie(-1,1))
#zadanie 6
#Podany wzór na równanie okręgu (x-a)^2+(y-b)^2=r^2
#def okrąg (x,a,y,b):
    #r=((x-a)**2+(y-b)**2)**0.5
    #return r
#print ("Długość promienia z podanych wartości wynosi: ")
#print (okrąg(0,0,0,0))

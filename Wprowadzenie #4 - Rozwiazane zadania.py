#import random
#import sys
#import math
lista = []
for x in range(1, 256, 1):
    if (x % 4 == 0):
       lista += [x]
file=open("podzielne.txt","w+")

file.writelines(str(lista))

file.close()
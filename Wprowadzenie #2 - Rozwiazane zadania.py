#import math
#import random
#import sys
    #zadanie 1.
    #Napisz skrypt, który pobiera od użytkownika zdanie i liczy w nim spacje. Wynik wyświetla na ekranie (użyj instrukcji input)
    #a = input("Podaj dowolne zdanie\n")
    #print("Podane zdanie to : "+a)
    #b=a.count(' ')
    #print("Liczba spacji w podanym zdaniu wynosi...")
    #print(b)
    #zadanie 2.
    #Napisz skrypt, który pobiera od użytkownika dwie wartości i mnoży je przez siebie. Wynik wyświetla na ekranie (użyj instrukcji readline() i write()).
#print("Podaj liczbę")
#a=sys.stdin.readline()
#print("Podaj kolejną liczbę")
#b=sys.stdin.readline()
#c=int(a)*int(b)
#print("Wynik mnozenia podanych liczb wynosi: ")
#sys.stdout.write(str(c))
    #zadanie 3.
    #Odszukaj w dokumentacji, jakie operatory można używać w instrukcjach warunkowych (np. równe, różne, mniejsze bądź równe itp.)
    #Odszukane, zastosuję je w póżniejszych zadaniach :)
    #zadanie 4.
    #Napisz skrypt, który pobiera od użytkownika liczbę i wypisuje na ekran wartość bezwzględną tej liczby
    #liczba=input("Podaj liczbe\n")
    #liczba=float(liczba)
    #print("Wartość bezwględna podanej liczby wynosi:")
    #b=math.fabs(liczba)
    #print(b)
    #zadanie 5.
    #Napisz skrypt, który pobiera od użytkownika trzy liczby a, b i c. Sprawdza następujące warunki:
    #czy a zawiera się w przedziale (0,10>
    #oraz czy jednocześnie a>b lub b>c.
    #Jeśli warunki są spełnione lub nie to ma się wyświetlić odpowiedni komunikat na ekranie.
#a=float(input("Podaj liczbę a\n"))
#b=float(input("Podaj liczbę b\n"))
#c=float(input("Podaj liczbę c\n"))
#if (a>0 and a <=10 and a>b or b>c):
    #print ("Tak")
#else:
    #print ("Nie")
#zadanie 6.
#for x in range(0, 51, 1):
    #if (x%5==0):
     #print(x)
#zadanie 7
#liczba = input("Podaj liczbe: ")
#liczba = liczba.split()
#dlugosc = len(liczba)
#for x in range(0, dlugosc, 1):
    #print(int(liczba[x])*int(liczba[x]))
#zadanie 8
#lista=[]
#while True:
    #n=input("Podaj liczbę:\n")
    #lista.append(n)
    #print("Dane wartosci w liscie",lista)
#zadanie 9.
#liczba=int(input("Wprowadz liczbę:"))
#tymczasowa=0
#while(liczba>0):
    #cyfra=liczba%10
    #tymczasowa=tymczasowa+cyfra
    #liczba=liczba//10
#print("Całkowita suma cyfr wynosi:",tymczasowa)
#Zadanie 10.
#for i in range(0, 6, 1):
    #for j in range(0, i+1, 1):
        #sys.stdout.write('A')
    #sys.stdout.write('\n')
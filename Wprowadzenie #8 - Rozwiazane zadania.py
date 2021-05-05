#zadanie 1
#Ponizsze biblioteki pobieramy komendą wpisywaną w terminalu bądż w cmd
#Podane komendy to:
#"pip install openpyxl" lub "-m pip install --upgrade pip'"
#"pip install pandas" wpisywane w cmd
#import pandas
#import openpyxl
#DataFrame = pandas.read_excel(pandas.ExcelFile("datasets/imiona.xlsx"), "ArkuszNarodziny")
#print(DataFrame)
#zadanie 2
#te same biblioteki co w zadaniu 1
#DataFrame = pandas.read_excel(pandas.ExcelFile("datasets/imiona.xlsx"), "ArkuszNarodziny")
#def a(DataFrame):
    #a) tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
    #print(DataFrame[DataFrame["Liczba"]>1000])
    #b) tylko rekordy gdzie nadane imię jest takie jak Twoje
#def b(DataFrame):
    #print(DataFrame[DataFrame["Imie"]=="Szymon" or "Wojtek"])
    #c) sumę wszystkich urodzonych dzieci w całym danym okresie
#def c(DataFrame):
    #print(DataFrame.agg({'Liczba': ['sum']}))
    #d) sumę dzieci urodzonych w latach 2000-2005
#def d(DataFrame):
    #Dzieci = DataFrame[(DataFrame["Rok"] >= 2000) & (DataFrame["Rok"] <= 2005)]
    #print(Dzieci.agg({"Liczba", ["sum"]}))

#import pandas
#import matplotlib.pyplot
#import openpyxl
#zadanie 1
#urodzenia = pandas.read_excel(pandas.ExcelFile("datasets do labow/imiona.xlsx"), "Arkusz1")
#wykres = urodzenia.groupby(["Rok"]).agg({"Liczba": ["sum"]})
#wykres.plot()
#matplotlib.pyplot.show()
#zadanie 2
#urodzenia = pandas.read_excel(pandas.ExcelFile("datasets do labow/imiona.xlsx"), "Arkusz1")
#wykres = urodzenia.groupby(["Plec"]).agg({"Liczba": ["sum"]})
#a = wykres.plot.bar()
#matplotlib.pyplot.show()

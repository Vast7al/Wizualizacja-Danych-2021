#import matplotlib.pyplot
#import numpy
#from sklearn import datasets
#pip install -U scikit-learn w cmd
#zadanie 1
#przedzial = range(1, 21)
#x= [1/x for x in przedzial]
#matplotlib.pyplot.plot(przedzial, x)
#matplotlib.pyplot.xlabel('x')
#matplotlib.pyplot.ylabel('f(x)')
#matplotlib.pyplot.legend()
#matplotlib.pyplot.show()
#zadanie 2
#przedzial = range(1, 21)
#x= [1/x for x in przedzial]
#matplotlib.pyplot.plot(przedzial, x,color='green', linestyle='dashdot',marker='>')
#matplotlib.pyplot.xlabel('x')
#matplotlib.pyplot.ylabel('f(x)')
#matplotlib.pyplot.legend()
#matplotlib.pyplot.show()
#zadanie 3
#x=numpy.linspace(0, 25, 100)
#matplotlib.pyplot.ylim([-1,1])
#sinx = numpy.sin(x)
#cosx = numpy.cos(x)
#matplotlib.pyplot.plot(x,sinx)
#matplotlib.pyplot.plot(x,cosx)
#matplotlib.pyplot.title("Wykres")
#matplotlib.pyplot.legend()
#matplotlib.pyplot.show()
#zadanie 4
#x=numpy.linspace(0, 30, 100)
#matplotlib.pyplot.ylim([-1,2.8])
#sinx = numpy.sin(x)+1.8
#cosx = numpy.cos(x)*-1.3
#matplotlib.pyplot.plot(x,sinx)
#matplotlib.pyplot.plot(x,cosx)
#matplotlib.pyplot.title("Wykres")
#matplotlib.pyplot.legend()
#matplotlib.pyplot.show()
#zadanie 5
#iris = datasets.load_iris()
#matplotlib.pyplot.scatter(iris.data[:, 3], iris.data[:, 2], c=iris.target,s=abs(iris.data[:,3]-iris.data[:, 2]))
#matplotlib.pyplot.show()

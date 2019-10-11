def mylist():
	print("LISTS")
	Movies = ["Into the wild", "Forrest Gump", "Sully"]
	print(len(Movies))
	Movies.insert(2, "Hangover")
	print(Movies)
	L1=[23,78,94,21,11]
	print(L1.pop())
	print(min(L1))
	sorted(L1)
	print(sum(L1))
	
def tuples1():
    print("TUPLES")
    sahtup=(1,2,3,"hello")
    print(sahtup[1:])
    print(len(sahtup))
    print(sahtup[::-1])
    print(tuple('sahana'))

def set1():
    print("SETS")
    seriesSet= {"Sherlock","Breaking bad","Friends","Modern Family"}
    seriesSet.add("Happy Halloween")
    rating={9.2,9.4,9.0,5.9}
    together= seriesSet|rating
    print(together)
    diff=seriesSet- rating
    print(diff)

def diction():
    print("DICTIONARY")
    diction1= {"blue": "color","rose": "flower","saucer":"utensil"}
    print(diction1)
    print(len(diction1))
    x=diction1["blue"]
    print(x)
    
mylist()
tuples1()
set1()
diction()



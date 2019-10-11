Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> Movies = ["Into the wild", "Forrest Gump", "Sully"]
>>> Movies.append("Titanic")
>>> print(Movies)
['Into the wild', 'Forrest Gump', 'Sully', 'Titanic']
>>> Movies.count()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Movies.count()
TypeError: count() takes exactly one argument (0 given)
>>> print(Movies.count())
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(Movies.count())
TypeError: count() takes exactly one argument (0 given)
>>> print(Movies.count(1))
0
>>> print(Movies.sort())
None
>>> print(len(Movies))
4
>>> Movies.insert(2, "Hangover")
>>> print(Movies)
['Forrest Gump', 'Into the wild', 'Hangover', 'Sully', 'Titanic']
>>> print(Movies.reverse())
None
>>> S=[45,23,11,09,788]
SyntaxError: invalid token
>>> S=[45,23,11,9,788]
>>> print(S.sort())
None
>>> print(sum(S))
876
>>> print(min(List))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(min(List))
NameError: name 'List' is not defined
>>> print(min(S))
9
>>> print(S.pop())
788
>>> print(S)
[9, 11, 23, 45]
>>> sorted(S)
[9, 11, 23, 45]
>>> sorted(Movies)
['Forrest Gump', 'Hangover', 'Into the wild', 'Sully', 'Titanic']
>>> Movies.sort(reverse=True)
>>> print(Movies)
['Titanic', 'Sully', 'Into the wild', 'Hangover', 'Forrest Gump']
>>> sahtup=(1,2,"hello")
>>> print(sahtup[1:])
(2, 'hello')
>>> print(len(sahtup))
3
>>> print(sahtup[::-1])
('hello', 2, 1)
>>> print(tuple('sahana'))
('s', 'a', 'h', 'a', 'n', 'a')
>>> ('s', 'a', 'h', 'a', 'n', 'a')('s', 'a', 'h', 'a', 'n', 'a')

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    ('s', 'a', 'h', 'a', 'n', 'a')('s', 'a', 'h', 'a', 'n', 'a')
TypeError: 'tuple' object is not callable
>>> sahtup1=(1,2,"HI")
>>> cmp(sahtup,sahtup1)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    cmp(sahtup,sahtup1)
NameError: name 'cmp' is not defined
>>> print(cmp(sahtup,sahtup1))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(cmp(sahtup,sahtup1))
NameError: name 'cmp' is not defined
>>> sahtup=sahtup1
>>> sahtup==sahtup1
True
>>> print(sahtup1)
(1, 2, 'HI')
>>> print(sahtup)
(1, 2, 'HI')
>>> print(sahtup.pop())
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(sahtup.pop())
AttributeError: 'tuple' object has no attribute 'pop'
>>> seriesSet= {"Sherlock","Breaking bad","Friends","Modern Family"}
>>> seriesSet.add("Happy Halloween")
>>> print(seriesSet)
{'Friends', 'Modern Family', 'Sherlock', 'Breaking bad', 'Happy Halloween'}
>>> rating={9.2,9.4,9.0,5.9}
>>> together= seriesSet|rating
>>> print(together)
{5.9, 'Friends', 'Modern Family', 9.2, 9.4, 9.0, 'Sherlock', 'Breaking bad', 'Happy Halloween'}
>>> inter=seriesSet&rating
>>> print(inter)
set()
>>> seriesSet.add(9.2)
>>> print(inter)
set()
>>> print(seriesSet)
{'Friends', 'Modern Family', 9.2, 'Sherlock', 'Breaking bad', 'Happy Halloween'}
>>> inter=seriesSet&rating
>>> print(inter)
{9.2}
>>> diff=seriesSet- rating
>>> print(diff)
{'Friends', 'Modern Family', 'Sherlock', 'Breaking bad', 'Happy Halloween'}
>>> print(seriesSet.symmetric_difference(rating))
{5.9, 'Friends', 9.4, 9.0, 'Modern Family', 'Sherlock', 'Breaking bad', 'Happy Halloween'}
>>> diction1= {"blue": "color","rose": "flower","saucer":"utensil"}
>>> print(diction1)
{'blue': 'color', 'rose': 'flower', 'saucer': 'utensil'}
>>> print(diction1.'blue')
SyntaxError: invalid syntax
>>> x=diction1["blue"]
>>> print(x)
color
>>> diction1["color"]= "red"
>>> print(diction1)
{'blue': 'color', 'rose': 'flower', 'saucer': 'utensil', 'color': 'red'}
>>> diction1["blue"]="red"
>>> print(diction1)
{'blue': 'red', 'rose': 'flower', 'saucer': 'utensil', 'color': 'red'}
>>> print(len(diction1))
4
>>> 

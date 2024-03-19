"""
import sys
print("Python Version: ", sys.version)

import numpy as np
print("Numpy Version: ", np.__version__)

import scipy as sp
print("Scipy Version: ", sp.__version__)

import matplotlib
print("matplotlib Version: ", matplotlib.__version__)

import pandas as pd
print("pandas Version: ", pd.__version__)

import sklearn
print("scikit-learn Version: ", sklearn.__version__)

import sympy
print("sympy Version: ", sympy.__version__)


import keyword
print(keyword.kwlist)

"""
s1={1,2,3} # set
print(type(s1))

s2=[1,2,3] # list
print(type(s2))

s3=(1,2,3) #tuple
print(type(s3))

s4=1,2,3 #tuple
print(type(s4))

s5={1:200} #dictionary
print(type(s5))


mid_scores=[75, 70, 55, 99, 70]
print(mid_scores)
mid_scores.sort()
print(mid_scores)
mid_scores.reverse()
print(mid_scores)
mid_scores.append(100)
print(mid_scores)
mid_scores.insert(2, 85)
print(mid_scores)
mid_scores.extend([100,88, 79])
print(mid_scores)

print("-------------------------------")

mytuple=('Gildong', 75, '100', False)
s1=mytuple[1:]
print(mytuple)
a=(10, 20)
b=(30, 40, 50)
s=a+b
print(s)
r=b*3
print(r)

d=((10,20), (30, 40, 50), (60, 70))
print(d[2])

x = [10,20,30]
y = ['apple','orange','banana']
z = ['cat', 'dog', 'monkey']
d = list(zip(x,y,z))
print(d)

print("---------------------")

mid_scores={'Gildong':75, 'Chulsoo':87, 'Soonhee':55}
mid_scores['Chulsoo']=95 # modify
mid_scores['Dongsoo']=67 # add
del mid_scores['Gildong'] # delete

mid_scores={'Gildong':75, 'Chulsoo':87, 'Soonhee':55}
print(mid_scores['Chulsoo'])
print(mid_scores.keys())
print(mid_scores.values())
print(mid_scores.items())
mydict=dict(mid_scores)
print(mydict)

mid_scores=[('Gildong',75), ('Chulsoo',87), ('Soonhee',55)]
mydict=dict(mid_scores)
print(mydict)
score=mydict['Chulsoo']
print(score)
scores=dict(Gildong=75, Chulsoo=87, Soonhee=55)
print(scores['Gildong'])

a = [1, 2, 3, 4, 5]
output = [num * 5 for num in a]
print(output)

try:
   print(1/0)
except:
   print("Something go wrong.")
else:
   print("It is OK.")
finally:
   print("The try-except is finished.")


print("---------week 3------------")


str = "Hong Gildong"
print(str)
print("{:/>20s}".format(str))
print("{:/<20s}".format(str))

number=123.456789123456789
print("num: {}".format(number))
# total digit=7, decimal point rounded to two digits
print("num: {:7.2f}".format(number))
# left alignment and fill with free space 0
print("num: {:0<8.2f}".format(number))
# right alignment and fill with free space 0
print("num: {:0>8.2f}".format(number))
# right alignment and fill with free space *
print("num: {:*>8.2f}".format(number))

a, b = input('Please enter two numbers: ').split()
print(a + b)
print(int(a) + int(b))

animals = ['cat', 'dog', 'lion']
with open('animals.dat', 'w') as file:
 for animal in animals:
    file.write(animal + '\n')

with open('animals.dat') as file:
   print(file.read())


f = open('test.txt', 'w')
f.close()

f = open('test.txt', 'w')
f.write('Opening a file\n')
f.write('Closing a file')
f.close()

f = open('test.txt', 'r')
f.read()

f = open('test.txt', 'r')
read = f.read()
split = read.split()
print(split)

f = open('test.txt', 'r')
for x in f:
   print(x, end='')




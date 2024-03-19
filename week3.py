height = 175
weight = 61
print ('나의 키는 {}cm 이고 몸무게는 {}kg 이다.'.format(height, weight))
print('{} and {}'.format('Python', 'Numpy'))
print('{1} and {0}'.format('cat', 'dog'))

""""
for i in range(10):
   print(i, end=' ')

print('010','1234','5678', sep=" ")
""""

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


str = "Hong Gildong"
print(str)
print("{:/>20s}".format(str))
print("{:/<20s}".format(str))

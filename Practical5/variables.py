a = 19245301
b = 4218520
c = 271
#set value of variables a,b,c
d = b-c #use subtraction to calculate the difference between b and c
print('The difference between the numbers of cases in 2020 and 2021 is',d)
e = a-b #use subtraction to calculate the difference between a and b
print('The difference between the numbers of cases in 2021 and 2022 is',e)

if d>e:
	print('d is greater than e')
else:
	print('e is greater than d')
#e is greater.Use 'if...else' to print different results.
#The rate of new cases was greater in 2021.

X1 = True
Y1 = False
W1 = X1&Y1
print(W1)
W2 = X1|Y1
print(W2)

X2 = True
Y2 = True
W1 = X2&Y2
print(W1)
W2 = X2|Y2
print(W2)

X3 = False
Y3 = False
W1 = X3&Y3
print(W1)
W2 = X3|Y3
print(W2)

X4 = False
Y4 = True
W1 = X4&Y4
print(W1)
W2 = X4|Y4
print(W2)

X='123'
Y='456'
W= X and Y
print(W)

X='123'
Y=''
W= X and Y
print(W)


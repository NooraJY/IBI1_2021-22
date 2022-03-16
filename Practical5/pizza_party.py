n = 0 #The cut starts with 0.
p = 1 #When there is no cut, there is only one piece of pizza.
while p < 64:
	n +=1
	p = (n ** 2 + n + 2)/2
	print('The number of cuts is', n,'and the pizza can be cut into',p,'pieces')
#one cycle means one cut is added
	if p >= 64:
		print('Now we have enough pieces of pizza for everyone in class.')
		break
#The pieces of pizza have exceeded 64 so the programme stops.

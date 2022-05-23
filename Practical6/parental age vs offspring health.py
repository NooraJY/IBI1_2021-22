paternal_age = [30,35,40,45,50,55,60,65,70,75]
chd = [1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
data = dict(zip(paternal_age,chd))
#combine the two lists into the 'data' dictionary
print(data)
#print the dictionary

import matplotlib.pyplot as plt
import numpy as np
#import module matplotlib and numpy
x = np.array(paternal_age)
#set the value of x
y = np.array(chd)
#set the value of y
ax = plt.axes()
ax.set_facecolor("lightskyblue")
#set the color of the background of the plot
plt.scatter(x,y,marker='X',color='mediumorchid')
#paint the plot and set the shape and color of the dots
plt.title('parental age vs offspring health')
#set the title of the plot
plt.xlabel('The paternal ages')
plt.ylabel('the offspring health')
#set the labels of x axis and y axis
plt.show()
#creat and show the scatter plot

age = input('the paternal age is:')
#input the paternal age
if int(age) in data:
	print('When the paternal age is',age,'the risk of congenital heart disease for the offspring is',data[int(age)])
#change the input string into a number and print the result if the age is in the 'data' dictionary
else:
	print("We can't find the risk of congenital heart disease for the offspring")
#print this result if we can't find the age in the 'data' dictionary


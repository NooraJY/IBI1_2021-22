marks=[45,36,86,57,53,92,65,45]
marks.sort()
#sort the list and change the initial order in the list
print(marks)

import numpy as np
import matplotlib.pyplot as plt
#import the module numpy and matplotlib
score = np.array(marks)
#set the value in the boxplot from the 'marks' list
plt.boxplot(score,patch_artist=True)
#paint the boxplot and show the color of the box
plt.title('list manipulation')
#set the title of the boxplot
plt.show()

average_mark=sum(marks)/len(marks)
#calculate the average of numbers in the 'marks' list
if average_mark >= 60:
	print('the average mark is',average_mark,'which is higher than the pass mark of 60%. Rob can pass the ICA.')
else:
	print('the average mark is',average_mark,'which is lower than the pass mark of 60%. Rob has failed the ICA.')
#print differnt results in the pass and fail situations

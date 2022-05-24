from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse("go_obo.xml")
obo = DOMTree.documentElement
#get the root element of the document
terms = obo.getElementsByTagName("term")
#a list of 'terms' elements
print('The number of terms is ',len(terms))


dic1 ={}
for term in terms:
    each_id = term.getElementsByTagName('id')[0].childNodes[0].data
    is_a_list = []
    for i in term.getElementsByTagName('is_a'):
        is_a_list.append(i.childNodes[0].data)
    for is_a in is_a_list:
        if is_a in dic1:
            dic1[is_a].append(each_id)
        else:
            dic1[is_a]=[each_id]
#add the id and is_a in the dictionary
#key = parent node/id, value = child node/is_a

def calculate(list0):
    for i in list0:
        if i in list0:
            if i not in list3:
                list3.append(i)
                if i in dic1:
                    calculate(dic1[i])
    return len(list3)
#define a function that can calculate the number of childnodes

list1=[]#all terms
list2=[]#all translation related terms
for term in terms:
    nodes=0
    list3=[]
    each_id = term.getElementsByTagName('id')[0].childNodes[0].data
    if each_id in dic1:
        nodes = calculate(dic1[each_id])
    list1.append(nodes)
    defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
    if defstr.find('translation')>0:
        list2.append(nodes)

import numpy as np
import matplotlib.pyplot as plt
plt.boxplot(list1)
plt.title('the distribution of childnodes across terms in the Gene Ontology')
plt.ylabel('the number of childNodes')
plt.xlabel('terms')
plt.show()

plt.boxplot(list2)
plt.title('the distribution of the translation related genes')
plt.ylabel('the number of childNodes')
plt.xlabel('the translation related terms')
plt.show()

average1 = np.mean(list1)
average2 = np.mean(list2)
if average1>average2:
    print('The translation related terms have fewer childeNodes than the overall terms on average.')
    
else:
    print('The translation related terms have more childeNodes than the overall terms on average.')


    

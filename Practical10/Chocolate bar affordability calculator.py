def buy_chocolate_bar(money,price):
    quantity = int(money)//int(price)
    change = int(money)-int(price)*quantity
#Define the function to calculate the quantity of the chocolate bars and the change.
    return [quantity,change];
#Return the results as a list.

money1 = input('The total money is:')
price1 = input('The price of one chocolate bar is:')
#input the total money and price
list1 = buy_chocolate_bar(money1,price1)
#Define the results as list1.
print('When the total money=',money1,' and the price of one chocolate bar=',price1,' ,the number of chocolate bars that we can buy is',list1[0],'. The change that is left over is',list1[1])

#example
money2 = 100
price2 = 7
list2 = buy_chocolate_bar(money2,price2)
print('When the total money=',money2,' and the price of one chocolate bar=',price2,' ,the number of chocolate bars that we can buy is:',list2[0],'. The change that is left over is',list2[1])

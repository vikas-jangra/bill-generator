#!/usr/bin/env python
# coding: utf-8

# In[1]:



# # To show the time and date


import datetime
x = datetime.datetime.now()
clock1 = x.strftime("Date : %d-%m-%Y\t\t\t\t\t\t\t\t\t\t\tTime: %H:%M:%S" )  #\t is used for the defalut spaces                
print(clock1)


name = '\033[1m' + 'Fresh And Naturelle Ice-Creams'  # \033[1m it is used for the bold
f1 = name.center(120)
print(f1)



f2 = input('Customer Name\t:\t\t')
f3 = input('Contact No.\t:\t\t')


list1 = []
items = {'Mango':75 ,'Orange':75,'Lychee':90,'Pista':100,'Mixed fruits':80}
flavour = input('Enter the flavour\t:\t\t')
Rate = items.get(flavour)
qty = int(input('Enter the quantity\t:\t\t'))
print(' ')
amt = (Rate*qty)
print(' ')
print('Flavour','\t\t','Rate','\t\t','Quantity','\t\t','Amount')
print(flavour,'\t\t\t ',Rate,'\t\t' ,qty,'\t\t\t',amt)
print('\t\t\t\t\t\t\t\t','---------')
list1.append(amt)
sum1 = 0
i = 0
for i in list1:
    i =+i
    totalsum = i + sum1
    print('Total amount\t\t:\t\t\t\t\t',totalsum)
print(' ')   
print( '\t\t\t\t\t\t\t''\033[1m'+'Visit Again')
    
    
   





# In[ ]:





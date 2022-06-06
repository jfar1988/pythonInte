# funcion lambda o anonima
from ast import Lambda
from functools import reduce

#Lambda Function
# palindromo = lambda String: String == String[::-1]
# print(palindromo('dabalearrozalazorraelabad'))

#Funcion normal
# def palindromo(string): 
#     return string==string[::-1]
# print(palindromo('ana'))

#High order fuctions:

#utilizando list comprehesions
# my_list=[1,4,5,6,9,13,19,21]
# myListImparOdd= [i for i in my_list if i %2 != 0]
# print(myListImparOdd)

# # uso de filter
# my_list=[1,4,5,6,9,13,19,21]
# odd = list(filter(lambda x: x % 2 !=0, my_list))
# print(odd)

#utilizando list comprehesions
# my_list=[1,2,3,4,5]
# square=[i**2 for i in my_list]
# print(square)

# #uso de map
# my_list=[1,2,3,4,5]
# square=list(map(lambda x: x**2, my_list))
# print(square)

#uso de reduce
# list_pairs = [2,2,2,2,2]
# add_p=reduce(lambda x,y: x*y, list_pairs)
# print(add_p)


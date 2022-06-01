# funcion lambda o anonima
from functools import reduce


# palindrome = lambda string: string == string[::-1]
# print(palindrome("jose"))
# # uso de filter
# my_list=[1,4,5,6,9,13,19,21]
# add = list(filter(lambda x: x%2 != 0, my_list))
# print(add)
# #uso de map
# my_list2=[1,2,3,4,5]
# add = list(map(lambda x: x**2, my_list2))
# print(add)
#uso de reduce
list_pairs = [2,2,2,2,2]
add_p=reduce(lambda x,y: x*y, list_pairs)
print(add_p)
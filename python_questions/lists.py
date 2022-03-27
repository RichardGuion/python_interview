'''
  Various things that can be done in python with list comprehension, sets, dictionaries
'''
def mult_list(list1):
    list2 =[x * 2 for x in list1]
    print(list2)

mult_list(range(11))

def list_squared_by_map(list1):
    list2 = list(map(lambda x: x**2, list1))
    print(f'squared using map = {list2}')

list_squared_by_map(range(10))

def list_items_not_divis_by_three(list1):
    list2 = [x for x in list1 if x % 3 == 0]
    print(list2)

list_items_not_divis_by_three(range(20))

def tuples_squared(list1):
    list2 = [(x, x ** 2) for x in list1]
    print(list2)

tuples_squared(range(10))

def dict_squared(list1):
    list2 = { x: x ** 2 for x in list1}
    print(list2)

dict_squared(range(10))

def pi_list_rounded():
    seq = range(10)
    from math import pi
    seq2 = [round(pi, i) for i in seq]
    print(seq2)

pi_list_rounded()


# this returns unique items but in random order
def unique_list_items(list1):
    return list(set(list1))

# this returns unique items in the original order
def unique_list_items_ordered(list1):
    from collections import OrderedDict
    if type(list1) is str:
        list1 = list1.split()
    return list(OrderedDict.fromkeys(list1))


result1 = unique_list_items(['foo', 'zoo', 'car', 'foo', 'zar', 'zoo'])
print(f'unique items from set on list: {result1 }')

result2 = unique_list_items_ordered(['foo', 'zoo', 'car', 'foo', 'zar', 'zoo'])
print(f'unique items from ordered dict on list: {result2}')

result3 = unique_list_items_ordered('I can can see clearly now my brain brain is gone')
print(f'unique items from ordered dict on string: {result3}')



def reverse_string(s):
    return s[::-1] 

print(reverse_string("Hello IT"))
#The fromkeys() method creates a dictionary from the given sequence of keys and values.

lst = [1, 1, 2, 5, 5, 3, 6, 2, 1, 1, 3, 7, 5, 5, 3]
lst1 = ['a','b']
def remove_duplicate(lst):
    return list(dict.fromkeys(lst))

print(remove_duplicate(lst))
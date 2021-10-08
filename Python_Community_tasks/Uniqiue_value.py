"""

Написать функцию, которая будет принимать список и находить уникальное число.

Пример:

find_unique_value([1, 2, 1, 1]) -> 2
find_unique_value([2, 3, 3, 3]) -> 2
find_unique_value([5, 5, 5, 0.5]) -> 0.5

"""

def find_unique_value(lst):
    res = [i for i in lst if lst.count(i) == 1]    
    return res

print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3]))
print(find_unique_value([5, 5, 5, 0.5]))
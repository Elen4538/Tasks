"""Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.
https://www.codewars.com/kata/523f5d21c841566fde000009/python

"""


def array_diff(list1,list2):
    if len(list2) < 1:
        return list1
    else:
        list3 = set(list2)    
        for num in list1[:]: #list1
            for i in list3:
                if i == num:
                    
                    list1.remove(num)
        return list1


print(array_diff([1,2,2,2,3],[2]))
print(array_diff([1,2,3],[1, 2]))
print(array_diff([5, 2, 3, 4, 19, -19, -20, 13, -5, -14, -4], [13, 13, 15]))
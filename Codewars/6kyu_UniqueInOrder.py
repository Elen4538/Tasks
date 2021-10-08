# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 14:02:00 2021

@author: somebody
"""

def unique_in_order(iterable):
    res = []
    
    if len(iterable) == 0:
        return res
    else:        
        res.append(iterable[0])
        for item in iterable:
            n = len(res)-1
            if item != res[n]:
                res.append(item)
        return res
    

#string1 = 'AAAABBBCCDAABBB'
#string2 = [str(i) for i in string1]


print(unique_in_order(['A', 'A', 'A', 'B', 'C', 'D', 'A', 'B',
                       'A', 'D', 'A', 'D', 'A', 'D', 'A', 'B',
                       'C', 'c', 'A', 'D', '1', '2', '3', 'a', 'b']))




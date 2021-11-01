#https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python

import itertools


def choose_best_sum(t, k, ls):

    sequences = list(itertools.combinations(ls, k))
    
    res = list((sum(x)) for x in sequences if sum(x) <= t)
    
    if len(res) == 0:
        return None
    else:
        return max(res)
    


ls = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89] 
t = 430 
k = 8 

print(choose_best_sum(t,k, ls))
#None
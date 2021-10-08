# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 21:10:23 2021

@author: somebody
"""

"""Write a function, persistence, that takes in a positive parameter num 
and returns its multiplicative persistence, which is the number of times 
you must multiply the digits in num until you reach a single digit."""

def persistence(n):
  from functools import reduce     
  count = 0
  while n > 9:      
    n = reduce(lambda x, y : x * y, [int(i) for i in str(n)])       
    count +=1
  return count 
    
    
print(persistence(999))



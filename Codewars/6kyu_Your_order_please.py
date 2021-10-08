# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 09:20:27 2021

@author: somebody
"""
"""Your task is to sort a given string. Each word in the string will contain 
a single number. This number is the position the word should have in the 
result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the
input String will only contain valid consecutive numbers."""

def order(sentence):
    
    if len(sentence)==0:
        return ""
    else:
    
        list1 = sentence.split(" ")
        new_list = [0]*len(list1)
    
        for i in list1:
            
            for symbl in i:
                if symbl.isdigit():
                    new_list[int(symbl)-1] = i
        ord_string = ' '.join(new_list)
    
    
        return ord_string
            
    
print(order("4be fro1m gi2ve and3"))
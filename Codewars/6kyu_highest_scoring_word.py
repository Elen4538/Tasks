"""
https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""

def high(x):
    list1 = x.split(' ')
    res =[]
    num = 0
    for word in list1:
        for letter in word:
            num+=ord(letter)-96
            print(num)
        res.append(num)
        num = 0
    
    max_word = res.index(max(res))

    return list1[max_word]

print(high('what time are we climbing up the volcano')) #'taxi'
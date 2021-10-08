"""
https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/python
For a given string s find the character c (or C) with longest consecutive repetition and return:
(c, l)
where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

For empty string return:
('', 0)
"""

def longest_repetition(chars):
    
    if len(chars) == 0:
        return ('', 0)
    else:
        length = 1
        res = ""

        for i in range(len(chars)):
            if i == 0: #если переменная результата пустая
                res = chars[i] 
                
                print(res)
            elif res[-1] == chars[i]:
                res +=chars[i]
                print(res)
            else:
                res = res + " " + chars[i] # разделяем последовательность если след символ не совпадает
                print(res)
        res = sorted(res.split(" "), reverse = True, key = len)
        return (*set(res[0]),len(res[0]))


print(longest_repetition("bbbaaabaaaa"))

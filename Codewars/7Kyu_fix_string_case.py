#https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python

# solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
# solve("coDE") = "code". Upper == lowercase. Change all to lowercase.

def solve(word):
    big = 0
    small = 0

    for i in word:
        if i.isupper():
            big+=1
        else:
            small+=1
    
    if big == small or small > big:
        return word.lower()
    else:
        return word.upper()



print(solve('coDe'))
# https://leetcode.com/problems/integer-to-roman/

def func(num):

    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    res = ''
    i = 0
    while num > 0:
        while num >= val[i]:
            num-=val[i]
            res+=syb[i]
        i+=1
    return res


print(func(3))
print(func(4000))
print(func(85))

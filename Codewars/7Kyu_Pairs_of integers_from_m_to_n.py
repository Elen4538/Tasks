"""https://www.codewars.com/kata/588e2a1ad1140d31cb00008c/train/python

Implement a function that receives two integers m and n and generates a sorted list of pairs (a, b) such that m <= a <= b <= n.

m = 2
n = 4

result = [(2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
"""
def generate_pairs(m, n):
    res = []

    for i in range(m, n+1):
        for y in range(i, n+1):
            res.append((i,y))    
    return res
    


print(generate_pairs(2,4))


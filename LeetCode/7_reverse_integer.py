#https://leetcode.com/problems/reverse-integer/



def reverse(x):
   
    left = -2**31
    right = 2**31 - 1

    if x >right or x < left or x ==0:
        return 0

    elif x >= 0:
        res = "".join(reversed(str(x).rstrip("0")))
        if int(res) <= right:
            return res
        return 0
    else:
        res = "-"+"".join(reversed(str(x)[1:].rstrip("0")))
        if int(res) >= left:
            return res
        return 0

print(reverse(100))

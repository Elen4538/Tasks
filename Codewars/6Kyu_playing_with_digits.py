"""
Playing with digits
https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
"""


def dig_pow(n, p):
    
    if n in range(1,10):
        return -1
    else:
        
        res=0
        for i in str(n):
            res +=int(i)**(p)
            p+=1    
        k = res/n
        
        if res % n==0:
            return int(k)
        else:
            return -1
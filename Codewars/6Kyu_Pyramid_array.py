"""https://www.codewars.com/kata/515f51d438015969f7000013/train/python

pyramid(0) => [ ]
pyramid(1) => [ [1] ]
pyramid(2) => [ [1], [1, 1] ]
pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]

"""



def pyramid(n):
    
    if n == 0:
        return [ ]
    else:    
        res = [ i * [1] for i in range(1,n+1)]
        return res
    


print(pyramid(3))








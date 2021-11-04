#https://www.codewars.com/kata/534e01fbbb17187c7e0000c6


def spiralize(size):
    res = [[0]*size for i in range(size)]
    counter = 0

    if size%2!=0:
        counter+=1

    for j in range(0,(size//2)+counter,2): 
        # upper rib
        for i in range(j-1,size-j):
            res[j][i] = 1 
            
        
        #right rib
        for i in range(1+j,size-j-1):
            res[i][size-j-1] = 1
        
        #lower rib
        for i in range(size-j-1, j,-1):
            res[size -j-1][i] = 1
                
        # left rib
        for i in range(size-j-1, j+1,-1): 
            res[i][j]= 1

    return res

print(spiralize(8))
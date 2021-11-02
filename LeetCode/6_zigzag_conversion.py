# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res =""
        n = len(s)
        counter = 0       
        matr = [([""]*n) for i in range(numRows)]
    
        if n == 1 or numRows == 1:
            
            return s
        
        else:
            s = list(s)
            while len(s) > 0:

                for i in range(numRows):

                    if len(s)> 0:
                        matr[i][counter] = s.pop(0)

                for j in range(numRows-2,0,-1):
                    if len(s)> 0:
                        matr[j][numRows-j-1+counter] = s.pop(0)

                counter+=(numRows -1)

            for i in matr:

                res+="".join(i)

            return res

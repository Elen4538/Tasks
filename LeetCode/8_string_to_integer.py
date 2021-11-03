#https://leetcode.com/problems/string-to-integer-atoi/submissions/
import string
def myAtoi(s: str) :
        left = -2**31
        right = (2**31)-1

        allowed = string.digits 
        res = ''
        counter = 0
        s = s.lstrip()

        if len(s) == 0:
            return 0
        else:
            
            if s[0] =='-':
               
                counter+=1
                res+=s[0]
            elif s[0] =='+':
              
                counter+=1
            for i in range(counter,len(s)):
                if s[i] in allowed:
                    res+=s[i]
                else:
                    break
            try:
                res_num = int(res)

                if left<= res_num <= right:
                    return res_num
                elif res_num > right:
                    return right
                elif res_num < left:
                    return left
            except:
                return 0
            return res


print(myAtoi("42"))
print(myAtoi("4193 with words"))
print(myAtoi("   -42"))
print(myAtoi("words and 987"))
print(myAtoi("-91283472332"))
print(myAtoi("+-12")) 
print(myAtoi('+'))
print(myAtoi('-'))
print(myAtoi("    -88827   5655  U"))
print(myAtoi("-5-"))
print(myAtoi(""))




    


       


# https://leetcode.com/problems/palindrome-number/


def num_palindrome(num):
    str_num = str(num)
    
    if str_num[0]=="-":
        return False
    elif len(str_num)==1:
        return True

    elif str_num == "".join(reversed(str_num)):
            return True
    else:
        return False

print(num_palindrome(100))
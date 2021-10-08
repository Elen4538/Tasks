import re
def increment_string(strng):
    
    res = re.search('[-+]?\d+$',strng) #str
    
    if res:    
        num_to_incr = res.group() 
        ln_num = len(str(num_to_incr)) # lenght of num
        increased_num = str(int(num_to_incr) + 1)

        if len(increased_num) < ln_num: #001
            nulls = ln_num - len(increased_num)
            return strng[:len(strng)-ln_num] + '0'*nulls + increased_num
        else:
            return strng[:len(strng)-ln_num] + increased_num
                
    else: # word without end num
        return strng + '1'


print(increment_string("12fo67ob7a8r"))
print(increment_string("foobar001"))
print(increment_string("foobar99"))
print(increment_string("foo"))


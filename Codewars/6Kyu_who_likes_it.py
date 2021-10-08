"""
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

"""
def likes(names):

    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        res = names[0] +' likes this'
        return res
    
    elif len(names) == 2:
        res = names[0] + ' and ' + names[1] + ' like this'
        return res 
    
    elif len(names) == 3:
        res = names[0] + ', '+ names[1] +' and '+ names[2] + ' like this'
        return res 
       
    else:
        
        res = names[0] +', ' + names[1] + \
        ' and ' + str(len(names) - 2)  + ' others like this' 
        return res 
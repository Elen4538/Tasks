"""
https://www.codewars.com/kata/52190daefe9c702a460003dd
"""
import re 

def search_substr(full_text, search_text, allow_overlap=True):
    
    if len(full_text) == 0 or len(search_text) == 0:
        return 0
    
    
    elif allow_overlap==True:
        pattern = re.compile('(?=%s)' % search_text)
        result = pattern.findall(full_text)
        return len(result)
    
    else:
        return full_text.count(search_text)
   

print(search_substr('aaacccbbbcccc', 'cc'))


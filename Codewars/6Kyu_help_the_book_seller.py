"""https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python


A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. 
Each book has a code c of 3, 4, 5 or more characters. The 1st character of a code 
is a capital letter which defines the book category.

In the bookseller's stocklist each code c is followed by a space and by a positive
 integer n (int n >= 0) which indicates the quantity of books of this code in stock.
"""

def stock_list(list1, list2):
    res = ""
    final_res = {}
    
    for i in list1:
        book = i.split()
        res = res + " "+ book[0][0] + ":"+ book[1]
    
    res1 = res.split()
   
    for letter in list2:
        for word in res1:
            if letter == word[0]:                
                final_res.setdefault(letter, [0]).append(int(word[2:]))
            else:
                final_res.setdefault(letter, [0])                
    res = ""
    
    for k, v in final_res.items():
        res = res + "(" + k + ' : ' + str(sum(v)) +') - ' 
    
    return res[:len(res)-3]

# "(A : 200) - (B : 1140)"

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]

print(stock_list(b,c))



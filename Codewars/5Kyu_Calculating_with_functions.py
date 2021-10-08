"""
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations:
 plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner 
function represents the right operand
Division should be integer division. 

"""
def zero(arg=None): #your code here
    if not arg:
        return 0
    else:
        return arg(0)

def one(arg=None): #your code here
    if not arg:
        return 1
    else:
        return arg(1)

        
def two(arg=None): #your code here
    if not arg:
        return 2
    else:
        return arg(2)

def three(arg=None): #your code here
    if not arg:
        return 3
    else:
        return arg(3)

def four(arg=None): #your code here
    if not arg:
        return 4
    else:
        return arg(4)

def five(arg=None): #your code here
    if not arg:
        return 5
    else:
        return arg(5)
        
def six(arg=None): #your code here
    if not arg:
        return 6
    else:
        return arg(6)
        
def seven(arg=None): #your code here
    if not arg:
        return 7
    else:
        return arg(7)
        
def eight(arg=None): #your code here
    if not arg:
        return 8
    else:
        return arg(8)
        
def nine(arg=None): #your code here
    if not arg:
        return 9
    else:
        return arg(9)

def plus(x): #your code here
    return lambda y: x + y

def minus(x): #your code here
    return lambda y: y - x

def times(x): #your code here
    return lambda y: x * y

def divided_by(x): #your code here
    return lambda y: y // x


print(eight(minus(three()))) # 5
print(six(divided_by(two()))) # 3
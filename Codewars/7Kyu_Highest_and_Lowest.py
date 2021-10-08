"""
https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

In this little assignment you are given a string of space separated numbers, 
and have to return the highest and lowest number."""


def high_and_low(numbers):
       
    list1 = list(map(int,numbers.split()))

    if len(list1) ==1:
        return numbers + ' ' + numbers
    else:
        max_num = str(max(list1))
        min_num = str(min(list1))
    
        return max_num + ' ' + min_num



print(high_and_low("1 9 3 4 -5"))





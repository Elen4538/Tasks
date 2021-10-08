# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 22:48:58 2021

@author: somebody
"""

'''Напишите программу, которая выводит на экран числа от 1 до 100.
 При этом вместо чисел, кратных трем, программа должна выводить 
 слово Fizz, а вместо чисел, кратных пяти — слово Buzz. 
 Если число кратно пятнадцати, то программа должна выводить
 слово FizzBuzz. Задача может показаться очевидной, но нужно 
 получить наиболее простое и красивое решение'''
 
for i in range(1,101):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 15 == 0:
        print('FizzBuzz')
    else:
        print(i)
        
print(
      *[(i, "Fizz", "Buzz", "Fizz Buzz")[(i % 3 == 0) + (i % 5 == 0) * 2] for i in range(1, 101)], sep=", "
          )



def FizzBuzz():
    for n in range(1,101):
        print("Fizz"*(not n % 3) + "Buzz"*(not n % 5) or n)

FizzBuzz()


def fizzbuzz(n):
    for x in range(1,n+1):
        if not x % 15:
            yield 'fizz buzz'
        elif not x % 3:
            yield 'fizz'
        elif not x % 5:
            yield 'buzz'
        else:
            yield x

if __name__ == "__main__":
    print ','.join(fizzbuzz(20))
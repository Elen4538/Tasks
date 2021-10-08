"""
Условие:

Написать функцию, которая будет возвращать все числа, на которые делится аргумент функции. 
Если же аргумент — простое число, то возвращаем строку, как на примере.

Пример:

find_divisors(13) -> 13 - простое число
find_divisors(10) -> [2, 5]
find_divisors(12) -> [2, 3, 4, 6]

"""
def find_divisors(num):
    if num % 2 !=0:
        return num
    else:
        res = [ i for i in range(2,num) if num % i == 0]
        return res

print(find_divisors(12))


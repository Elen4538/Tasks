"""
Условие:

Написать простую функцию, которая будет возвращать век, на основе года.

Пример:

get_century(2021) -> 21
get_century(1999) -> 20
get_century(2000) -> 20
get_century(101) -> 2

"""
def get_century(year):
    century = year/100
    if century % 100 == 0:
        return year//100
    else:
        return year//100 + 1

print(get_century(2021))
print(get_century(1999))
print(get_century(101))

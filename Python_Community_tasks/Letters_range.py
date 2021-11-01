# Условие:
# Написать функцию, которая будет принимать диапазон букв, разделённых дефисом и возвращать все символы между ними включительно.
# Никаких проверок на ошибку делать не надо, минимальное значение всегда меньше или равно максимальному.
# Пример:

# letters_range("a-c") -> abc
# letters_range("a-a") -> a
# letters_range("s-H") -> stuvwxyzABCDEFGH
# letters_range("a-A") -> abcdefghijklmnopqrstuvwxyzA
import string

def letters_range(strng):
    alphabet = string.ascii_letters
    start_ind = strng[0]
    end_ind = strng[-1]

    return alphabet[alphabet.index(start_ind):alphabet.index(end_ind)+1]

print(letters_range("a-c"))


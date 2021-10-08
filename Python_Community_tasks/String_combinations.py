"""
Условие:

Написать функцию, которая будет возвращать все возможные расположения символов внутри строки 

Пример:

permutations("a") -> ['a']
permutations("ab") -> ['ba', 'ab']
permutations("abc") -> ['abc', 'cba', 'bca', 'bac', 'cab', 'acb']
"""
def permutations(strng):
    def permutate(strng, all_str=''):

        res = []
        for i, char in enumerate(strng):
            str_part = strng[:i] + strng[i+1:]#delete symb
            full_strng = all_str + char

            if len(str_part) == 0:
                res.append(full_strng)
            else:
                 res.extend(permutate(str_part, full_strng))

        return res
    res1 = permutate(strng)
    return list(set(res1))

print(permutations("abc"))

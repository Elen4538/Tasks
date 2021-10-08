"""Условие:

Напишите, пожалуйста, функцию, которая превращает одномерный список в список из пар. 

Если количество элементов в списке не позволяет поделить его на 2, то метод использует необязательный метод fill_char с значением для заполнения.

Желательно не использовать сторонние модули.

Пример:

to_pairs([1, 2, 3, 4]) -> [[1, 2], [3, 4]]
to_pairs([1, 2, 3, 4, 5]) -> [[1, 2], [3, 4], [5, None]]
to_pairs([1, 2, 3, 4, 5, 0], fill_char = 0) -> [[1, 2], [3, 4], [5, 0]]"""


def to_pairs(list1):
    res = []
    if len(list1) %2 == 1: # нечетный
        for i in range(0,len(list1)-2,2):
            
            res.append([list1[i], list1[i+1]])
        res.append( [ list1[-1], (None)])
        
        return res        
    
    else:
        for i in range(0,len(list1)-1,2):

            res.append([list1[i], list1[i+1]])
        
        return res

print(to_pairs([1, 2, 3, 4]))

#lambda x, y: res.append([x,y]) in list1


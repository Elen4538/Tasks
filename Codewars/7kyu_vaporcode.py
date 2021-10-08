"""
https://www.codewars.com/kata/5966eeb31b229e44eb00007a
Write a function that converts any sentence into a V A P O R W A V E sentence. 
a V A P O R W A V E sentence converts all the letters into uppercase, and adds
 2 spaces between each letter (or special character) to create this V A P O R W A V E effect."""


def vaporcode(s):

    res =""
    
    for i in s:
        if i != " ": #убираем одиночные пробелы
            res+=i.upper()+"  "# добавляем 3 равнозначных пробела между буквами
            print(res)
    
    return res.strip(" ") # удалямем один ненужный робел между буквами



print(vaporcode("Why isn't my code working?"))
#"Lets go to the movies"       -->  "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"
#"Why isn't my code working?"  -->  "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"


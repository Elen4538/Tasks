# Условие:

# Ваша задача — написать функцию, которая проверяет, может ли такая переменная существовать. 
# Переменная не может начинаться с цифры, состоит только из символов A-z, цифр и "_". Также, 
# она не может быть ни одним из зарегистрированных слов. Их можно взять их keyword.kwlist.

# Примеры:

# check_var_name('I$Contain0*7') -> False
# check_var_name('1wrong') -> False
# check_var_name('_oKe') -> True
# check_var_name('True') -> False
import string 
import keyword

def check_var_name(strng):
    
    forbid_list = keyword.kwlist

    letters = string.ascii_letters
    digit_symb = string.digits
    spec_symb = '_'

    if strng in forbid_list or strng[0] in digit_symb:
        return False
    
    for i in strng:
        if not i in (letters+digit_symb+spec_symb):
            return False

    return True
        
print(check_var_name('True'))
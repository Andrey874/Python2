import random
import string as st
from random import choices  # choices(iterable, k=0) - возвращает список из k элементов последовательности с повтором
from random import sample   # sample(iterable, k=0) - возвращает список из k элементов последовательности без повторов

digits = st.digits
lower = st.ascii_lowercase
upper = st.ascii_uppercase
punc = st.punctuation

"""
Написать класс декоратор, который принимает в качестве аргументов ИМЕНА наборов
из модуля string(punctuation, ascii_lowercase, ascii_uppercase, digits) и возвращает
случайную строку такой же длины из символов указанных наборов.
Аргумент string_len функции password > 4
Пример:
До декорирования: 
print(password(5))   # Out: 84743

После декорирования:
@strong('lower', 'punc')
print(password(5))   # Out: au%d#

@strong()
print(password(5))  # Out: 63215

@strong('lower', 'upper')
print(password(5))  # Out: wASTr

@strong('punc')
print(password(5))  # Out: !,.;?
"""

class strong:
    def __init__(self, *args):
            self.arg = args

    def __call__(self, function):
        def decor(*args):
            symb_len = len(function(*args))
            method = []
            method += self.arg
            method_len = len(self.arg)
            if 'upper' in method and method_len == 1:
                return "".join(random.choices(upper, k=symb_len))
            elif 'lower' in method and method_len == 1:
                return "".join(random.choices(lower, k=symb_len))
            elif 'punc' in method and method_len == 1:
                return "".join(random.choices(punc, k=symb_len))
            elif 'digits' in method and method_len == 1:
                return "".join(random.choices(digits, k=symb_len))
            elif 'upper' in method and 'lower' in method and method_len == 2:
                up = "".join(random.choices(upper, k=symb_len))
                lo = "".join(random.choices(lower, k=symb_len))
                list = []
                list += up
                list += lo
                return "".join(random.choices(list, k=symb_len))
            elif 'upper' in method and 'digits' in method and method_len == 2:
                up = "".join(random.choices(upper, k=symb_len))
                dg = "".join(random.choices(digits, k=symb_len))
                list = []
                list += up
                list += dg
                return "".join(random.choices(list, k=symb_len))
            elif 'upper' in method and 'punc' in method and method_len == 2:
                up = "".join(random.choices(upper, k=symb_len))
                pu = "".join(random.choices(punc, k=symb_len))
                list = []
                list += up
                list += pu
                return "".join(random.choices(list, k=symb_len))
            elif 'lower' in method and 'punc' in method and method_len == 2:
                lo = "".join(random.choices(lower, k=symb_len))
                pu = "".join(random.choices(punc, k=symb_len))
                list = []
                list += lo
                list += pu
                return "".join(random.choices(list, k=symb_len))
            elif 'lower' in method and 'digits' in method and method_len == 2:
                lo = "".join(random.choices(lower, k=symb_len))
                dg = "".join(random.choices(digits, k=symb_len))
                list = []
                list += lo
                list += dg
                return "".join(random.choices(list, k=symb_len))
            elif 'punc' in method and 'digits' in method and method_len == 2:
                pu = "".join(random.choices(punc, k=symb_len))
                dg = "".join(random.choices(digits, k=symb_len))
                list = []
                list += pu
                list += dg
                return "".join(random.choices(list, k=symb_len))
            elif 'upper' in method and 'lower' in method and 'punc' in method and method_len == 3:
                pu = "".join(random.choices(punc, k=symb_len))
                lo = "".join(random.choices(lower, k=symb_len))
                up = "".join(random.choices(upper, k=symb_len))
                list = []
                list += pu
                list += lo
                list += up
                return "".join(random.choices(list, k=symb_len))
            elif 'upper' in method and 'lower' in method and 'digits' in method and method_len == 3:
                lo = "".join(random.choices(lower, k=symb_len))
                dg = "".join(random.choices(digits, k=symb_len))
                up = "".join(random.choices(upper, k=symb_len))
                list = []
                list += lo
                list += dg
                list += up
                return "".join(random.choices(list, k=symb_len))
            elif 'upper' in method and 'punc' in method and 'digits' in method and method_len == 3:
                pu = "".join(random.choices(punc, k=symb_len))
                dg = "".join(random.choices(digits, k=symb_len))
                up = "".join(random.choices(upper, k=symb_len))
                list = []
                list += pu
                list += dg
                list += up
                return "".join(random.choices(list, k=symb_len))
            elif 'lower' in method and 'punc' in method and 'digits' in method and method_len == 3:
                pu = "".join(random.choices(punc, k=symb_len))
                dg = "".join(random.choices(digits, k=symb_len))
                lo = "".join(random.choices(lower, k=symb_len))
                list = []
                list += pu
                list += dg
                list += lo
            elif 'lower' in method and 'punc' in method and 'digits' in method and 'upper' in method and method_len == 4:
                pu = "".join(random.choices(punc, k=symb_len))
                dg = "".join(random.choices(digits, k=symb_len))
                lo = "".join(random.choices(lower, k=symb_len))
                up = "".join(random.choices(upper, k=symb_len))
                list = []
                list += pu
                list += dg
                list += lo
                list += up
                return "".join(random.choices(list, k=symb_len))
            return "".join(random.choices(digits, k=symb_len))
        return decor


# @strong('lower', 'punc')
@strong('lower', 'upper', 'digits', 'punc')
def password(string_len: int) -> str:
    """ Функция генерирует строку случайных символов
        указанной длины из набора st.digits"""
    return "".join(random.choices(digits, k=string_len))

# До декорирования
print(password(9))  # Out: 84743
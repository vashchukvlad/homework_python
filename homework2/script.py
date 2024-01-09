# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

# 2) протипізувати перше завдання
from typing import Callable


def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list

    return add_todo, get_all

# add_todo, get_all = notebook()
# add_todo('todo1')
# add_todo('todo2')
# print(get_all())



# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)

# Приклад:

# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(num: int) -> str:
    num_str: str = str(num)
    num_arr: list = []

    for index, one_number in enumerate(num_str):
        if one_number != '0':
            number_of_zerous: int = len(num_str) - (index + 1)
            num_arr.append(one_number + '0' * (number_of_zerous))

    result: str = ' + '.join(num_arr)
    return result

# print(expanded_form(12))
# print(expanded_form(42))
# print(expanded_form(70304))



# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція 
# продекорована цим декоратором, та буде виводити це значення після виконання функцій

def decor(func):
    counter = 0

    def inner(*args, **kwargs):
        nonlocal counter
        counter += 1
        print('couner = ', counter)
        func(*args, **kwargs)
        print('-------------------------------------')
    return inner

@decor
def func1():
    print('func1')

@decor
def func2():
    print('func2')

# func1()
# func1()
# func2()
# func1()
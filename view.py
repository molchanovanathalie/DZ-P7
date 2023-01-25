def inp_mod():
    mod = input('Введите режим работы (импорт или экспорт): ')
    return mod


def inp_import():
    name = input('Введите фамилию для поиска: ')
    return name

def view_import (result):
    print(*result, sep='\n')

def inp_export():
    name = input('Введите фамилию: ')
    surname = input('Введите имя: ')
    sec_name = input('Введите отчество: ')
    phone = input('Введите телефона: ')
    comment = input('Ведите признак телефона (домашний, рабочий): ')
    return '\n', name, surname, sec_name, phone, comment


def view_import_no ():
    print(f'Данные не найдены')

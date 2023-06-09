from exceptions import UnexpectedLengthOfList
from datetime import datetime
import re


def convert_str_to_true_list(data: str, true_length: int) -> list:
    result = data.split()
    lst_length = len(result)
    if lst_length != true_length:
        raise UnexpectedLengthOfList(true_length, lst_length)

    return result


def check_list(lst: list, name: str):
    if len(lst) == 1:
        return lst[0]
    else:
        message = f'{name}: ' + 'нет данных' if len(lst) < 1 else 'данных больше чем нужно'
        raise ValueError(message)


def get_gender(lst):
    lst_temp = []
    for i in lst:
        if len(i) == 1 and (str(i).lower() == 'm' or i == 'f'):
            lst_temp.append(i)
    return check_list(lst_temp, 'Пол')


def get_phone_number(lst: list):
    numeric_values = [x for x in lst if x.isdigit()]
    return check_list(numeric_values, 'Номер телефона')


def get_date_of_birth(lst: list):
    result = []
    for item in lst:
        try:
            date = datetime.strptime(item, '%d.%m.%Y')
            if date <= datetime.now():
                result.append(item)
            else:
                raise ValueError('Дата рождения не может быть из будущего!')
        except ValueError:
            pass
    return check_list(result, 'Дата рождения')


def get_fio(lst: list):
    pattern = r'^[A-ZА-ЯЁ][a-zA-Zа-яёА-ЯЁ]*$'
    result = [item for item in lst if re.match(pattern, item)]
    if len(result) == 3:
        return result
    else:
        message = 'ФИО: ' + 'нет данных' if len(result) < 3 else 'данных больше чем нужно'
        raise ValueError(message)


def get_valid_data(data: str) -> dict:
    lst = convert_str_to_true_list(data, 6)
    lst = [x.replace(',', '') for x in lst]
    gender = get_gender(lst)
    phone = get_phone_number(lst)
    b_date = get_date_of_birth(lst)
    fio = get_fio(lst)
    return {'f_name': fio[0], 'patronymic': fio[1], 'l_name': fio[2], 'b_date': b_date, 'phone': phone,
            'gender': gender}

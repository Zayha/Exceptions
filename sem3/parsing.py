from exceptions import UnexpectedLengthOfList
from datetime import datetime


def convert_str_to_true_list(data: str, true_length: int) -> list:
    result = data.split()
    lst_length = len(result)
    if lst_length != true_length:
        raise UnexpectedLengthOfList(true_length, lst_length)

    return result


def get_gender(lst):
    lst_temp = []
    for i in lst:
        if len(i) == 1 and (i == 'm' or i == 'f'):
            lst_temp.append(i)
    if len(lst_temp) == 1:
        return lst_temp[0]
    else:
        message = 'Пол: ' + 'нет данных' if len(lst_temp) < 1 else 'данных больше чем нужно'
        raise ValueError(message)


def get_phone_number(lst: list):
    numeric_values = [x for x in lst if x.isdigit()]
    if len(numeric_values) == 1:
        return numeric_values[0]
    else:
        message = 'Номер телефона: ' + 'нет данных' if len(numeric_values) < 1 else 'данных больше чем нужно'
        raise ValueError(message)


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
            print(f'{item} - Некорректный формат даты')
    if len(result) == 1:
        return result[0]
    else:
        message = 'Дата рождения: ' + 'нет данных' if len(result) < 1 else 'данных больше чем нужно'
        raise ValueError(message)


def get_valid_data(data: str) -> dict:
    lst = convert_str_to_true_list(data, 6)
    gender = get_gender(lst)
    phone = get_phone_number(lst)
    return {'gender': gender, 'phone': phone}

# Анна=4
# Елена=5
# Марина=6
# Владимир=?
# Константин=?
# Иван=4
# Реализуйте метод, который считывает данные из файла и сохраняет в двумерный массив
# (либо HashMap, если студенты с ним знакомы). В отдельном методе нужно будет пройти по структуре данных,
# если сохранено значение ?, заменить его на соответствующее число.Если на каком-то месте встречается символ,
# отличный от числа или ?, бросить подходящее исключение.Записать в тот же файл данные с замененными символами ?./

def read_to_lst(file_name: str, divider: str) -> list:
    lst = []

    if not isinstance(file_name, str):
        raise TypeError("Некорректный тип данных для file_name. Ожидалась строка.")
    if not isinstance(divider, str):
        raise TypeError("Некорректный тип данных для divider. Ожидалась строка.")

    try:
        with open(file_name, "r", encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                line = line.strip()
                try:
                    a, b = line.split(divider)
                    lst.append([a, b])
                except ValueError:
                    # Обработка ошибки, если не удается разделить строку по разделителю
                    print(f"Ошибка при разделении строки: {line}")
    except FileNotFoundError:
        # Обработка ошибки, если файл не найден
        print(f"Файл не найден: {file_name}")
        return lst  # Возвращаем пустой список, если файл не найден
    return lst


def can_convert_to_int(data: str) -> bool:
    return True if set(data).issubset(set('1234567890')) else False


def remake_list(lst: list) -> list:
    for i in lst:
        if not can_convert_to_int(i[1]):
            if i[1] == '?':
                i[1] = str(len(i[0]))
            else:
                raise ValueError(f"неожиданное значение: {i[1]}")
    return lst


def write_list_to_file(lst, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        lines = ['='.join(item) for item in lst]
        file.write('\n'.join(lines))


def main():
    rtl = read_to_lst('file.txt', '=')
    result = remake_list(rtl)
    write_list_to_file(result, 'output.txt')


if __name__ == '__main__':
    main()

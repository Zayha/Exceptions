# Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float), и возвращает введенное
# значение. Ввод текста вместо числа не должно приводить к падению приложения, вместо этого, необходимо повторно
# запросить у пользователя ввод данных.


def get_float():
    while True:
        value = input("Введите число типа float: ")
        try:
            value = value.replace(',', '.')
            num_float = float(value)
            break
        except ValueError:
            print(f"Значение {value} не может быть приведено к типу float!")

    print(f'{num_float} соответствует типу float')
    return num_float


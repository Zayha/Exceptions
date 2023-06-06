# Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку. Пользователю должно
# показаться сообщение, что пустые строки вводить нельзя.
def if_empty_string(data: str):
    if not isinstance(data, str):
        raise TypeError("Некорректный тип данных")
    if len(data) < 1:
        raise ValueError("Пустые строки вводить нельзя!")
    return True

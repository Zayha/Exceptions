from ui_console import get_data_from_console
from parsing import get_valid_data
from exceptions import UnexpectedLengthOfList
from files import write_from_file


def main():
    while True:
        try:
            result = (get_valid_data(get_data_from_console()))
            break
        except UnexpectedLengthOfList as ex:
            print(ex)
        except ValueError as ex:
            print(ex)
    try:
        write_from_file(result, 'files')
    except FileNotFoundError as ex:
        print(ex, "Отсутствие файл или директория")
    except PermissionError as ex:
        print(ex, "Нет разрешения на доступ к файлу")
    except IOError as ex:
        print(ex)


if __name__ == '__main__':
    main()

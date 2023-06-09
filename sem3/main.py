from ui_console import get_data_from_console
from parsing import get_valid_data
from exceptions import UnexpectedLengthOfList


def main():

    while True:
        try:
            print(get_valid_data(get_data_from_console()))
            break
        except UnexpectedLengthOfList as ex:
            print(ex)
        except ValueError as ex:
            print(ex)


if __name__ == '__main__':
    main()

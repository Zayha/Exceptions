from hw2.ex1 import get_float
from hw2.ex4 import if_empty_string


def main():
    get_float()
    try:
        print(if_empty_string(""))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()

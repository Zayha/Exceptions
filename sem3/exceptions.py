class UnexpectedLengthOfList(Exception):
    def __init__(self, true_length: int, length: int):
        short = 'Данных для обработки недостаточно'
        long = 'Данных больше чем требуется'
        if length > true_length:
            self.message = long
        if length < true_length:
            self.message = short
        super().__init__(self.message)

    def __str__(self):
        return self.message


# class MoreDataThenExpected(Exception):
#     def __init__(self, data):
#         self.message = f'Проверьте корректность введенных данных: {data}'
#         super().__init__(self.message)
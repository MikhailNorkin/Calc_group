
from numpy import number


def get_number(input_string: str) -> int:
    '''
    Получение целого числа
    '''
    while True:
        try:
            num = int(input(input_string))
            return num
        except ValueError:
            print('Это не то ...')


def get_number_operation(input_string):
    '''
    Получение целого числа от 0 до 4
    '''
    while type:
        number_float = input(input_string)
        try:
            number_float = int(number_float)
            if number_float > 0 and number_float < 5:
                return number_float
        except ValueError:
            print('Неверный ввод данных!!!')

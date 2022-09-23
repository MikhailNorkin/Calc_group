# Рациональные числа — это целые и дробные числа (обыкновенные дроби,
# конечные десятичные дроби и бесконечные периодические дроби).
# Рациональное число — это число, которое можно представить
# в виде положительной или отрицательной обыкновенной дроби
# или числа ноль.
# Если число можно получить делением двух целых чисел,
# то это число рациональное.

from typing import Union


def sum_ratio(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    '''
    Функция вычисляет сумму рациональных чисел.
    '''
    sum_ratio_value = x + y
    return sum_ratio_value


def diff_ratio(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    '''
    Функция вычисляет разность рациональных чисел.
    '''
    diff_ratio_value = x - y
    return diff_ratio_value


def mult_ratio(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    '''
    Функция вычисляет произведение рациональных чисел.
    '''
    mult_ratio_value = x * y
    return mult_ratio_value


def div_ratio(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    '''
    Функция вычисляет деление рациональных чисел.
    '''
    div_ratio_value = x / y
    return div_ratio_value

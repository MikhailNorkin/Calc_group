
import check as ch
import controller as c


operants_1 = ch.get_number('Введите первое число \n')
operants_2 = ch.get_number('Введите второе число \n')

operantions = ch.get_number_operation(
    'Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n')


def view_result(result):
    print(f'\n \n \n \n Результат: \n ', result)

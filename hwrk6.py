"""Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# Ввод в строку через пробел
"""
input_str = input(
    "Введите первый элемент, разность и количество элементов (через пробел): "
)
a1, d, n = map(int, input_str.split())
"""

a1 = int(input("Введите первый элемент прогрессии 'a1': "))
d = int(input("Введите разность прогрессии 'd': "))
n = int(input("Введите количество элементов прогрессии 'n': "))
ar_progr = [a1 + i * d for i in range(n)]
print("Элементы арифметической прогрессии:", " ".join(map(str, ar_progr)))


"""Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)"""


def find_index_in_and_out_range(arr, min_value, max_value):
    in_range_index = []
    out_range_index = []

    for i in range(len(arr)):
        if min_value <= arr[i] <= max_value:
            in_range_index.append(i)
        else:
            out_range_index.append(i)

    return in_range_index, out_range_index


for_find_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_value = 5
max_value = 15
in_range, out_range = find_index_in_and_out_range(for_find_list, min_value, max_value)
print("Индексы из диапазона", min_value, "-", max_value, ":", in_range)
print("Индексы вне диапазона", min_value, "-", max_value, ":", out_range)

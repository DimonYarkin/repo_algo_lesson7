"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
import timeit
from statistics import median
from random import random


# Для сортировки будем использовать агоритм Шелла
def shell(seq):
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)


def my_median(my_list):
    my_list_m = my_list.copy()
    shell(my_list_m)
    print(f'Отсортированный массив: {my_list_m}')
    len_cent = len(my_list) // 2
    for i in range(len_cent):
        my_list_m.pop()
    return my_list_m.pop()


m = int(random() * 10)
len_arr = 2 * m + 1
my_list = list(map(int, [random() * 50 for _ in range(len_arr)]))
print(f'Число m = {m} длина массива {len_arr} сам исходный массив {my_list}')

print(f'Медиана расчитанная с помощью функции my_median: {my_median(my_list)}')

print(f'Медиана расчитанная с помощью функции median: {median(my_list)}')

print('Моя функция', timeit.timeit("my_median(my_list[:])", setup="from __main__ import my_median, my_list", number=1))
print('Системная функция', timeit.timeit("median(my_list[:])", setup="from __main__ import median, my_list", number=1))

'''
Моя функция 1.8188002286478877e-05
Системная функция 2.7789792511612177e-06

по результатам профилирования производительности
написанная функция работает значительно быстрей чем стандартная
'''

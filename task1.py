"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import timeit
import random

'''
Здесь просто реверсируем условие и все
'''


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_v2(lst_obj):
    n = 1
    n_step = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                n_step += 1
        if n_step == 0:
            break
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
orig_listv2 = orig_list.copy()
orig_list_timeit = orig_list.copy()
print(f'Исходный массив: {orig_list}')
print(f'Отсортированный массив: {bubble_sort(orig_list)}')
# Проверим доработанную сортировку на отсортированном списке
print(f'Отсортированный массив поле доработки: {bubble_sort_v2(orig_listv2)}')

# замеры 10
print(timeit.timeit("bubble_sort(orig_list_timeit[:])", setup="from __main__ import bubble_sort, orig_list_timeit",
                    number=10))
print('V2', timeit.timeit("bubble_sort_v2(orig_list_timeit[:])",
                          setup="from __main__ import bubble_sort_v2, orig_list_timeit", number=10))
print('Тест V2 на отсортированном списке ',
      timeit.timeit("bubble_sort_v2(orig_listv2[:])", setup="from __main__ import bubble_sort_v2, orig_listv2",
                    number=10))

'''
8.79329745657742e-05
V2 9.107898222282529e-05
Тест V2 на отсортированном списке  1.4444987755268812e-05
По результатам профилирования производительность версии 2 значительно повышается если 
массив уже отсортирован
иначе оптимизация не имеет смысла
'''

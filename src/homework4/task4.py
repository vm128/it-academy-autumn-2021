"""
4 Даны два списка чисел. Посчитайте, сколько различных чисел
входит только в один из этих списков
Задачу поместите в файл task4.py в папке src/homework4.
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 0]
list2 = [1, 2, 3, 4, 5, 22, 12, 34, 106]

a = set(list1)
b = set(list2)
c = a - b
print(len(c))









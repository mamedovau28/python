# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list_items = ['элемент', '15', 23]
for items in list_items:
    print(type(items))

list_items = ['элемент', '15', 23]
[print(type(items)) for items in list_items]

list_items = ['элемент', '15', 23]
a = [type(items) for items in list_items]
print(a)

list_items = ['элемент', '15', 23]
print([type(items) for items in list_items])

# Попробовала разными способами вывести данные

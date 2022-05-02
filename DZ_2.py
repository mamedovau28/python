# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

request = input('Введите список элементов: ')
list_items = list(request.split())
elements = len(list_items)
items, items2, sum_items = [], [], []
if elements % 2 == 0:
    for items, items2 in zip(list_items[::2], list_items[1::2]):
        sum_items.append(items2)
        sum_items.append(items)
    print(sum_items)
else:
    for items, items2 in zip(list_items[::2], list_items[1::2]):
        sum_items.append(items2)
        sum_items.append(items)
    sum_items.append(list_items[-1])
    print(sum_items)

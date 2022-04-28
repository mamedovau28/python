# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.

# Нужно собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.

# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

name_tuple = ()
name_list = []
name_dick = {'название': [], 'цена': [], 'количество': [], 'ед': []}
name_analiz_dick = {'название': [], 'цена': [], 'количество': [], 'ед': []}
name_analiz_list, price_analiz_list, quantity_analiz_list, unit_analiz_list = [], [], [], []
grant = 0
while True:
    print('Введите данные товара')
    name, price, quantity, unit = input('Название: '), int(input('Цена: ')), int(input('Количество: ')), input('Единица измрения: ')
    name_dick['название'], name_dick['цена'], name_dick['количество'], name_dick['ед'] = name, price, quantity, unit
    name_dick = name_dick.copy()
    grant += 1
    name_tuple = (grant, name_dick.copy())
    name_list.append(name_tuple)
    name_analiz_list.append(name)
    price_analiz_list.append(price)
    quantity_analiz_list.append(quantity)
    unit_analiz_list.append(unit)
    name_analiz_dick['название'], name_analiz_dick['цена'] = name_analiz_list, price_analiz_list
    name_analiz_dick['количество'], name_analiz_dick['ед'] = quantity_analiz_list, unit_analiz_list
    unit_analiz_list = list(dict.fromkeys(unit_analiz_list))
    name_0 = int(input('Если товары закончилися, тоставьте 0. Если есть, поставьте 1: '))
    if name_0 == 0:
        break
unit_analiz_list = set(unit_analiz_list)
print(name_list)
print(name_analiz_dick)

# 7. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

a = 3
b = 7
result = a / 10
result_day = a
day = 1
print('a = {}, b = {}'.format(a, b))
print('Результат:')
print('{}-й день: {}'.format(day, result_day))
while int(result_day) < b:
    result = a / 10
    result_day = result + a
    a += result
    day += 1
    print('{}-й день: {}'.format(day, result_day))
print('Ответ: на {} день спортсмен достиг результата — не менее {} км.'.format(day, b))

# Не знаю как сделать 2 и меньше цифр после запятой
# Не знаю как цифру перевести в надпись (10 в десять)

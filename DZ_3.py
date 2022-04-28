# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number_n = input('Введите число до 10: ')
number_nn = number_n + number_n
number_nnn = number_nn + number_n
amount = int(number_n) + int(number_nn) + int(number_nnn)
print('{} + {} + {} = {}'.format (number_n, number_nn, number_nnn, amount))


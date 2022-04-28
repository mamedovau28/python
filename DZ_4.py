# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# 1. Вариант, по решению самый простой
numbers_user = input('Введите целое положительное число: ')
if numbers_user.find('9') != -1:
    print(9)
elif numbers_user.find('8') != -1:
    print(8)
elif numbers_user.find('7') != -1:
    print(7)
elif numbers_user.find('6') != -1:
    print(6)
elif numbers_user.find('5') != -1:
    print(5)
elif numbers_user.find('4') != -1:
    print(4)
elif numbers_user.find('3') != -1:
    print(3)
elif numbers_user.find('2') != -1:
    print(2)
else:
    print(1)

# 2. Оооочень долго решала) но как решить с арифметическими операциями так и не поняла
numbers_user = input('Введите целое положительное число: ')
number_user = None
c = None
members = []
while c != 1:
    c = int(len(numbers_user))
    number_user = int(numbers_user[0])
    members.append(number_user)
    numbers_user = numbers_user[1:]
print(max(members))


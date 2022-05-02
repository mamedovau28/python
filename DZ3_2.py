# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

#1)
def information(**kwargs):
    return kwargs
print(information(имя='Юлия', фамилия='Мамедова', год_рождения=1991, город_проживания='Москва', email='m@yandex.ru', телефон='7985508...'))

#2)
def information(name, surname, year_of_birth, city_of_residence, email, telefon):
    return name, surname, year_of_birth, city_of_residence, email, telefon
print(information('Юлия', 'Мамедова', 1991, 'Москва', 'm@yandex.ru', '7985508...'))

#3)
def information(name='Юлия', surname='Мамедова', year_of_birth=1991, city_of_residence='Москва', email='m@yandex.ru', telefon='7985508...'):
    return name, surname, year_of_birth, city_of_residence, email, telefon
print(information())

#4)
def information(name=input('Имя: '), surname=input('Фамилия: '), year_of_birth=input('Год рождения: '), city_of_residence=input('Город проживания: '), email=input('email: '), telefon=input('Телефон: ')):
    return name, surname, year_of_birth, city_of_residence, email, telefon
print(information())

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
season_list = []
season_dick = {}
if month == 12 or 1 <= month < 3:
    season_list = ['Зима', month]
    season_dick = dict(Зима=month)
elif 3 <= month < 6:
    season_list = ['Весна', month]
    season_dick = dict(Весна=month)
elif 6 <= month < 9:
    season_list = ['Лето', month]
    season_dick = dict(Лето=month)
else:
    season_list = ['Осень', month]
    season_dick = dict(Осень=month)
print(season_list)
print(season_dick)

month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
season_list = ['Зима', 'Весна', 'Лето', 'Осень']
if month == 12 or 1 <= month < 3:
    print(season_list[0])
    season_dick = {'Зима': []}
    for season in season_dick.keys():
        print(season)
elif 3 <= month < 6:
    print(season_list[1])
    season_dick = {'Весна': []}
    for season in season_dick.keys():
        print(season)
elif 6 <= month < 9:
    print(season_list[2])
    season_dick = {'Лето': []}
    for season in season_dick.keys():
        print(season)
else:
    print(season_list[3])
    season_dick = {'Осень': []}
    for season in season_dick.keys():
        print(season)

# Не совсем поняла условия, что именно нужно вывести в ответ. Сделала 2 варианта. Как сократить код, пока не знаю
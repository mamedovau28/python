# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# 1 Вариант решения
seconds = int(input('Введите время в секундах: '))
hour = seconds // 3600
minute = seconds // 60 - hour * 60
seconds_remains = seconds - hour * 3600 - minute * 60
if hour < 10 and minute < 10 and seconds_remains < 10:
    print('0{}:0{}:0{}'.format(hour, minute, seconds_remains))
elif hour < 10 and minute < 10 and seconds_remains >= 10:
    print('0{}:0{}:{}'.format(hour, minute, seconds_remains))
elif hour < 10 and minute >= 10 and seconds_remains >= 10:
    print('0{}:{}:{}'.format(hour, minute, seconds_remains))
elif hour < 10 and minute >= 10 and seconds_remains < 10:
    print('0{}:{}:0{}'.format(hour, minute, seconds_remains))
elif hour >= 10 and minute >= 10 and seconds_remains < 10:
    print('{}:{}:0{}'.format(hour, minute, seconds_remains))
elif hour >= 10 and minute < 10 and seconds_remains >= 10:
    print('{}:0{}:{}'.format(hour, minute, seconds_remains))
elif hour >= 10 and minute < 10 and seconds_remains < 10:
    print('{}:0{}:0{}'.format(hour, minute, seconds_remains))
else:
    print('{}:{}:{}'.format(hour, minute, seconds_remains))
# Знаю, что задание не довалось, но хотелось попробовать на основе знаний, что получила на подготовительном курсе.

# 2 Вариант решения
seconds = int(input('Введите время в секундах: '))
hour = seconds // 3600
minute = seconds // 60 - hour * 60
seconds_remains = seconds - hour * 3600 - minute * 60
if int(hour) < 10:
    hour = '0' + str(hour)
if int(minute) < 10:
    minute = '0' + str(minute)
if int(seconds_remains) < 10:
    seconds_remains = '0' + str(seconds_remains)
print('{}:{}:{}'.format(hour, minute, seconds_remains))

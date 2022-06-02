def rate_DZ1():
    time_work = int(input('Сколько часов отработал сотрудник? '))
    rate_hour = 550
    premium = int(input('Какую премию получит сотрудник? '))
    all_rate = time_work * rate_hour + premium
    print(f'Заработная плата сотрудника в этом месяце составила: {all_rate}')

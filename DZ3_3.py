#Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(a,b,c):
    if  c >= a <= b:
        return c + b
    elif c >= b <= a:
        return c + a
    else:
        return a + b
print(my_func(5, 5, 1))


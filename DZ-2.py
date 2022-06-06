my_file = open('DZ-2.txt', 'rt')
while True:
    data = my_file.readline()
    words = data.split()
    print('Количество слов в строке :', len(words))
    if len(words) == 0:
        break
my_file.close()
my_file2 = open('DZ-2.txt', 'rt')
sum_str = sum(1 for line in my_file2)
print('Количество строк :', sum_str)
my_file2.close()

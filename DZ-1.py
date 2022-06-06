new_file = open('DZ-1.txt', 'w')
text_info = None
while True:
    text_info = input('Введите текст: ')
    if len(text_info) == 0:
        break
    new_file.writelines(f"{text_info}\n")
new_file.close()

import re

try:
    f = open('myFile.html', 'r')
    s = f.read()
    result = re.findall('\w+@\w+\.\w+', s)
    if result:
        print("Результаты поиска: ", result)
        f.close()
    else:
        print("Совпадений не найдено")
except FileNotFoundError:
    print("Файл не найден!")















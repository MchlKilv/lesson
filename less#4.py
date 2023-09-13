# def f(x):
#     return x * x


# a = f
# print(a(5))
# print(f(5) # передача ссылкой


# def calk1(a, b):  # a, b - несколько перем
#     return a + b


# def calk2(a, b):
#     return a * b


# def math(op, x, y):
#     print(op(x, y))


# math(calk1, 5, 45)  # calk1, calk2... передаем по ссылке в ор


# lambda func
# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# # lambda a, b: a + b

# math(lambda a, b: a + b, 5, 45)  # calk1, calk2... передаем по ссылке в ор
"""
lis_t = [1, 2, 3, 5, 8, 15, 23, 38]
res = list()

for i in lis_t:
    if i % 2 == 0:
        res.append((i, i**2))
print(res)
"""

"""
def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

lis_t = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, lis_t)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)
"""

# функция map
"""
list_1 = [x for x in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)
"""
"""
data = "10 12 13 15 57 8 6 5 4"
print(data)

data = list(map(int, data.split()))
print(data)
"""

# filter
"""
data = [0, 12, 13, 15, 57, 8, 6, 5, 45]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)

lis_t = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, lis_t)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)
"""

# f zip
# f enumerate

# работа с файлами

# a - открытие для добавления данных
# r - откр для чтения, r+ - открыть для чтения и дописывать
# w - откр для записи, w+ - откр для записи и читать

"""
Примеры использования различных режимов в коде:
Режим a
 colors = ['red', 'green', 'blue']
 data = open('file.txt', 'a')          # здесь указываем режим, в котором будем работать
 data.writelines(colors)               # разделителей не будет
 data.close()

data.close() — используется для закрытия файла, чтобы разорвать подключение файловой
переменной с файлом на диске.
exit() — позволяет не выполнять код, прописанный после этой команды в скрипте.
В итоге создаётся текстовый файл с текстом внутри: redbluedreen.
При повторном выполнении скрипта redbluedreenredbluedreen — добавление в
существующий файл, а не перезапись файлов.

Ещё один способ записи данных в файл:
with open('file.txt', 'w') as data:
 data.write('line 1\n')
 data.write('line 2\n')

Режим r - Чтение данных из файла:
 path = 'file.txt'
 data = open(path, 'r')
 for line in data:
 print(line)
 data.close()

Режим w
 colors = ['red', 'green', 'blue']
 data = open('file.txt', 'w')
 data.writelines(colors) # разделителей не будет
data.close()

В итоге создаётся текстовый файл с текстом внутри: ‘redbluedreen’.
В случае перезаписи новые данные записываются, а старые удаляются.
"""

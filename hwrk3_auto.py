"""
k = input('enter word ')
points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_en:
            if i in points_ru[j]:
                count = count + j
print(count)"""


list_1 = [1, 2, 3, 4, 5, 70, 55, 12, 8, 3, 4]
k = 40
m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)

closest_element = None
min_difference = float("inf")  # Начальное значение для минимальной разницы
for num in list_1:
    difference = abs(num - k)
    if difference < min_difference:
        min_difference = difference
        closest_element = num

print(closest_element)

list_1 = [1, 2, 3, 4, 5, 3, 3, 3]
lk = 3

count = list_1.count(lk)
print(count)

count = 0
for i in range(len(list_1)):
    if list_1[i] == lk:
        count += 1
print(count)

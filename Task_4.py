# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

numA = int(input())
numB = ''

while numA > 0:
    numB = str(numA % 2) + numB
    numA = numA // 2

print(numB)

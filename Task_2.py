# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


list = [2, 3, 4, 5, 6]


def multiList(list):
    l = len(list)//2 + 1 if len(list) % 2 != 0 else len(list)//2
    nList = [list[i]*list[len(list)-i-1] for i in range(l)]
    print(nList)


x = multiList(list)



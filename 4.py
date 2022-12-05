# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input("Введите число: "))
elements = list(range( - N, N + 1))
print(elements)
result = 1
pos = open('file.txt', 'r')
for i in pos:
    print(i)
    result *= elements[int(i)]
pos.close()
print(result)


# import random
# n=int(input('input number '))
# list=[]
# for i in range(n):                      # генератор случайных чисел
#     a=random.randint(-n, n)
#     list.append(a)   
# print (list)
# index_list = input(f'введите позиции элементов от 1 до {n} через пробел').split()
# result=1
# for j in range(len(index_list)):        # перебор элементов с номерами позиций
#     a=int(index_list[j])-1
#     print (f'{result}*{int(list[a])}', end=' ')
#     result*=int(list[a])    
# print (f'= {result}')


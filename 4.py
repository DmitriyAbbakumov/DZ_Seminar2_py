# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input("Введите число: "))
elements = list(range(-N, N+1))
print(elements)
result = 1
pos = open('file.txt', 'r')
for i in pos:
    print(i)
    result *= elements[int(i)]
pos.close()
print(result)

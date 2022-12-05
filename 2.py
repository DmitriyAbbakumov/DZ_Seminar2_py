# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input("Введите число: "))
factorial = 1
elements = list()
for i in range(1, N + 1):
    factorial *= i
    elements.append(factorial)
print(elements)


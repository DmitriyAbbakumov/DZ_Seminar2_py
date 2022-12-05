# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input())
# elements = list()
# for i in range(1, n+1):
#     elements.append(round((1+1/i)**i, 3))
# print(elements)
# print(sum(elements))



n = int(input("Введите число: "))
print(sum([round((1 + 1 / i) ** i, 3) for i in range(1, n + 1) ]))

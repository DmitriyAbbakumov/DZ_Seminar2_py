# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

from tkinter import N


n = (input())
sum = 0
for i in n:
    if i != '.':
        sum += int(i)
print(sum)








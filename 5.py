# Реализуйте алгоритм перемешивания списка.

import random
spisok1 = [1, 3, 'df', '3d3', 8.8]
print(spisok1)
spisok2 = spisok1[:]
print(spisok2)
for i in range(len(spisok2)):
    index = random.randint(0, len(spisok2)-1)
    spisok2[i], spisok2[index] = spisok2[index], spisok2[i]
print(spisok2)

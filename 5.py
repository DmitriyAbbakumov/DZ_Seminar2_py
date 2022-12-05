# Реализуйте алгоритм перемешивания списка.

import random
list1 = [1, 3, 'df', '3d3', 8.8]
print(list1)
for i in range(len(list1)):
    index = random.randint(0, len(list1)-1)
    list1[i], list1[index] = list1[index], list1[i]
print(list1)


# import random 
# y = ['Apple', '2 ', '-5675 ', '0.678 ', 'morning']
# random.shuffle(y)
# print(y)

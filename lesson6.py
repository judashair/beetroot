# task1
from random import randint

x = 0
list_of_numbers = list()
while x < 10:
    x += 1
    list_of_numbers.append(randint(0, 100))
print(max(list_of_numbers))

# task2
from random import randint

list_1, list_2, list_3 = [randint(0, 100) for _ in range(10)], [randint(0, 100) for _ in range(10)], []
x = 0
while x < 10:
    if list_1[x] in list_2:
        list_3.append(list_1[x])
    x += 1
print(list_3 if list_3 else "No duplicates.")

# task3
list_1, list_2 = list(range(1, 101)), []
i = 0
while i < len(list_1):
    if list_1[i] % 7 == 0 and not list_1[i] % 5 == 0:
        list_2.append(list_1[i])
    i += 1
print(list_2)

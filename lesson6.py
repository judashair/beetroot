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

list1, list2, list3 = [randint(0, 10) for i in range(10)], [randint(0, 10) for i in range(10)], []
i = 0
print(list1)
print(list2)
while i < 10:
    if list1[i] in list2:
        list3.append(list1[i])
    i += 1

print(list3 if list3 else "Повторень немає.")

# task3
list_1, list_2 = list(range(1, 101)), []
i = 0
while i < len(list_1):
    if list_1[i] % 7 == 0 and not list_1[i] % 5 == 0:
        list_2.append(list_1[i])
    i += 1
print(list_2)

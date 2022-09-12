# task 1

users_str = input("string: ").split()
list_words = []
for i in users_str:
    word_count = users_str.count(i)
    list_words.append((i, word_count))

slovar = dict(list_words)

print(slovar)

# task 2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_price = 0
for elem in stock:
    if elem in prices:
        total_price += stock[elem] * prices[elem]

print(total_price)

# task 3
list_of_tuples = []
for i in range(1, 10):
    j = i ** 2
    list_of_tuples.append((i, j))
print(list_of_tuples)
# or
print([(i, i ** 2) for i in range(1, 11)])

# task 4
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

week_days = {i: day for i, day in enumerate(days, 1)}
print(week_days)

reversed_dict = {value: key for key, value in week_days.items()}
print(reversed_dict)

# task_1
import random
number = random.randint(1, 10)

while True:
    user_number = int(input(f"Guess number in the range (1, 10):\n"))

    if (user_number < 1) or (10 < user_number):
        print("You are out of range.")
    elif user_number == number:
        print("Congratulations!!")
    elif number > user_number:
        print(f"The number is greater than {user_number}.")
    elif number < user_number:
        print(f"The number is less than {user_number}.")

# task_2
name = str(input("Enter your name: "))
age = int(input('Enter your age: '))
greeting = f"Hello {name.title()}, on your next birthday you’ll be {age + 1} years"

print(greeting)

# task_3
import random

game_word = str(input("Give me your characters: "))
for i in range(5):
    print("".join(random.sample(game_word, k=len(game_word))))

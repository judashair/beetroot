"""
author: Anna Samsonenko
date: 02.09.2022
"""

# lesson3_task1
a = "helloworld"
b = "my"
c = "x"
if len(a) < 2:
    print(" ")
else:
    print(a[0:2] + a[-2:])

if len(b) < 2:
    print(" ")
else:
    print(b[0:2] + b[-2:])

if len(c) < 2:
    print("' '")
else:
    print(c[0:2] + c[-2:])

# task2

phone_number = str(input("Please, enter your phone number: "))
if (len(phone_number) == 10) and phone_number.isdigit():
    print("Your phone number is okay.")
else:
    print("Please, enter 10 numbers!")

# task3
quiz = "A Simple Math Quiz: 12 + 5 * 10?"
print(quiz)
answer = int(input("Please, enter your answer: "))

if answer == 62:
    print("Correct.")
else:
    print("Incorrect.")

# task4
name = "anna"
enter_name = input("Enter your name: ")

if (name == enter_name.title()) or (name == enter_name.capitalize()) or (name == enter_name.lower()) or (name == enter_name.upper()):
    print("True")
else:
    print("False")

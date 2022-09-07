import random

lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
uppercase_alphabet = lowercase_alphabet.upper()
numbers = "0123456789"
special_characters = "!?#$%^&*()+@-"
characters_set = "" + lowercase_alphabet

print("By default password creates from english alphabet in lower case.")


while True:
    answer_u = input("Do you want to add upper case letters to your random password? YES/NO: ")
    if answer_u == "NO" or answer_u == "YES":
        break
    else:
        print("You typed wrong answer. Please enter YES or NO: ")

if answer_u == "YES":
    characters_set = characters_set + uppercase_alphabet

while True:
    answer_n = input("Do you want to add numbers to your random password? YES/NO: ")
    if answer_n == "NO" or answer_n == "YES":
        break
    else:
        print("You typed wrong answer. Please enter YES or NO: ")

if answer_n == "YES":
    characters_set = characters_set + numbers

while True:
    answer_s = input("Do you want to add special characters to your random password? YES/NO: ")
    if answer_s == "YES" or answer_s == "NO":
        break
    else:
        print("You typed wrong answer. Please enter YES or NO: ")
if answer_s == "YES":
    characters_set = characters_set + special_characters

print("Set of symbols to create password:", "".join(characters_set), end="\n\n")

print("Password should be not lower than 6 symbols and not more than 32")

while True:
    password_length = int(input("Enter number between 6 and 32: "))
    if 6 <= password_length <= 32:
        break
    else:
        print("You typed wrong number.")


password = random.choices(characters_set, k = password_length)
print("".join(password))

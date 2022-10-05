import random
import json


def print_cars(cars: dict) -> None:
    print(f"Default cars list: {json.dumps(cars, indent=4)}")


car_dict = dict
car_dict = {"Mercedes-benz": {"car_model": "C63_AMG", "engine": "2.0", "power": "671",
                              "0-100": round(random.uniform(3.3, 3.8), 2)},
            "Infiniti": {"car_model": "Q50", "engine": "3.0", "power": "405",
                         "0-100": round(random.uniform(5.1, 5.6), 2)},
            "Nissan":   {"car_model": "GTR", "engine": "3.8", "power": "565",
                         "0-100": round(random.uniform(2.7, 3.4), 2)}
            }

print(f"Default car list is: ")
print_cars(car_dict)
cars_list = []
for key in car_dict:
    cars_list.append(key)
print(f"Shortlist with car brands: {cars_list}")


def car_add_to_list():
    car = input("Enter car brand: ").capitalize()
    car_model = input("Enter car model: ").capitalize()
    engine = input("Enter engine: ")
    power = input("Enter horsepower: ")
    speed = float(input("Enter speed: "))

    car_dict[car] = {"car_model": car_model,
                     "engine": engine,              
                     "power": power,
                     "0-100": float(round(random.uniform(speed - 0.3, speed + 0.6), 2))}


def car_add():
    print("Do you want to add new car to the list? If yes enter 'yes', if no enter 'no'. Your choice:  ")
    answer = input().lower()
    while answer == "yes":
        car_add_to_list()
        answer = input("Do you want to add another car? Print 'yes' or 'no'. Your choice:  ").lower()

        if answer == "no":
            print("Here is car list")
            print_cars(car_dict)
            break


car_add()
new_cars_list = []
for key in car_dict:
    new_cars_list.append(key)
print(new_cars_list)


def race():
    first_car = input("Choose the car from the list: ").capitalize()
    second_car = input("Choose the car from the list: ").capitalize()

    first_car_speed = (car_dict.get(first_car).get("0-100"))
    second_car_speed = (car_dict.get(second_car).get("0-100"))

    print(f"{first_car}'s speed is {first_car_speed}")
    print(f"{second_car}'s speed is {second_car_speed}")

    if first_car_speed < second_car_speed:
        print(f"{first_car} wins.")
    else:
        print(f"{second_car} wins.")


def exit_or_no():
    end = input("Do you wanna race? Enter yes/no(for exit): ").lower()
    while end == "yes":
        car_add()
        race()
        exit_or_no()
    if end == "no":
        exit()


exit_or_no()

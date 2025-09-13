from pprint import pprint

cars_info = []

for i in range(2):
    car = input("Mashina: ").title()
    year = input("Yili: ")

    cars_info.append([car, year])

pprint(cars_info)
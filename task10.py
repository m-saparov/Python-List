
fruits = ["Olma", "Anor", "Banan", "Gilos"]

print(f"Mevalar: {fruits}")

index = int(input("Qaysi indeksdagi elementni o'zgartirmoqchisiz? (1-4): "))
new_value = input("Yangi qiymatni kiriting: ").capitalize()

fruits[index - 1] = new_value

print(fruits)

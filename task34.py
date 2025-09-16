def find_pairs(numbers: list) -> list:
    new_list = []
    n = len(numbers)

    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == 10:
                new_list.append((numbers[i], numbers[j]))

    return new_list


def main():
    numbers = []
    for i in range(6):
        num = int(input(f"{i+1}-sonni kiriting: "))
        numbers.append(num)

    result = find_pairs(numbers)
    print("Yig'indisi 10 bo'lgan juftliklar:", result)


main()

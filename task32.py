def get_list(count: int) -> list:
    elements = []
    for i in range(count):
        element = input(f"{i + 1}-Element: ")
        elements.append(element)
    return elements


def get_bigger(elements: list) -> list:
    new_list = []

    for i in elements:
        if len(i) > 5:
            new_list.append(i)

    return new_list
    


def main():
    count = int(input("List element soni: "))
    elements = get_list(count)

    print("bigger texts: ", get_bigger(elements))


main()

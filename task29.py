def get_list(count: int) -> list:
    elements = []
    for i in range(count):
        element = input(f"{i + 1}-Element: ")
        elements.append(element)
    return elements


def unique_elements(elements: list) -> list:
    new_list = []
    for i in elements:
        counter = 0
        for j in elements:
            if i == j:
                counter += 1
        if counter == 1:
            new_list.append(i)
    return new_list


def main():
    new_list = get_list(10)
    get_unique = unique_elements(new_list)
    print("Faqat 1 marta uchragan elementlar:", get_unique)


main()

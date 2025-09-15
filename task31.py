def get_list(count: int) -> list:
    elements = []
    for i in range(count):
        element = input(f"{i + 1}-Element: ")
        elements.append(element)
    return elements


def get_common(elements: list):
    most_common = elements[0]
    max_count = 1

    for i in elements:
        if elements.count(i) > max_count:
            max_count = elements.count(i)
            most_common = i
    
    return most_common
    


def main():
    count = int(input("List element soni: "))
    elements = get_list(count)

    print("Eng ko'p qatnashgan: ", get_common(elements))


main()

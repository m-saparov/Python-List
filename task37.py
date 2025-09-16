def swap_lists(list1: list, list2: list):
    n1 = len(list1)
    n2 = len(list2)

    if n1 != n2:
        return "Listlarning uzunligi bir xil emas!"
    
    for i in range(n1):
        list1[i], list2[i] = list2[i], list1[i]

    return list1, list2


def get_list(count: int) -> list:
    elements = []
    for i in range(count):
        element = input(f"{i + 1}-Element: ")
        elements.append(element)
    return elements


def main():
    count = int(input("List element soni: "))

    print("\n--- 1-listni kiriting ---")
    elements1 = get_list(count)

    print("\n--- 2-listni kiriting ---")
    elements2 = get_list(count)

    print("\nAlmashtirishdan oldin:")
    print("1-list:", elements1)
    print("2-list:", elements2)

    result1, result2 = swap_lists(elements1, elements2)

    print("\nAlmashtirilgandan keyin:")
    print("1-list:", result1)
    print("2-list:", result2)


main()

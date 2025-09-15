def get_list(count: int) -> list:
    elements = []
    for i in range(count):
        element = input(f"{i + 1}-Element: ")
        elements.append(element)
    return elements

def get_intersection(list1: list, list2: list) -> list:
    new_list = []
    for i in list1:
        if i in list2 and i not in new_list:
            new_list.append(i)
            
    return new_list


def main():
    count1 = int(input("1-List element soni: "))
    elements1 = get_list(count1)
    count2 = int(input("2-List element soni: "))
    elements2 = get_list(count2)

    print("Umumiylar: ", get_intersection(elements1, elements2))

main()

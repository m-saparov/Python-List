def get_list(count: int) -> list:
    elements = []
    for i in range(count):
        element = input(f"{i + 1}-Element: ")
        elements.append(element)

    return elements


def get_palindrome(elements: list) -> list:
    new_list = []

    for i in elements:
        if i == i[::-1]:
            new_list.append(i)
    
    return new_list

def main():
    elements = get_list(5)
    palindrome_list = get_palindrome(elements)

    if palindrome_list:
        print("Palindromlar:", palindrome_list)
    else:
        print("Hech qanday palindrom topilmadi!")


main()

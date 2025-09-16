
def get_longer(texts: list) -> str:
    longer = texts[0]
    max_size = len(texts[0])

    for i in texts:
        if len(i) > max_size:
            max_size = len(i)
            longer = i
    
    return longer

def main():
    words = []

    for i in range(6):
        word = input(f"{i+1}-so'zni kiriting: ")
        words.append(word)
    
    result = get_longer(words)

    print("Eng uzun  so'z: ", result)


main()
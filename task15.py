numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

start_index = int(input("Starting Index(1-15): ")) - 1
end_index = int(input("Ending Index(1-15): ")) - 1

if start_index <= end_index:
    print(numbers[start_index : end_index + 1])
else:
    print(numbers[start_index : end_index - 1 : -1])

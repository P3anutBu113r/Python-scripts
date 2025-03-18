def find_max(numbers):
    i = 1
    while len(numbers) > 1:
        if numbers[0] > numbers[1]:
            numbers.remove(numbers[1])
        elif numbers[0] < numbers[1]:
            numbers.remove(numbers[0])
    return numbers
list = [12, 45, 23, 67, 9]
print(find_max(list))

import random

def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    random_list_numbers = []
    while len(random_list_numbers) < 15:
        random_int = random.randint(-10, 10)
        hasNumber = False
        for i in random_list_numbers:
            if i == random_int:
                hasNumber = True
        if hasNumber == False:
            random_list_numbers.append(random_int)
    return random_list_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

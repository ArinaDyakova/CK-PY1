list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
#необходимо найти индекс максимального числа
max_index = 0
max_number = list_numbers[max_index]

for i, current_number in enumerate(list_numbers): #перебераем все индексы
    if current_number >= max_number: #если текущее значение числа больше или равно того, который встречали ранее
        max_index = i #то перезаписываем индекс максимального числа
        max_number = list_numbers[max_index]

# TODO Оформить решение
list_numbers[max_index], list_numbers[-1] = list_numbers[-1], max_number
print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
#пустая строка, пишу комментарием, так как у меня она исчезает при загрузке в github

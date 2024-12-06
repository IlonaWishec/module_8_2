def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for i in numbers:
        try:
            result += i
        except TypeError:
            print(f'Некорректный тип данных для подсчета суммы - {i}')
            incorrect_data += 1

    return result, incorrect_data

def calculate_average(numbers):
    try:
        iter(numbers)
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    try:
        result, incorrect_data = personal_sum(numbers)
        count = len(numbers) - incorrect_data
        return result / count if count > 0 else 0
    except ZeroDivisionError:
        return 0

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
# Некорректный тип данных для подсчета суммы - 1
# Некорректный тип данных для подсчета суммы - ,
# Некорректный тип данных для подсчета суммы -
# Некорректный тип данных для подсчета суммы - 2
# Некорректный тип данных для подсчета суммы - ,
# Некорректный тип данных для подсчета суммы -
# Некорректный тип данных для подсчета суммы - 3
# Результат 1: 0
# Некорректный тип данных для подсчета суммы - Строка
# Некорректный тип данных для подсчета суммы - Ещё Строка
# Результат 2: 2.0
# В numbers записан некорректный тип данных
# Результат 3: None
# Результат 4: 26.5
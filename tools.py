# Возвращает список данных с заданного столбца
def read_data(sheet, column_symbol):
    data = []

    for row in range(2, sheet.max_row + 1):
        value = sheet[column_symbol + str(row)].value

        if value is None:  # Если дошли до конца столбца
            break

        data.append(value)

    return data


# Возвращает среднее число заданного столбца
def calculate_average_for_column(sheet, column_symbol):
    sum, counter = 0, 0

    for row in range(2, sheet.max_row + 1):
        value = sheet[column_symbol + str(row)].value

        if value is None:   # Если дошли до конца столбца
            break

        sum += value
        counter += 1

    return sum / counter


# Выводит минимальное/максимальное/среднее из данных
def output_min_max_avg_data(data):
    min, max = 100, 0
    counter, sum = 0, 0

    for value in data:

        if max < value:
            max = value

        if min > value:
            min = value

        sum += value
        counter += 1

    avg = sum / counter

    print(f"Минимальное значение: {min}\n"
          f"Максимальное значение: {max}\n"
          f"Среднее значение: {avg}")

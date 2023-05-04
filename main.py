from openpyxl import load_workbook  # Импортируем функцию для чтения таблиц
from chart import *     # Импортируем класс Chart для построения диаграмм
from tools import *     # Импортируем инструменты для работы с Excel
from point import *

book = load_workbook("./test.xlsx", read_only=True)
sheet = book.active

data = read_data(sheet, 'D')  # Считываем данные с таблицы
average_balls = calculate_average_for_column(sheet, 'D')    # Рассчитываем среднее значение баллов
output_min_max_avg_data(data)

canvas = Chart()

canvas.draw_histogram(data, 12, "Количественная вероятность", 0.8, colors[13])
canvas.draw_vertical_line(Point(average_balls, 4), colors[0])

canvas.set_label_x('Баллы')
canvas.set_label_y('Количество студентов')
canvas.set_title("Баллы студентов группы ИТ/ЦТ-49Д")
canvas.set_legend()
canvas.set_lim_y(0, 4)
canvas.set_lim_x(0, 100)

plt.show()

"""Класс Chart рисует диаграммы"""

import matplotlib.pyplot as plt             # Для построения графиков
from matplotlib.ticker import MaxNLocator   # Для изменения типа данных оси Oy на графике
from point import *     # Импортируем класс Point
from colors import *    # Импортируем список цветов


def decorator(func):
    """Проверяет входные данные (Tuple or Point) для координат.
    Конвертирует Tuple в Point для использования в Chart."""
    def wrapper(*args):
        index = 0
        for arg in args:
            if type(arg) is tuple:
                coordinates = Point(arg)
                temp_list = list(args)
                temp_list[index] = coordinates
                func(*temp_list)
                return
            elif type(arg) is Point:
                func(*args)
                return
            else:
                index += 1
    return wrapper


class Chart:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        self.ax.set_facecolor(colors[11])
        self.ax.grid(True, ls=':', c=colors[6], alpha=0.3, zorder=0)
        self.ax.yaxis.set_major_locator(MaxNLocator(integer=True))  # Устанавливаем по оси Oy целочисленную градацию

    def draw_histogram(self, data, bins, text, alpha, color):
        """Рисует гистограмму"""
        self.ax.hist(
            data,               # Массив данных для построения
            bins=bins,          # Кол-во частотных диапазонов (карманов)
            label=text,         # Подпись рядом с цветом в легенде
            density=False,      # Гистограмма в виде плотности вероятности (S==1)
            alpha=alpha,        # Прозрачность
            linewidth=2,        # Толщина линии прямоугольников
            linestyle='-',      # Стиль линии
            edgecolor='black',  # Цвет линии
            facecolor=color)    # Цвет заливки прямоугольников гистограммы


    @decorator
    def draw_vertical_line(self, point, color):
        """Рисует вертикальную линию"""
        self.ax.vlines(         # Рисуем вертикальную линии
            point.x,          # Координата по "X"
            0, point.y,          # Начало и конец по "Y"
            colors=color,       # Цвет линии
            linewidth=2.5,      # Толщина линии
            linestyles='--')    # Стиль Лини

    def draw_horizontal_line(self, x_l, y_l, x_r, y_r):
        """Рисует горизонтальную линию (l-left, r-right)"""
        self.ax.annotate(
            text='',                                    # Подпись у линии
            xy=(x_l, y_l),                              # Левые координаты (x,y) линии
            xytext=(x_r, y_r),                          # Правые координаты (x,y) линии
            arrowprops={'arrowstyle': '-', 'lw': 1.5})  # Тип линии и её толщина

    def draw_kernel_density_line(self, xx, probes, color):
        """Рисует огибающую графика"""
        self.ax.plot(xx, probes, lw=3.5, c=color)

    def draw_double_arrow(self, x_l, y_l, x_r, y_r):
        """Рисует двойную стрелку (l-left, r-right)."""
        self.ax.annotate(                               # Рисуем двойную стрелку
            text='',                                    # Подпись у стрелки отсутствует
            xy=(x_l, y_l),                              # Левые координаты (x,y) стрелки
            xytext=(x_r, y_r),                          # Правые координаты (x,y) стрелки
            arrowprops={'arrowstyle': '<->', 'lw': 1})  # Тип стрелки и её толщина

    @decorator
    def draw_text(self, point, text, color):
        """Рисует текст"""
        self.ax.text(
            x=point.x,    # X координата начала подписи
            y=point.y,    # Y координата начала подписи
            s=text,         # Текст подписи
            fontsize=14,    # Размер шрифта
            color=color)

    def set_lim_x(self, point_start, point_end):
        """Устанавливает пределы оси X"""
        self.ax.set_xlim(point_start, point_end)

    def set_lim_y(self, point_start, point_end):
        """Устанавливает пределы оси Y"""
        self.ax.set_ylim(point_start, point_end)

    def set_label_x(self, text, fontsize=15):
        """Устанавливает подпись оси X"""
        self.ax.set_xlabel(text, fontsize=fontsize)

    def set_label_y(self, text, fontsize=15):
        """Устанавливает подпись оси Y"""
        self.ax.set_ylabel(text, fontsize=fontsize)

    def set_title(self, text, fontsize=15):
        """Устанавливает подпись в заголовке"""
        self.ax.set_title(text, fontsize=fontsize)

    def set_legend(self, loc="upper right", fontsize=12):
        """Устанавливает легенду у графика"""
        self.ax.legend(loc=loc, fontsize=fontsize)

    def get_axis(self):
        """Возвращает указатель на Axis"""
        return self.ax

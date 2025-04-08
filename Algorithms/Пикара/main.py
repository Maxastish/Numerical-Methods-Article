from math import cos
def picard_method(f, y0, x0, xn, h, max_iter=100, xol=1e-6):
    """
    Метод Пикара для решения нелинейных дифференциальных уравнений.

    :param f: Функция правой части уравнения f(x, y).
    :param y0: Начальное значение y(x0).
    :param x0: Начальное значение времени.
    :param xn: Конечное значение времени.
    :param h: Шаг интегрирования.
    :param max_iter: Максимальное количество итераций.
    :param xol: Точность метода.
    :return: Список значений времени и соответствующих значений y(x).
    """
    result = [(x0, y0)]
    x = x0
    y = y0
    for _ in range(max_iter):
        y_new = y0
        for i in range(1, int((xn - x0) / h) + 1):
            y_new += h * f(x0 + (i - 1) * h, y_new)
        if abs(y_new - y) < xol:
            break
        y = y_new
    while x < xn:
        x = x + h
        y = y0
        for i in range(1, int(h / h) + 1):
            y += h * f(x - h + (i - 1) * h, y)
        result.append((x, y))
    return result


# Пример использования:

# Задаем дифференциальное уравнение: y'(x) = (1 - y * y) * cos(x) + 0.6 * y
def f(x, y):
    return (1 - y * y) * cos(x) + 0.6 * y

# Начальные условия
x0 = 0
xn = 1
y0 = 0
h = 0.02

# Получаем результаты с использованием метода Пикара
result = picard_method(f, y0, x0, xn, h)

# Выводим результаты
for x, y in result:
    print(f"x = {x}, y = {y}")
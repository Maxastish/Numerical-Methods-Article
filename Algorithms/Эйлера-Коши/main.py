from math import cos
def improved_euler_method(f, y0, x0, xn, h):
    result = [(x0, y0)]
    x = x0
    y = y0
    while x < xn:
        f1 = f(x, y)
        f2 = f(x + h, y + h * f1)
        y = y + h / 2 * (f1 + f2)
        x = x + h
        result.append((x, y))
    return result
# Пример использования:
# Задаем дифференциальное уравнение: y'(x) = x*y
def f(x, y):
    return x * y
# Задаем дифференциальное уравнение: y'(x) = (1 - y * y) * cos(x) + 0.6 * y
def f(x, y):
    return (1 - y * y) * cos(x) + 0.6 * y
# Начальные условия
x0 = 0
xn = 1
y0 = 0
h = 0.02
# Получаем результаты с использованием усовершенствованного метода Эйлера
result = improved_euler_method(f, y0, x0, xn, h)
# Выводим результаты
for x, y in result:
    print(f"x = {x}, y = {y}")
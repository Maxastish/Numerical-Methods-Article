from math import cos
def euler_method(f, y0, x0, xn, h):
    result = [(x0, y0)]
    x = x0
    y = y0
    while x < xn:
        y = y + h * f(x, y)
        x = x + h
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
# Получаем результаты с использованием метода Эйлера
result = euler_method(f, y0, x0, xn, h)
# Выводим результаты
for x, y in result:
    print(f"x = {x}, y = {y}")
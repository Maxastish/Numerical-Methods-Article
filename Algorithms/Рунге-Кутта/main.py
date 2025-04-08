from math import cos

def runge_kutta_method(f, y0, x0, xn, h):
    result = [(x0, y0)]
    x = x0
    y = y0
    while x < xn:
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y = y + (k1 + 2*k2 + 2*k3 + k4)/6
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
y0 = 1
h = 0.02
# Получаем результаты с использованием метода Рунге-Кутты
result = runge_kutta_method(f, y0, x0, xn, h)
# Выводим результаты
for x, y in result:
    print(f"x = {x}, y = {y}")
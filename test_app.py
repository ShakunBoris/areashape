"""
Задание:
    Напишите на C# или Python библиотеку для поставки внешним клиентам, 
которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. 
Дополнительно к работоспособности оценим:
    - Юнит-тесты
    + Легкость добавления других фигур
    + Вычисление площади фигуры без знания типа фигуры в compile-time
    + Проверку на то, является ли треугольник прямоугольным
"""
import areashape.areashape as ash

import tests

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


c = ash.Circle(3)
t = ash.Triangle((2,1), (3,6), (6,2))
print(f'Circle: calculate_area(Shape): {ash.calculate_area(c)}')
print(f'Circle: obj.area() method: {c.area()}')
print(f'Triangle: calculate_area(Shape): {ash.calculate_area(t)}')
print(f'Triangle: obj.area() method: {t.area()}')
print(f'Triangle: obj.is_right_angled : {t.is_right_angled}')


polygon = Polygon(t.vertexes)

fig, ax = plt.subplots(1,1)

ax.add_patch(polygon)

plt.ylim(0,10)
plt.xlim(0,10)

plt.show()
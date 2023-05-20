import math
class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def distance(self, other_point) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно, что точек каждого цвета ровно три,
# но порядок точек в списке произвольный
points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]
# Все точки одного цвета соединены линиями и образуют треугольник

# Задание-1: доработайте конструктор class Point для хранения цвета точки
# Задание-2: реализуйте метод distance()
# Задание-3: вычислите площади треугольников образованных из точек одного цвета(зеленый и красный)
# для вычисления площади можно использовать формулу Герона:
# math.sqrt(p * (p-a) * (p-b) * (p-c)), где p - это полупериметр; p=(a+b+c)/2
points_red = []
points_green = []
for point in points:
    if ( point.color == "red" ):
        points_red.append(point)
    else:
        points_green.append(point)

a_red = points_red[0].distance(points_red[1])
b_red = points_red[0].distance(points_red[2])
c_red = points_red[1].distance(points_red[2])
a_green = points_green[0].distance(points_green[1])
b_green = points_green[0].distance(points_green[2])
c_green = points_green[1].distance(points_green[2])
p_red = (a_red + b_red + c_red) / 2
p_green = (a_green + b_green + c_green) / 2

def S_triangle(p, a, b, c):
    return math.sqrt(p * (p-a) * (p-b) * (p-c))

print("Площадь красного треугольника = ", S_triangle(p_red, a_red, b_red, c_red))
print("Площадь зеленого треугольника = ", S_triangle(p_green, a_green, b_green, c_green))
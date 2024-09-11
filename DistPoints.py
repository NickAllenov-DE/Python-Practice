import math

def DistPoints(Ax, Ay, Bx, By):
    ''' программа принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. '''

    distance = math.sqrt((Bx - Ax) ** 2 + (By - Ay) ** 2)

    print('Расстояние между точками = ', round(distance, roundrange))

Ax = int(input('Введите координату Х для точки А: '))
Ay = int(input('Введите координату Y для точки А: '))
Bx = int(input('Введите координату Х для точки B: '))
By = int(input('Введите координату Y для точки B: '))
roundrange = int(input('Выберите степень округления (знаков после запятой): '))

DistPoints(Ax, Ay, Bx, By)

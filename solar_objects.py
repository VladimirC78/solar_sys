# coding: utf-8
# license: GPLv3


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self, r, color, m, x, y, vx, vy):
        self.type = "star"
        self.m = m
        self.x = x
        self.y = y
        self.Vx = vx
        self.Vy = vy
        self.Fx = 0
        self.Fy = 0
        self.R = r
        self.color = color


class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """
    def __init__(self, r, color, m, x, y, vx, vy):

        self.type = "planet"
        self.m = m
        self.x = x
        self.y = y
        self.Vx = vx
        self.Vy = vy
        self.Fx = 0
        self.Fy = 0
        self.R = r
        self.color = color

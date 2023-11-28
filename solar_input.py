# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
from solar_vis import DrawableObject
import json


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """
    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем

            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return [DrawableObject(obj) for obj in objects]


def parse_star_parameters(line, star):
    splitted = line.split(' ')
    star.R = float(splitted[1])
    star.color = splitted[2]
    star.m = float(splitted[3])
    star.x = float(splitted[4])
    star.y = float(splitted[5])
    star.Vx = float(splitted[6])
    star.Vy = float(splitted[7])
    pass


def parse_planet_parameters(line, planet):
    splitted = line.split(' ')
    planet.R = float(splitted[1])
    planet.color = splitted[2]
    planet.m = float(splitted[3])
    planet.x = float(splitted[4])
    planet.y = float(splitted[5])
    planet.Vx = float(splitted[6])
    planet.Vy = float(splitted[7])
    pass


def write_space_objects_data_to_file(output_filename, space_objects):
    """Функция преобразует объекты в список словарей и записывает в файл"""
    with open(output_filename, "w") as output_file:
        object1=[{'type': obj.type,
                         'R': obj.R,
                         'color': obj.color,
                         'm': obj.m,
                         'x': obj.x,
                         'y': obj.y,
                         'v_x': obj.Vx,
                         'v_y': obj.Vy} for obj in space_objects]
        output_file.write(json.dumps(object1))


if __name__ == "__main__":
    print("This module is not for direct call!")


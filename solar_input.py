# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
from solar_vis import DrawableObject


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
                star = Star(parse_star_parameters(line))
                objects.append(star)
            elif object_type == "planet":
                planet = Planet(parse_planet_parameters(line))
                objects.append(planet)
            else:
                print("Unknown space object")

    return [DrawableObject(obj) for obj in objects]


def parse_star_parameters(line):
    splitted = line.split(' ')
    r = splitted[1]
    color = splitted[2]
    m = splitted[3]
    x = splitted[4]
    y = splitted[5]
    vx = splitted[6]
    vy = splitted[7]
    return r, color, m, x, y, vx, vy


def parse_planet_parameters(line):
    splitted = line.split(' ')
    r = splitted[1]
    color = splitted[2]
    m = splitted[3]
    x = splitted[4]
    y = splitted[5]
    vx = splitted[6]
    vy = splitted[7]
    return r, color, m, x, y, vx, vy


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.

    Строки должны иметь следующий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла

    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            # FIXME!


if __name__ == "__main__":
    print("This module is not for direct call!")


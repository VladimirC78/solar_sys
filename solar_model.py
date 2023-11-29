# coding: utf-8
# license: GPLv3
import math

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj or not obj.alive:
            continue
        r = ((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2) ** 0.5
        body.Fx += -gravitational_constant * body.m * obj.m / r ** 3 * (body.x - obj.x)
        body.Fy += -gravitational_constant * body.m * obj.m / r ** 3 * (body.y - obj.y)

        # FIXME: обработка аномалий при прохождении одного тела сквозь другое


def move_space_object(body, dt):
    ax = body.Fx/body.m
    ay = body.Fy/body.m
    body.x += body.Vx * dt + ax * dt ** 2 / 2
    body.Vx += ax * dt
    body.y += body.Vy * dt + ay * dt ** 2 / 2
    body.Vy += ay * dt


def RK4(space_objects, dt):
    k1 = space_objects
    for body in k1:
        calculate_force(body, space_objects)
    for body in k1:
        move_space_object(body, dt)
    k2 = space_objects
    for body in k2:
        calculate_force(body, k1)
    for body in k2:
        move_space_object(body, dt/2)
    k3 = space_objects
    for body in k3:
        calculate_force(body, k2)
    for body in k3:
        move_space_object(body, dt/2)
    for i in range(len(space_objects)):
        space_objects[i].x += dt/6 * (space_objects[i].Vx + 2 * k1[i].Vx + 2 * k2[i].Vx + k3[i].Vx)
        space_objects[i].y += dt/6 * (space_objects[i].Vy + 2 * k1[i].Vy + 2 * k2[i].Vy + k3[i].Vy)
        space_objects[i].Vx += dt/6 * (space_objects[i].Fx/space_objects[i].m + 2 * k1[i].Fx/k1[i].m + 2 * k2[i].Fx/k2[i].m + k3[i].Fx/k3[i].m)
        space_objects[i].Vy += dt/6 * (space_objects[i].Fy/space_objects[i].m + 2 * k1[i].Fy/k1[i].m + 2 * k2[i].Fy/k2[i].m + k3[i].Fy/k3[i].m)


def recalculate_space_objects_positions(space_objects, dt):
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)

    #RK4(space_objects, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")

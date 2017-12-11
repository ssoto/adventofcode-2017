#!/usr/bin/env python


def new_coordinates(x, y, movement):
    if movement == 'n':
        return x, y-1
    elif movement == 'ne':
        return x + 1, y - 1
    elif movement == 'se':
        return x + 1, y
    elif movement == 's':
        return x, y + 1
    elif movement == 'sw':
        return x - 1, y + 1
    elif movement == 'nw':
        return x - 1, y


def distance_in_grid(a, b, x, y):
    return (abs(a - x)
            + abs(a + b - x - y)
            + abs(b - y)) / 2


def count_movements(movements):
    a = b = 0
    x = a
    y = b
    max_distance = -10000000
    distance = 0
    for m in movements:
        x, y = new_coordinates(x, y, m)
        distance = distance_in_grid(a, b, x, y)
        if distance > max_distance:
            max_distance = distance

    print('Max_distance is {}'.format(max_distance))

    return distance_in_grid(a, b, x, y)


if __name__ == '__main__':
    with open('./input.txt', 'r') as fd:
        content = fd.read().strip().split(',')

    distance = count_movements(content)
    print('Distance is {}'.format(distance))

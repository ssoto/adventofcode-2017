#!/usr/bin/env python


def sublist_reverse(start_rev, size, orig_lst):
    lst = orig_lst.copy()
    reversed = [
        lst[i % len(orig_lst)]
        for i in range(start_rev, start_rev+size)
    ]
    reversed.reverse()

    for i, element in enumerate(reversed, start_rev):
        lst[i % len(orig_lst)] = element

    return lst


def solve(values, lengths):
    position = 0
    skip_size = 0
    for length in lengths:
        values = sublist_reverse(position, length, values)
        new_position = (position + skip_size + length) % len(values)
        if new_position <= len(values):
            position = new_position
        skip_size += 1

    return values


if __name__ == '__main__':
    with open('./input.txt', 'r') as fd:
        lengths = [int(element) for element in fd.read().strip().split(',')]
    values = list(range(256))

    values = solve(values, lengths)

    print('Result is {} X {} = {}'.format(
        values[0], values[1], values[0]*values[1],
    ))

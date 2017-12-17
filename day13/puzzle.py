import itertools


def scanner(height, time):
    offset = time % ((height - 1) * 2)

    return (
        2 * (height - 1) - offset
        if offset > height - 1 else offset
    )


if __name__ == '__main__':

    with open('./input.txt', 'r') as fd:
        lines = [line.split(': ')
                 for line in fd.readlines()]

    heights = {
        int(pos): int(height) for pos, height in lines
    }

    solution = sum(
        pos * heights[pos]
        for pos in heights if scanner(heights[pos], pos) == 0
    )
    print('Part 1 solution: {}'.format(solution))

    solution = next(
        wait
        for wait in itertools.count()
        if not any(scanner(heights[pos], wait + pos) == 0 for pos in heights))
    print('Part 2 solution: {}'.format(solution))

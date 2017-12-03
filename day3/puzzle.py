#!/usr/bin/env python
import os


class Challenge(object):

    def __init__(self, input_value):
        self.number = input_value

    def x_steps(self, values, i):
        size = values[i] - values[i-1]
        elements = [
            values[i-1] + (i - 1) * 1,
            values[i-1] + (i - 1) * 3,
            values[i-1] + (i - 1) * 5,
            values[i-1] + (i - 1) * 7,
        ]
        result = sorted(
            [abs(self.number - i) for i in elements]
        )
        return result[0]

    def solve(self):
        i = 0
        steps = [0, ]
        while True:
            i += 1
            if i == 1:
                value = 1
            else:
                value = steps[i-1] + (i - 1) * 8
            steps.append(value)
            if steps[-1] >= self.number:
                break
        x_steps = self.x_steps(steps, i)
        print('For {} are {} circle + {} steps: {}'.format(
            self.number,
            i-1,
            x_steps,
            i -1 + x_steps,
        ))
        return i - 1 + x_steps


if __name__ == '__main__':

    for i in [12, 23, 39, 1024, 289326, ]:
        print('Solution of {} -> {}'.format(i, Challenge(i).solve()))


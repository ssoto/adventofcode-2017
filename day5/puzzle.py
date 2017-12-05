#!/usr/bin/env python


class Puzzle(object):

    def __init__(self, input):
        self.input = input

    def solve(self):
        i = 0
        idx = 0
        while True:
            try:
                step = self.input[idx]
            except IndexError:
                return idx
            self.input[idx] += i
            i += 1
            idx = step

    def solve_second(self):
        idx = 0
        while True:
            try:
                offset = self.input[idx]
                if offset >= 3:
                    i = -1
                else:
                    i = 1
            except IndexError:
                return idx
            self.input[idx] += i
            i += 1
            idx = offset


if __name__ == '__main__':
    print('-------------------')
    with open('./input.txt', 'r') as fd:
        raw_input = fd.readlines()

    input_steps = [int(step.strip()) for step in raw_input]

    problem = Puzzle(input_steps)
    solution1 = problem.solve()
    print('First soultion: {}'.format(solution1))
    solution2 = problem.solve_second()
    print('First soultion: {}'.format(solution2))

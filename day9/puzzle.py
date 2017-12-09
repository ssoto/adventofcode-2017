#!/usr/env/bin python

import sys
sys.setrecursionlimit(100000)

class Puzzle(object):

    @staticmethod
    def clear_input(stream):
        cleared_input = ''
        garbage_mode = False
        ignored = False
        for char in stream:
            if ignored:
                ignored = False
                continue

            if char == '<':
                garbage_mode = True
            elif char == '>':
                garbage_mode = False
            elif char == '!':
                ignored = True
            elif not garbage_mode:
                cleared_input += char
        return cleared_input

    @staticmethod
    def groups(stream):
        groups = 0
        for char in stream:
            if char == '{':
                groups += 1

        return groups

    @staticmethod
    def groups_score(stream, level=1):
        groups_size = Puzzle.groups(stream)
        if groups_size == 1:
            result = level
        else:
            groups = stream[1:-1].split(',')
            result = level + sum([
                Puzzle.groups_score(group, level=level+1)
                for group in groups])
        return result

    @staticmethod
    def score(stream):
        return Puzzle.groups_score(stream)


def simple_solution():
    nesting_score = 0
    curr_nesting = 0
    in_garbage = False
    garbage_count = 0
    with open('input.txt') as f:
        while True:
            char = f.read(1)
            if not char:
                print("total nesting score: ", nesting_score, " GarbageCount: ",
                      garbage_count)
                break
            if char == '!' and in_garbage:
                f.read(1)
            elif char == '<':
                if in_garbage: garbage_count += 1
                in_garbage = True
            elif char == '>':
                in_garbage = False
            elif char == '{' and not in_garbage:
                curr_nesting += 1
                nesting_score += curr_nesting
            elif char == '}' and not in_garbage:
                curr_nesting -= 1
            elif in_garbage:
                garbage_count += 1


def recursive_solution():
    with open('input.txt') as fd:
        content = fd.read()

    puzzle = Puzzle()
    cleared_stream = puzzle.clear_input(content)
    score = puzzle.score(cleared_stream)
    print('Score of input is {}'.format(score))


if __name__ == '__main__':
    simple_solution()

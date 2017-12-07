#!/usr/bin/env python
import itertools


class Puzzle(object):

    def __init__(self, input):
        self.blocks = input

    def redistribute_blocks(self):
        states = [self.current_state(), ]

        for iteration in itertools.count():
            print('Status {}: {}'.format(
                iteration+1, self.blocks))
            max_block = max(self.blocks)
            max_block_index = self.blocks.index(max_block)
            self.blocks[max_block_index] = 0

            for i in range(1, max_block+1):
                # print('Reindex {}: {}'.format( i, self.blocks ))
                self.blocks[(max_block_index + i) % len(self.blocks)] += 1

            current_state = self.current_state()
            if current_state in states:
                # first solution return iteration+1

                # now second one
                index_of_state = states.index(current_state)
                return iteration - index_of_state + 1
            else:
                states.append(self.current_state())

    def current_state(self):
        return ','.join([str(block) for block in self.blocks])


if __name__ == '__main__':
    with open('./input.txt') as fd:
        content = fd.read().strip()

    blocks = [int(element) for element in content.split('\t')]

    puzzle = Puzzle(blocks)
    last_iteration = puzzle.redistribute_blocks()
    print('Stop in iteration {}'.format(last_iteration))
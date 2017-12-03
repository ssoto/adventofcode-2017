#!/usr/bin/env python
import os


class Challenge(object):

    def __init__(self, chain):
        self.chain = chain

    def inverse_captcha(self):
        return sum([
            int(self.chain[i])
            for i in range(len(self.chain)) if self.check(i)
        ])

    def check(self, i):
        result = 0
        current_index = i % len(self.chain)
        next_index = (i + 1) % len(self.chain)

        if self.chain[current_index] == self.chain[next_index]:
            result = int(self.chain[current_index])

        return result

    def inverse_captcha_second_issue(self):
        return sum([
            int(self.chain[i])
            for i in range(len(self.chain)) if self.check_second_issue(i)
        ])

    def check_second_issue(self, i):
        current_index = i
        next_index = int(
            (i + (len(self.chain) / 2)) % len(self.chain)
        )

        if self.chain[current_index] == self.chain[next_index]:
            return int(self.chain[current_index])

        return 0


if __name__ == '__main__':
    path = None
    while True:
        path_inserted = input('Insert path of file input: ')
        if os.path.exists(path_inserted):
            path = path_inserted
            break

    with open(path, 'r') as fd:
        content = fd.read()

    number_chain = int(content)
    print('Number to manage: {}'.format(number_chain))

    challenge = Challenge(content)
    solve = challenge.inverse_captcha()
    print('Captcha is {}'.format(solve))

    second_solve = challenge.inverse_captcha_second_issue()
    print('Second captcha is {}'.format(second_solve))

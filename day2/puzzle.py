#!/usr/bin/env python
import os


class Challenge(object):

    def __init__(self, chain):
        spreadsheet = []
        for row_chain in chain.split('\n'):
            spreadsheet.append([
                int(item)
                for item in row_chain.split('\t')
            ])
        self.spreadsheet = spreadsheet

    def check_sum(self, row):
        sorted_row = sorted(row, reverse=True)

        largest = sorted_row[0]
        smallest = sorted_row[len(sorted_row) - 1]

        return largest - smallest

    def solve(self):
        return sum([
            self.check_sum(row)
            for row in self.spreadsheet
        ])

    def divisible_values(self, row):
        for i in range(len(row)):
            for j in range(i + 1, len(row)):
                if row[i] % row[j] == 0:
                    return row[i] / row[j]
                elif row[j] % row[i] == 0:
                    return row[j] / row[i]
        return 0

    def second_issue_solve(self):
        rows_sums = [
            self.divisible_values(row)
            for row in self.spreadsheet
        ]
        print(rows_sums)
        return sum(rows_sums)


if __name__ == '__main__':
    path = None
    while True:
        # path_inserted = input('Insert path of file input: ')
        path_inserted = 'input.txt'
        if os.path.exists(path_inserted):
            path = path_inserted
            break

    with open(path, 'r') as fd:
        content = fd.read()

    challenge = Challenge(content)

    print('Checksum is {}'.format(challenge.solve()))
    print('Second checksum is {}'.format(challenge.second_issue_solve()))

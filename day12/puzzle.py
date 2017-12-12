#!/usr/bin/env python


def process_programs(programs):

    return programs


if __name__ == '__main__':
    with open('./input.txt', 'r') as fd:
        content = fd.readlines()

    def build_program(line):
        id, programs = line.strip().split('<->')
        programs = [int(p) for p in programs.strip().split(',')]
        return (id, programs)

    programs = dict()
    for line in content:
        id, p = build_program(line)
        programs[id] = p

    programs_completed = process_programs(programs)

    result = [k for k, v in programs_completed.items() if 0 in v]
    print('There are {} programs of 0'.format(len(result)))
#!/usr/bin/env python


def process_programs(programs):
    pass


if __name__ == '__main__':
    with open('./input.txt', 'r') as fd:
        content = fd.readlines()

    def build_program(line):
        id, programs = line.split('<->')
        programs = [int(p) for p in programs.strip().split(',')]
        return {
            'id': int(id),
            'programs': programs
        }

    programs = [
        build_program(program)
        for program in content
    ]
    print(programs[0])
    processed = process_programs(programs)

    result = sum([
        program
        for program in programs
        if 0 in program['programs']
    ])
    print('There are {} programs of 0'.format(result))
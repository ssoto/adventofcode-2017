#!/usr/bin/env python

def process_programs(programs):
    result = {}
    for prog, related in programs.items():
        for prog_related in related:
            new_related = set(related).union(set(programs[prog_related]))
            result[prog] = new_related
    return result


if __name__ == '__main__':
    with open('./input.txt', 'r') as fd:
        content = fd.readlines()

    def build_program(line):
        id, programs = line.strip().split('<->')
        id = int(id)
        programs = set([int(p) for p in programs.strip().split(',')])
        return (id, programs)

    programs = dict()
    for line in content:
        id, p = build_program(line)
        programs[id] = p

    programs_completed = process_programs(programs)

    result = [k for k, v in programs_completed.items() if 0 in v]
    print('There are {} programs of 0'.format(len(result)))
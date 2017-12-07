#!/usr/bin/env python


class ProgramssTree(object):

    def __init__(self, name, number, children=[]):
        self.name = name
        self.number = number
        self.children = children

    def add_children(self, element):
        self.children.append(element)


class Puzzle(object):

    def __init__(self):
        self.input = input

    @classmethod
    def build_data_structure(cls, content):
        result = dict()
        for line in content:
            splited_line = line.split('->')

            if len(splited_line) == 2:
                data, children = splited_line
            else:
                data = splited_line[0]
                children = []
            program_name, program_number = data.strip().split(' ')
            program_number = program_number[1:-1]

            if children:
                children_names = list(
                    name.strip() for name in children.split(','))
            else:
                children_names = []
            program_data = {
                'program_name': program_name,
                'program_number': program_number,
                'children_names':  children_names,
            }
            result[program_data['program_name']] = program_data
        return result


if __name__ == '__main__':

    print('-------------------')
    with open('./input.txt', 'r') as fd:
        raw_input = fd.readlines()

    content = Puzzle().build_data_structure(raw_input)
    print(len(content))

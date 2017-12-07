#!/usr/bin/env python


class ProgramsNode(object):

    def __init__(self, name, number, children=[]):
        self.name = name
        self.number = number
        self.children = children
        self.is_child_of = []

    def children(self):
        return len(self.children)

    def replace_name_by_element(self, element):
        index = self.children.index(element.name)
        element.is_child_of.append(self)
        self.children[index] = element

    def __str__(self):
        return '{} ({}) - {}'.format(
            self.name,
            self.number,
            [o.name for o in self.children]
        )


class Puzzle(object):

    def __init__(self):
        self.input = input

    @classmethod
    def build_nodes(cls, content):
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

    @staticmethod
    def build_tree(nodes):
        node_elements = {}
        for data_node in nodes.values():
            node = ProgramsNode(name=data_node['program_name'],
                                number=data_node['program_number'],
                                children=data_node['children_names'], )
            node_elements[node.name] = node

        for node_element in node_elements.values():
            for children_name in node_element.children:
                children = node_elements.get(children_name)
                node_element.replace_name_by_element(children)
        return node_elements.values()


if __name__ == '__main__':

    print('-------------------')
    with open('./input.txt', 'r') as fd:
        raw_input = fd.readlines()

    nodes_list = Puzzle().build_nodes(raw_input)
    nodes_tree = Puzzle().build_tree(nodes_list)
    no_childrens = [node for node in nodes_tree if not len(node.is_child_of)]
    print([n.name for n in no_childrens])

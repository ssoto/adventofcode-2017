#!/usr/bin/env python


class ProgramsNode(object):

    def __init__(self, name, weight, children=[]):
        self.name = name
        self.weight = weight
        self.children = children
        self.parents = []

    def get_number_of_children(self):
        return len(self.children)

    def get_children_tower_size(self):
        return [children.tower_size() for children in self.children]

    def replace_name_by_element(self, element):
        index = self.children.index(element.name)
        element.parents.append(self)
        self.children[index] = element

    def tower_size(self):
        return self.weight + sum([
            node.tower_size() for node in self.children
        ])

    def __str__(self):
        return '{} ({}) - {}'.format(
            self.name,
            self.weight,
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
            program_name, program_weight= data.strip().split(' ')
            program_weight = int(program_weight[1:-1])

            if children:
                children_names = list(
                    name.strip() for name in children.split(','))
            else:
                children_names = []
            program_data = {
                'program_name': program_name,
                'program_weight': program_weight,
                'children_names':  children_names,
            }
            result[program_data['program_name']] = program_data
        return result

    @staticmethod
    def build_tree(nodes):
        node_elements = {}
        for data_node in nodes.values():
            node = ProgramsNode(name=data_node['program_name'],
                                weight=data_node['program_weight'],
                                children=data_node['children_names'], )
            node_elements[node.name] = node

        for node_element in node_elements.values():
            for children_name in node_element.children:
                children = node_elements.get(children_name)
                node_element.replace_name_by_element(children)
        return list(node_elements.values())


if __name__ == '__main__':

    print('-------------------')
    with open('./input.txt', 'r') as fd:
        raw_input = fd.readlines()

    nodes_list = Puzzle().build_nodes(raw_input)
    nodes_tree = Puzzle().build_tree(nodes_list)
    parent_nodes = [node for node in nodes_tree if not len(node.parents)]
    if parent_nodes:
        parent = parent_nodes[0]

    print(parent.weight)

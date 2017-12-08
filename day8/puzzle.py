#!/usr/bin/env python
import collections
import operator


class Command(object):

    def __init__(self, register, operation, value, condition_register,
                 condition_operator, condition_value):
        self.register = register
        self.operation = self.build_operation(operation)
        self.value = value
        self.condition_register = condition_register
        self.condition_operator = self.build_logic_operation(condition_operator)
        self.condition_value = int(condition_value)

    @staticmethod
    def build_logic_operation(operation):
        if operation == '<':
            return operator.lt
        elif operation == '<=':
            return operator.le
        elif operation == '==':
            return operator.eq
        elif operation == '>=':
            return operator.ge
        elif operation == '>':
            return operator.gt
        elif operation == '!=':
            return operator.ne

    @staticmethod
    def build_operation(operator):
        if operator == 'inc':
            return lambda x, y: x + y
        else:
            return lambda x, y:  x - y

    @staticmethod
    def build_commands(content):
        '''Will receive a string line like:
            pnt dec 503 if vk == 8

        :param content:
        :return:
        '''
        splited = content.strip().split(' ')

        register = splited[0]
        operation = splited[1]
        value = int(splited[2])
        condition_register = splited[4]
        condition_operator = splited[5]
        condition_value = int(splited[6])
        return Command(
            register=register,
            operation=operation,
            value=value,
            condition_register=condition_register,
            condition_operator=condition_operator,
            condition_value=condition_value,
        )


if __name__ == '__main__':

    print('-------------------')
    with open('./input.txt', 'r') as fd:
        content = fd.readlines()

    commands = [
        Command.build_commands(line)
        for line in content
    ]

    registers = dict()
    max_value = -10000000

    for command in commands:
        destiny_register = command.register
        condition_register_content = registers.get(command.condition_register, 0)
        if command.condition_operator(condition_register_content, command.condition_value):  # noqa
            current_value = registers.get(destiny_register, 0)
            new_value = command.operation(
                current_value, command.value
            )
            registers[destiny_register] = new_value

        current_max = sorted(registers.values(), reverse=True)
        if current_max and current_max[0] > max_value:
            max_value = current_max[0]

    print('Highest value is: {}'.format(
        sorted(registers.values(), reverse=True)[0]))
    print('Highest value during operations is: {}'.format(max_value))

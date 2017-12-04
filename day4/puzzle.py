

def is_valid_line(line):
    return len(line) == len(set(line))


if __name__ == '__main__':

    with open('./input.txt', 'r') as fd:
        lines = fd.readlines()

    content_words = [
        line.strip().split(' ')
        for line in lines
    ]

    valid_first_words = [
        is_valid_line(line) for line in content_words
    ]
    print('First passphrase: {}'.format(sum(valid_first_words)))

    second_validation = 0
    for line in content_words:
        is_valid = is_valid_line([
            ''.join(sorted(word))
            for word in line
        ])
        second_validation += is_valid
    print('Second passphrase: {}'.format(second_validation))

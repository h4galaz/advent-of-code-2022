import os
import re

from tabulate import tabulate


def main(file_path: str):

    crates_matrix = []
    move_instructions = []
    pattern = re.compile('[\W_]+')

    with open(file_path, 'r') as input:
        for line in input:
            line = line.rstrip('\n')

            if not 'move' in line and not '[' in line:
                continue

            if 'move' in line:
                move_instructions.append(line)
                continue

            for index, crate in enumerate(re.split('\s{1,4}', line)):
                crate = pattern.sub('', crate)
                if len(crates_matrix) <= index:
                    crates_matrix.insert(index, crate)
                else:
                    crates_matrix[index] = crate + crates_matrix[index]

    crates_matrix_2 = crates_matrix.copy()
    part_1 = "".join([crates[-1:]
                     for crates in move_crate(crates_matrix, move_instructions)])
    part_2 = "".join(
        [crates[-1:] for crates in move_crate(crates_matrix_2, move_instructions, True)])

    os.system('clear')
    print(tabulate([[part_1, part_2]], headers=['PART 1', 'PART 2']))


def move_crate(matrix: list, move_instructions: list, cratemover_9001: bool = False) -> list:
    for instruction in move_instructions:
        num_of_crates, source, destination = [int(digit)
                                              for digit in re.findall('\d+', instruction)]

        if cratemover_9001:
            matrix[destination - 1] = matrix[destination - 1] + \
                matrix[source - 1][-num_of_crates:]
        else:
            matrix[destination - 1] = matrix[destination - 1] + \
                matrix[source - 1][-num_of_crates:][::-1]
        matrix[source - 1] = matrix[source - 1][:-num_of_crates]
    return matrix


if __name__ == '__main__':
    # main('5-Supply-Stacks/demo-input.txt')
    main('5-Supply-Stacks/challenge-input.txt')

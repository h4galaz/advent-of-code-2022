import os
import string
from itertools import islice

from tabulate import tabulate


def main(file_path: str):
    priority = []
    group_priority = []
    with open(file_path, 'r') as input:
        while True:
            lines_group = list(islice(input, 3))

            if not lines_group:
                break

            group = list(set.intersection(*[set(line.rstrip('\n'))
                                            for line in lines_group]))[0]
            group_priority.append(get_priority(group))
            print(group)

            for rucksack in lines_group:
                rucksack = rucksack.rstrip('\n')

                comp_1, comp_2 = rucksack[0:len(
                    rucksack)//2], rucksack[len(rucksack)//2:]
                # intersection finds matches in set
                _match = list(set(comp_1).intersection(comp_2))[0]
                priority.append(get_priority(_match))

    part_1 = sum(priority)
    part_2 = sum(group_priority)

    os.system('clear')
    print(tabulate([[part_1, part_2]], headers=['PART 1', 'PART 2']))


def get_priority(letter: str) -> int:
    return string.ascii_letters.index(letter) + 1


if __name__ == '__main__':
    # main('3-Rucksack-Reorganization/demo-input.txt')
    main('3-Rucksack-Reorganization/challenge-input.txt')

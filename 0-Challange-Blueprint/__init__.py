import os

from tabulate import tabulate


def main(file_path: str):
    with open(file_path, 'r') as input:
        for line in input:
            print(line)

    part_1 = 0
    part_2 = 0

    os.system('clear')
    print(tabulate([[part_1, part_2]], headers=['PART 1', 'PART 2']))


if __name__ == '__main__':
    main('[challange-name]/demo-input.txt')
    # main('[challange-name]/challenge-input.txt')

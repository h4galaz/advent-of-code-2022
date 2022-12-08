import os
from collections import defaultdict

from tabulate import tabulate


def main(file_path: str):
    sizes = defaultdict(int)
    history = ["/"]
    with open(file_path, 'r') as input:
        for line in input:
            if line.startswith('$ cd'):
                folder = line.split()[-1]
                if folder == '/':
                    continue
                elif '..' not in line:
                    history.append("/".join(history+[folder]).lstrip('/'))
                else:
                    history = history[:-1]

            if line[0].isdigit():
                for k in history:
                    sizes[k] += int(line.split()[0])

    part_1 = sum(filter(lambda x: x <= 100000, sizes.values()))
    part_2 = min(filter(lambda x: x >= 30000000 -
                 (70000000 - sizes['/']), sizes.values()))

    os.system('clear')
    print(tabulate([[part_1, part_2]], headers=['PART 1', 'PART 2']))


if __name__ == '__main__':
    # main('7-No-Space-Left-On-Device/demo-input.txt')
    main('7-No-Space-Left-On-Device/challenge-input.txt')

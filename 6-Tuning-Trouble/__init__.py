import os

from tabulate import tabulate


def main(file_path: str):
    with open(file_path, 'r') as input:
        line = input.read().rstrip('\n')

    part_1 = find_set_of_n(line, 4)
    part_2 = find_set_of_n(line, 14)

    os.system('clear')
    print(tabulate([[part_1, part_2]], headers=['PART 1', 'PART 2']))


def find_set_of_n(text: str, steps: int) -> str:
    return text.index([text[i:i+steps] for i in range(0, len(text)) if len(set(text[i:i+steps])) == steps][0]) + steps


if __name__ == '__main__':
    # main('6-Tuning-Trouble/demo-input.txt')
    main('6-Tuning-Trouble/challenge-input.txt')

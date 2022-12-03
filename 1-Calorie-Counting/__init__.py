import os

from tabulate import tabulate


def main(file_path: str):
    with open(file_path, 'r') as input:
        all_count = []
        count = 0
        for line in input:
            try:
                count += int(line)
            except ValueError:
                all_count.append(count)
                count = 0
    all_count.sort(reverse=True)

    part_1 = all_count[0]
    part_2 = sum(all_count[:3])

    os.system('clear')
    print(tabulate([[part_1, part_2]], headers=['PART 1', 'PART 2']))


if __name__ == '__main__':
    main('1-Calorie-Counting/challenge-input.txt')

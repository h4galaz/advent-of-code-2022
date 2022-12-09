import os
from functools import reduce
from math import prod

from tabulate import tabulate


def main(file_path: str):

    with open(file_path, 'r') as input:
        line = input.read().rstrip('\n').split('\n')
        tree_map = [[int(c) for c in x] for x in line]

    part_1 = 0
    part_2 = 0

    for row_i, row in enumerate(tree_map):
        for col_i, tree in enumerate(row):
            if col_i in [0, len(row) - 1] or row_i in [0, len(tree_map) - 1] or all(x < tree for x in row[col_i+1:]) or all(x < tree for x in row[:col_i]) or all(x[col_i] < tree for x in tree_map[row_i+1:]) or all(x[col_i] < tree for x in tree_map[:row_i]):
                part_1 += 1

            up = [x[col_i] for x in tree_map[:row_i]][::-1]
            right = row[col_i+1:]
            left = row[:col_i][::-1]
            down = [x[col_i] for x in tree_map[row_i+1:]]

            sol = prod([
                next((u_i for u_i, u in enumerate(
                    up, 1) if u >= tree), len(up)),
                next((r_i for r_i, r in enumerate(
                    right, 1) if r >= tree), len(right)),
                next((l_i for l_i, l in enumerate(left, 1)
                     if l >= tree), len(left)),
                next((d_i for d_i, d in enumerate(down, 1)
                     if d >= tree), len(down)),
            ])
            if sol > part_2:
                part_2 = sol

    os.system('clear')
    print(tabulate([[part_1, part_2]], headers=['PART 1', 'PART 2']))


def get_reach(trees_in_view: list, own_height: int) -> int:
    try:
        return trees_in_view.index(max(min([x for x in trees_in_view if x >= own_height]), own_height)) + 1
    except ValueError:
        return len(trees_in_view)


if __name__ == '__main__':
    # main('8-Treetop-Tree-House/demo-input.txt')
    main('8-Treetop-Tree-House/challenge-input.txt')

import os
import re

from tabulate import tabulate


def main(file_path: str):
    part_1 = 0
    part_2 = ''
    x = 1
    cycle = 0
    add = 0
    with open(file_path, 'r') as input:
        inst = input.readline()
        while inst != '':

            part_2 += draw_crt(x, cycle)
            cycle += 1
            if cycle in range(20, 240, 40):
                sum_cycle = cycle * x
                part_1 += sum_cycle

            if inst.startswith('noop'):
                inst = input.readline()
            elif inst.startswith('addx') and add == 0:
                add = int(inst.split()[1])
            elif inst.startswith('addx') and add != 0:
                x += add
                add = 0
                inst = input.readline()

    part_2 = "\n".join(re.findall(r'.{40}', part_2))

    os.system('clear')
    print(tabulate([[part_1, part_2]], headers=['PART 1', 'PART 2']))


def draw_crt(sprite_pos: int, pixel_pos: int) -> str:
    return '#' if sprite_pos - 1 <= pixel_pos % 40 <= sprite_pos + 1 else '.'


if __name__ == '__main__':
    # main('10-Cathode-Ray-Tube/demo-input.txt')
    main('10-Cathode-Ray-Tube/challenge-input.txt')

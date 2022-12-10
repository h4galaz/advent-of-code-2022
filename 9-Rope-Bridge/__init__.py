import os
import time

from tabulate import tabulate


def main(file_path: str):
    with open(file_path, 'r') as input:
        knots_1 = [[11, 5] for _ in range(2)]
        history_1 = set()
        history_1.add((0, 0))

        knots_2 = [[11, 5] for _ in range(10)]
        history_2 = set()
        history_2.add((0, 0))
        for line in input:
            line = line.rstrip('\n').split()
            direction = line[0]
            steps = int(line[1])
            history_1.update(simulate(knots_1, direction, steps))
            history_2.update(simulate(knots_2, direction, steps))

    part_1 = len(history_1)  # 6391
    part_2 = len(history_2)

    os.system('clear')
    print(tabulate([[part_1, part_2]], headers=['PART 1', 'PART 2']))


def simulate(entities: list, direction: str, distance: int, animate: bool = False) -> set:
    return_set = set()
    i = 1
    if direction in ['L', 'D']:
        i *= -1
    for _ in range(0, distance):
        a = int(direction in ['R', 'L'])
        entities[0][int(not a)] += i
        for index, knot in enumerate(entities[1:]):
            x_dis = entities[index][int(not a)] - knot[int(not a)]
            y_dis = entities[index][a] - knot[a]

            if (abs(x_dis) == 2) and (abs(y_dis) == 2):
                knot[int(not a)] += x_dis // 2
                knot[a] += y_dis // 2
            else:
                if abs(x_dis) == 2:
                    knot[int(not a)] += x_dis // 2
                    knot[a] = entities[index][a]
                elif abs(y_dis) == 2:
                    knot[a] += y_dis // 2
                    knot[int(not a)] = entities[index][int(not a)]
            if animate:
                paint(direction, distance, entities)
                print(index + 1, knot, entities[index], x_dis,
                      y_dis)
        return_set.add(tuple(entities[-1]))

    return return_set


def paint(direction: str, distance: int, entities: list, speed: int = 10) -> None:
    control = [['.' for _ in range(0, 26)] for _ in range(0, 21)]

    os.system('clear')
    print(f'== {direction} {distance} ==')
    for index, entity in enumerate(entities):
        control[::-1][entity[1]][entity[0]] = 'H' if index == 0 else str(index)

    print(''.join([''.join(x) + '\n' for x in control]))
    time.sleep(0.05 / speed)


if __name__ == '__main__':
    # main('9-Rope-Bridge/demo-input.txt')
    main('9-Rope-Bridge/challenge-input.txt')

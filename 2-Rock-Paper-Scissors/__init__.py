import os
from collections import deque

from tabulate import tabulate

SCORING = [
    (['A', 'Z'], 'X', 'Rock beats scissors'),
    (['B', 'X'], 'Y', 'Paper beats rock'),
    (['C', 'Y'], 'Z', 'Scissors beats paper'),
]


def main(file_path: str):
    round_scores = [[], []]
    with open(file_path, 'r') as input:
        for round in input:
            round_scores[0].append(get_points(round.rstrip('\n').split(' ')))
            round_scores[1].append(get_points_part_2(
                round.rstrip('\n').split(' ')))

    part_1 = sum(round_scores[0])
    part_2 = sum(round_scores[1])

    os.system('clear')
    print(tabulate([[part_1, part_2]], headers=['PART 1', 'PART 2']))


def get_points(round_result: list) -> int:
    # Weapon of choice points
    round_score = [score[1] for score in SCORING].index(round_result[1]) + 1
    if chr(ord(round_result[0]) + 23) == round_result[1]:
        # Draw!
        return round_score + 3
    if not any(round_result in score for score in SCORING):
        # You win!
        return round_score + 6
    # You lose!
    return round_score


def get_points_part_2(round_result: list) -> int:
    # Weapon of choice points
    weapons = deque([score[0][0] for score in SCORING])
    # rotate list to match draw, win, lose state
    weapons.rotate((ord(round_result[1]) - 88) - 1)

    round_score = [score
                   for score in weapons].index(round_result[0]) + 1

    win_draw_lose = ord(round_result[1]) - 88
    round_status_score = win_draw_lose * 3

    # Points based on win (Z), draw (Y) or lose (X)
    return round_score + round_status_score


if __name__ == '__main__':
    # main('2-Rock-Paper-Scissors/demo-input.txt')
    main('2-Rock-Paper-Scissors/challenge-input.txt')

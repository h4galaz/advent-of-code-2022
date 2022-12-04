import os

from tabulate import tabulate


def main(file_path: str):
    contain_count = 0
    overlap_count = 0
    with open(file_path, 'r') as input:
        for teams in input:
            teams = teams.rstrip('\n')
            team_range = [t.split('-') for t in teams.split(',')]

            team1 = range(int(team_range[0][0]), int(team_range[0][1]) + 1)
            team2 = range(int(team_range[1][0]), int(team_range[1][1]) + 1)

            if (team1.start in team2 and team1[-1] in team2) or (team2.start in team1 and team2[-1] in team1):
                contain_count += 1

            if (team1.start in team2 or team1[-1] in team2) or (team2.start in team1 or team2[-1] in team1):
                overlap_count += 1

    part_1 = contain_count
    part_2 = overlap_count

    os.system('clear')
    print(tabulate([[part_1, part_2]], headers=['PART 1', 'PART 2']))


if __name__ == '__main__':
    # main('4-Camp-Cleanup/demo-input.txt')
    main('4-Camp-Cleanup/challenge-input.txt')

import json
import os
from datetime import datetime
from typing import List, Optional

import requests
from dotenv import load_dotenv
from pydantic import BaseModel, parse_obj_as, validator
from tabulate import tabulate

SORT_BY = 'local_score'
DESC = True
UDPATE_FREQ = 1800
LOCAL_LEADERBOARD = 'demo-leaderboard.json'


def main():
    os.system('clear')
    last_update = os.path.getmtime(LOCAL_LEADERBOARD)
    time_diff = (datetime.now(
    ) - datetime.fromtimestamp(last_update)).total_seconds()

    if os.stat(LOCAL_LEADERBOARD).st_size == 0 or time_diff >= UDPATE_FREQ:
        update_leaderboard()

    with open(LOCAL_LEADERBOARD) as leader_file:
        leader_dict = json.load(leader_file)['members']

    players = parse_obj_as(List[PlayerModel], [
        leader_dict[leader] for leader in leader_dict])

    sort_and_output(players, desc=DESC, sort_by=SORT_BY)


def sort_and_output(data: list, desc: bool = False, sort_by: str = 'local_score'):
    data.sort(key=lambda x: getattr(x, sort_by), reverse=desc)
    print(f"[{datetime.fromtimestamp(os.path.getmtime(LOCAL_LEADERBOARD)).strftime('%d.%m.%Y, %H:%M')}]\n\n")
    print(tabulate([list(item.dict().values()) for item in data], headers=[
        'Name', 'AOC Score', 'Local Score', 'Last Star Obtained', 'Stars', 'Completion Days'], tablefmt='github'))


def update_leaderboard():
    cookies = {'session': os.environ.get('AOC-SESSION-TOKEN')}
    leaderboard = requests.get(
        f"https://adventofcode.com/2022/{os.environ.get('LEADERBOARD-URI')}", cookies=cookies)

    with open(LOCAL_LEADERBOARD, 'w') as leader_file:
        leader_dict = json.dumps(leaderboard.json())
        if leader_dict:
            leader_file.write(leader_dict)


class PlayerModel(BaseModel):
    name: str
    global_score: int
    local_score: int
    last_star_ts: Optional[str]
    stars: int
    completion_day_level: str

    @validator('last_star_ts', pre=True)
    def parse_ts(cls, value):
        return datetime.fromtimestamp(
            value).strftime('%d.%m.%Y, %H:%M')

    @validator('completion_day_level', pre=True)
    def parse_completion(cls, value):
        return "".join(map(lambda x: u'\u2605' if str(x) in value.keys() else u'\u2606', range(1, 25)))


if __name__ == '__main__':
    load_dotenv()
    main()

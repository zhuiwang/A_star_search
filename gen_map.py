

import json
import random
from tkinter import S

from traceback import print_tb
from typing import _Protocol, Dict, List, Iterator, Tuple, TypeVar, Optional

from pyparsing import rest_of_line
GridLocation = Tuple[int, int]


class GenMap:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.map = {'map': [[ '.' for i in range(width)] for i in range(height)]}

        self.map['map'][0][0] = 'R'
        self.map['map'][self.height - 1][self.width - 1] = 'S'
        self.map['score'] = { 'R':0,
        'S':0
        }
        self.map['round'] = 0

    def update_map_resource(self):
        for pos in self.get_locations():
            rand_num = random.randint(10, 30)
            self.map['map'][pos[0]][pos[1]] = rand_num
            print(f'Set [{pos[0]}, {pos[1]}] to {rand_num}')

    def get_locations(self):
        times = random.randint(1, 5)
        res_locations = []
        for i in range(times):
            pos = self.gen_rand_location()
            res_locations.append(pos)
        return res_locations

    def gen_rand_location(self):
        x_pos = random.randint(0, self.width - 1)
        y_pos = random.randint(0, self.height - 1)

        while self.map['map'][y_pos][x_pos] != '.':
            x_pos = random.randint(0, self.width - 1)
            y_pos = random.randint(0, self.height - 1)
        return [y_pos, x_pos]

    def draw_map(self):
        map = self.map['map']

        print('---'*self.width)
        for y in range(self.height):
            for x in range(self.width):
                if len(str(map[y][x])) == 1:
                    print(f" {map[y][x]} ", end='')
                elif len(str(map[y][x])) == 2:
                    print(f" {map[y][x]}", end='')
            print('')
        print('~~~'*self.width)


    def write_josn_to_file(self):
        with open('./runtime_data/round_01_for_A.json', 'w') as f:
            f.write(json.dumps(self.map, indent=4, separators=(',', ':')))


if __name__ == "__main__":
    # 7 line 3 collm
    s = GenMap(10, 10)
    # print(s.grid_map)
    s.update_map_resource()
    s.draw_map()
    s.write_josn_to_file()
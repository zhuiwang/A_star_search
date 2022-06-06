

import json

from traceback import print_tb
from typing import _Protocol, Dict, List, Iterator, Tuple, TypeVar, Optional
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



    def draw_map(self):
        map = self.map['map']

        print('---'*self.width)
        for y in range(self.height):
            for x in range(self.width):
                print(f" {map[y][x]} ", end='')
            print('')
        print('~~~'*self.width)


    def write_josn_to_file(self):
        with open('map.json', 'w') as f:
            f.write(json.dumps(self.map, indent=4, separators=(',', ':')))

if __name__ == "__main__":
    # 7 line 3 collm
    s = GenMap(10, 10)
    # print(s.grid_map)
    s.draw_map()
    s.write_josn_to_file()
import json
from typing import _Protocol, Dict, List, Iterator, Tuple, TypeVar, Optional

T = TypeVar('T')

GridLocation = Tuple[int, int]

Location = TypeVar('Location')


class SquareGrid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.walls: List[GridLocation] = []

    def in_bounds(self, id: GridLocation) -> bool:
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id: GridLocation) -> bool:
        return id not in self.walls

    def neighbors(self, id: GridLocation) -> Iterator[GridLocation]:
        (x, y) = id
        # eight neighbors
        # neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)] # E W N S
        # four neighbors
        neighbors = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]  # E W N S
        # see "Ugly paths" section for an explanation:
        if (x + y) % 2 == 0: neighbors.reverse()  # S N W E
        results = filter(self.in_bounds, neighbors)
        results = filter(self.passable, results)
        return results

class MapAnalyser(SquareGrid):
    def __init__(self, map) -> None:
        self.map = map
        self.width = len(map[0])
        self.height = len(map)
        self.start = []
        super(MapAnalyser, self).__init__(self.width, self.height)

    def get_resource_point(self):
        resource_poss= []
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == 'R':
                    self.start = [x, y]

                if self.map[y][x] not in ['.', 'R', 'S']:
                    print(f'resource_found in [{x}, {y}], resource is {self.map[y][x]}')
                    resource_poss.append([x, y])
        return resource_poss

    def get_des_pos(self):
        des_poss = []
        for pos in self.get_resource_point():
            for neighbor in self.neighbors(pos):
                if neighbor not in des_poss:
                    des_poss.append(neighbor)
        # [x, y]
        return des_poss

if __name__ == "__main__":
    with open('./runtime_data/round_01_for_A.json', 'r') as f:
        data = json.load(f)
    data_map = data['map']
    m = MapAnalyser(data_map)
    res = m.get_des_pos()

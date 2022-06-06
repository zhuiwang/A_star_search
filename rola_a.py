
import json
import mapanalyser
from a_star import *



with open('./runtime_data/round_01_for_A.json', 'r') as f:
    data = json.load(f)

map = data['map']

def draw_map(map):
    width = len(map[0])
    height = len(map)
    print('---'*width)
    for y in range(height):
        for x in range(width):
            if len(str(map[y][x])) == 1:
                print(f" {map[y][x]} ", end='')
            elif len(str(map[y][x])) == 2:
                print(f" {map[y][x]}", end='')
        print('')
    print('~~~'*width)


draw_map(map)

m = mapanalyser.MapAnalyser(map)
des_poss = m.get_des_pos()
start = m.start
print('start', start)
for pos in des_poss:
    map[pos[1]][pos[0]] = '*'

draw_map(map)

diagram4 = GridWithWeights(len(map[0]), len(map))


for goal in des_poss:
    came_from, cost_so_far = a_star_search(diagram4, tuple(start), tuple(goal))
    draw_grid(diagram4, path=reconstruct_path(came_from, start=tuple(start), goal=tuple(goal)))



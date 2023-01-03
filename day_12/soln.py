from collections import defaultdict
import heapq
import math

START = (0, 20)
END = (43, 20)

with open('input.txt') as input:
    area = [
        list(line.rstrip())
        for line in input.readlines()
        ]
    
# --------------------------------- Part One ---------------------------------

def neighbors(node, area):
    def height(a):
        if a.islower():
            return ord(a)
        elif a == 'S':
            return ord('a')
        else:
            return ord('z')
    neighbors = []
    for [a, b] in [[1,0], [-1,0], [0,1], [0,-1]]:
        if 0 <= node[0] + a < len(area[0]) and 0 <= node[1] + b < len(area):
            curr_height = height(area[node[1]][node[0]])
            new_height = height(area[node[1] + b][node[0] + a])
            if new_height <= curr_height + 1:
                neighbors.append((node[0] + a, node[1] + b))
    return neighbors
    

visited = set()
queue = []
path_length = defaultdict(lambda : math.inf)
path_length[START] = 0
heapq.heappush(queue, (0, START))

while queue:
    length, curr = heapq.heappop(queue)
    if curr == END:
        break
    visited.add(curr)
    for neighbor in neighbors(curr, area):
        if neighbor in visited:
            continue
        if length + 1 < path_length[neighbor]:
            path_length[neighbor] = length + 1
            heapq.heappush(queue, (length + 1, neighbor))
                  
print(f'Shortest path to the best signal is {length}')

# --------------------------------- Part Two ---------------------------------

def new_neighbors(node, area):
    def height(a):
        if a.islower():
            return ord(a)
        elif a == 'S':
            return ord('a')
        else:
            return ord('z')
    neighbors = []
    for [a, b] in [[1,0], [-1,0], [0,1], [0,-1]]:
        if 0 <= node[0] + a < len(area[0]) and 0 <= node[1] + b < len(area):
            curr_height = height(area[node[1]][node[0]])
            new_height = height(area[node[1] + b][node[0] + a])
            if curr_height <= new_height + 1:
                neighbors.append((node[0] + a, node[1] + b))
    return neighbors

visited = set()
queue = []
path_length = defaultdict(lambda : math.inf)
path_length[END] = 0
heapq.heappush(queue, (0, END))

while queue:
    length, curr = heapq.heappop(queue)
    if area[curr[1]][curr[0]] in ('a', 'S'):
        break
    visited.add(curr)
    for neighbor in new_neighbors(curr, area):
        if neighbor in visited:
            continue
        if length + 1 < path_length[neighbor]:
            path_length[neighbor] = length + 1
            heapq.heappush(queue, (length + 1, neighbor))
                  
print(f'Shortest path to the best signal from any start is {length}')
        




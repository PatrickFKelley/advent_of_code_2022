from collections import defaultdict

SAND_START = (500, 0)

with open('input.txt') as input:
    raw_data = [
        line.rstrip()
        for line in input.readlines()
        ]
    data = [
        [eval('(' + point + ')')
        for point in path.split(' -> ')]
        for path in raw_data
        ]
    low_rock = max([
        point[1]
        for path in data
        for point in path
        ])
    
# --------------------------------- Part One ---------------------------------

free = defaultdict(lambda : True)

for path in data:
    for (curr_x, curr_y), (next_x, next_y) in zip(path[:-1], path[1:]):
        free.update([
            ((x, y), False)
            for x in range(min(curr_x, next_x), max(curr_x, next_x) + 1)
            for y in range(min(curr_y, next_y), max(curr_y, next_y) + 1)
            ])
        
curr_sand = SAND_START
landed_sand = 0

while curr_sand[1] < low_rock:
    (curr_x, curr_y) = curr_sand
    if free[(curr_x, curr_y + 1)]:
        curr_sand = (curr_x, curr_y + 1)
    elif free[(curr_x - 1, curr_y + 1)]:
        curr_sand = (curr_x - 1, curr_y + 1)
    elif free[(curr_x + 1, curr_y + 1)]:
        curr_sand = (curr_x + 1, curr_y + 1)
    else:
        free[curr_sand] = False
        landed_sand += 1
        curr_sand = SAND_START
        
print(f'The total amount of landed sand is {landed_sand}')

# --------------------------------- Part Two ---------------------------------

floor = low_rock + 2

while free[SAND_START]:
    (curr_x, curr_y) = curr_sand
    if free[(curr_x, curr_y + 1)] and curr_y + 1 < floor:
        curr_sand = (curr_x, curr_y + 1)
    elif free[(curr_x - 1, curr_y + 1)] and curr_y + 1 < floor:
        curr_sand = (curr_x - 1, curr_y + 1)
    elif free[(curr_x + 1, curr_y + 1)] and curr_y + 1 < floor:
        curr_sand = (curr_x + 1, curr_y + 1)
    else:
        free[curr_sand] = False
        landed_sand += 1
        curr_sand = SAND_START
        
print(f'The total amount of landed sand before'\
      f'the source blocks is {landed_sand}')
with open('input.txt') as input:
    raw_data = [
        line.rstrip().split(' ')
        for line in input.readlines()
        ]
    data = [
        ((int(sensor[2][2:-1]), int(sensor[3][2:-1])),
         (int(sensor[8][2:-1]), int(sensor[9][2:])))
        for sensor in raw_data
        ]
    
# --------------------------------- Part One ---------------------------------

CHECK_ROW = 2000000

unoccupied = set()

def man_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

for (sensor_x, sensor_y), (beacon_x, beacon_y) in data:
    dist = man_dist((sensor_x, sensor_y), (beacon_x, beacon_y))
    dist_remain = dist - abs(sensor_y - CHECK_ROW)
    for x in range(sensor_x - dist_remain, sensor_x + dist_remain + 1):
        unoccupied.add((x, CHECK_ROW))
    unoccupied.discard((beacon_x, beacon_y))

print(f'Total unoccupied space is {len(unoccupied)}')

# --------------------------------- Part Two ---------------------------------

BOUNDARY = 4000000

def dist_sum(point, args):
    sensors, distances = args
    result = 0
    for i, sensor in enumerate(sensors):
        dist = man_dist(sensor, point)
        if dist 
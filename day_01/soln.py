from itertools import groupby
import heapq

# Reads input file and creates an array of total calories held by each elf

with open('input.txt') as input:
    elves = [sum(list(map(int, g))) for k, g 
                     in groupby(input.read().splitlines(), lambda x: x != '')
                     if k]

# --------------------------------- Part One ---------------------------------

print(f'The maximum calories carried by an elf is {max(totals)}')

# --------------------------------- Part Two ---------------------------------

top = 3

negElves = [-elf for elf in elves]
heapq.heapify(negElves)

topTotalSum = 0
for _ in range(top):
    topTotalSum -= heapq.heappop(negTotals)

print(f'The total calories carried by the top {top} elves is {topTotalSum}')
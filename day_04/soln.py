# Reads input file

with open('input.txt') as input:
    pairs = [[list(map(int, elf.split('-')))
             for elf in line.strip().split(',')]
             for line in input.readlines()]
    
# --------------------------------- Part One ---------------------------------

def fullyContain(pair):
    firstContain = pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]
    secondContain = pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]
    return firstContain or secondContain

totalContain = sum([fullyContain(pair) for pair in pairs])

print(f'The number of redundant assignment pairs is {totalContain}')

# --------------------------------- Part Two ---------------------------------

def overlap(pair):
    return pair[0][1] >= pair[1][0] and pair[0][0] <= pair[1][1]

totalOverlap = sum([overlap(pair) for pair in pairs])

print(f'The number of overlapping assignment pairs is {totalOverlap}')
        

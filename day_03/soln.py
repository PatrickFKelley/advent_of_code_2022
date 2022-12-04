# Reads input file

with open('input.txt') as input:
    rucksacks = [line.strip() for line in input.readlines()]
    
# --------------------------------- Part One ---------------------------------

def rucksackValue(compartment1, compartment2):
    intersect = set(compartment1).intersection(set(compartment2)).pop()
    return ord(intersect) - ord('a') + 1 if intersect.islower() else ord(intersect) - ord('A') + 27

totalPriority = sum([rucksackValue(r[:len(r)//2], r[len(r)//2:]) for r in rucksacks])

print(f'Total priority value of the rucksacks is {totalPriority}')

# --------------------------------- Part Two ---------------------------------

def threeElfBadge(elf1, elf2, elf3):
    intersect = set(elf1).intersection(set(elf2)).intersection(set(elf3)).pop()
    return ord(intersect) - ord('a') + 1 if intersect.islower() else ord(intersect) - ord('A') + 27

totalThreePriority = sum([threeElfBadge(rucksacks[3*i], rucksacks[3*i+1], rucksacks[3*i+2])
                          for i in range(len(rucksacks)//3)])

print(f'Total badge priorities of three elf teams is {totalThreePriority}')
    
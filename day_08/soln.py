from functools import reduce

# Reads input file

with open('input.txt') as input:
    forest = [ list(map(int, line.rstrip())) for line in input.readlines()]
    forestRows = len(forest)
    forestCols = len(forest[0])
    
# --------------------------------- Part One ---------------------------------

# Computes the sightlines from a given tree

def computeSightLines(x, y, forest):
    left = forest[y][:x][::-1]
    right = forest[y][x+1:]
    above = [row[x] for row in forest[:y][::-1]]
    below = [row[x] for row in forest[y+1:]]
    return [left, right, above, below]

# Determines if a given tree is visible or not

def isVisible(x, y, forest):
    sightLines = computeSightLines(x, y, forest)
    height = forest[y][x]
    return any([height > max(line) for line in sightLines if line])

perimeter = 2 * (forestRows + forestCols) - 4
numVisible = perimeter + sum([isVisible(x, y, forest)
                              for x in range(1, forestCols-1)
                              for y in range(1, forestRows-1)])

print(f'The number of visible trees is {numVisible}')

# --------------------------------- Part One ---------------------------------

# Computes scenic score for a given tree

def scenicScore(x, y, forest):
    sightLines = computeSightLines(x, y, forest)
    height = forest[y][x]
    viewLengths = []
    for line in sightLines:
        if line:
            for i, tree in enumerate(line):
                if height <= tree:
                    break
            viewLengths.append(len(line[:i+1]))
    return reduce(lambda a,b: a*b, viewLengths)

topScenicScore = max([scenicScore(x, y, forest) 
                      for x in range(forestCols) 
                      for y in range(forestRows)])

print(f'The maximum scenic score is {topScenicScore}')
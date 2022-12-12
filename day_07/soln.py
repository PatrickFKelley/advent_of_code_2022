smallFileSize = 100000
totalSystemSize = 70000000
neededSpace = 30000000

# N-ary tree class used to model file system

class Node(object):
    def __init__(self, parent=None, size=0):
        self.parent = parent
        self.size = size
        self.children = {}

# Reads input file

with open('input.txt') as input:
    commands = [line.rstrip().split(' ') for line in input.readlines()][2:]
    
# Models file system

topDir = Node()
currDir = topDir

for command in commands:
    if len(command) == 3:
        if command[2] == '..':
            currDir = currDir.parent
        else:
            if command[2] not in currDir.children:
                currDir.children[command[2]] = Node(parent=currDir)
            currDir = currDir.children[command[2]]
    elif command[0] == 'dir':
        currDir.children[command[1]] = Node(parent=currDir)
    elif command[0].isdigit():
        currDir.children[command[1]] = Node(parent=currDir,
                                            size=int(command[0]))

# Updates sizes in file system model to include subfiles and subdirectories

def updateSize(currDir, sizes):
    if currDir.size == 0:
        for subDir in currDir.children.values():
            updateSize(subDir, sizes)
            currDir.size += subDir.size
        sizes.append(currDir.size)

sizes = []
updateSize(topDir, sizes)

# --------------------------------- Part One ---------------------------------
            
totalSmallSize = sum([size for size in sizes if size <= smallFileSize])

print(f'The total combined size of small directories is {totalSmallSize}')

# --------------------------------- Part Two ---------------------------------

needToRemove = neededSpace - (totalSystemSize - topDir.size)

minRemoveSize = min([size for size in sizes if size >= needToRemove])

print(f'The minimum size of a directory to delete is {minRemoveSize}')

numStacks = 9
maxInitialHeight = 8

# Reads input file

with open('input.txt') as input:
    lines = input.readlines()
    stacks = [[] for _ in range(numStacks)]
    for line in lines[:maxInitialHeight][::-1]:
        for i in range(numStacks):
            if line[4*i + 1] != ' ':
                stacks[i].append(line[4*i + 1])
                
    moves = [list(map(int, line.rsplit()[1::2]))
              for line in lines[maxInitialHeight + 2:]]
    
stacksCopy = [stack.copy() for stack in stacks]
    
# --------------------------------- Part One ---------------------------------

def moveBoxes(move, stacks):
    for _ in range(move[0]):
        stacks[move[2] - 1].append(stacks[move[1] - 1].pop())

for move in moves:
    moveBoxes(move, stacks)
    
message = ''.join([stack.pop() for stack in stacks])
print(f'The combined message is {message}')

# --------------------------------- Part Two ---------------------------------

def moveBoxesNew(move, stacks):
    for _ in range(move[0]):
        stacks[move[2] - 1].append(stacks[move[1] - 1].pop())
    stacks[move[2] - 1][-move[0]:] = reversed(stacks[move[2] - 1][-move[0]:])
    
for move in moves:
    moveBoxesNew(move, stacksCopy)

messageNew = ''.join([stack.pop() for stack in stacksCopy])
print(f'The new combined message is {messageNew}')


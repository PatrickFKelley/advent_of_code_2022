import numpy as np

# Reads input file

with open('input.txt') as input:
    moves = [line.rstrip().split(' ') 
             for line in input.readlines()]
    
# --------------------------------- Part One ---------------------------------

# Updates head and tail positions for a series of moves and updates
# the set of known tail positions

def moveRope(head, tail, move, tailSeen):
    dir = {'R' : [1,0],
           'L' : [-1,0],
           'U' : [0,1],
           'D' : [0,-1]}
    for _ in range(int(move[1])):
        prevHead = head
        head = (head[0] + dir[move[0]][0], head[1] + dir[move[0]][1])
        if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
            tail = prevHead
        tailSeen.add(tail)
    return head, tail

head = tail = (0, 0)
tailSeen = {(0,0)}

for move in moves:
    head, tail = moveRope(head, tail, move, tailSeen)
    
print(f'The tail of the rope visits {len(tailSeen)} different positions')

# --------------------------------- Part Two ---------------------------------

totalKnots = 10

# Computes new knot position based on previous knot position

def moveSingleKnot(currKnot, prevKnot):
    xDiff = prevKnot[0] - currKnot[0]
    yDiff = prevKnot[1] - currKnot[1]
    if abs(xDiff) > 1 or abs(yDiff) > 1:
        currKnot = (currKnot[0] + np.sign(xDiff),
                    currKnot[1] + np.sign(yDiff))
    return currKnot

# Updates the positions of every knot for a series of moves and
# updates the set of known tail positions

def moveKnottedRope(knots, move, tailSeen):
    dir = {'R' : [1,0],
           'L' : [-1,0],
           'U' : [0,1],
           'D' : [0,-1]}
    for _ in range(int(move[1])):
        knots[0] = (knots[0][0] + dir[move[0]][0], 
                    knots[0][1] + dir[move[0]][1])
        for i in range(1, len(knots)):
            knots[i] = moveSingleKnot(knots[i], knots[i-1])
        tailSeen.add(knots[-1])
    return knots

knots = [(0,0)] * totalKnots
tailSeen = {(0,0)}

for move in moves:
    knots = moveKnottedRope(knots, move, tailSeen)

print(f'The tail of extra knotted rope visits'\
      f' {len(tailSeen)} different positions')
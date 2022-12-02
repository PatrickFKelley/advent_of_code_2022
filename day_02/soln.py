# Reads input file

with open('input.txt') as input:
    matches = [line.rsplit() for line in input.readlines()]
    
# --------------------------------- Part One ---------------------------------

def matchValue(match):
    throwValue = ord(match[1]) - ord('X') + 1
    resultValue = ((ord(match[1]) - ord(match[0]) - ord('X') + ord('A') + 1) % 3) * 3
    return throwValue + resultValue

totalMatchValue = sum(map(matchValue, matches))

print(f'Following the strategy guide yields {totalMatchValue} points.')

# --------------------------------- Part Two ---------------------------------

def correctMatchValue(match):
    throwValue = ((ord(match[0]) + ord(match[1]) - ord('X') - ord('A') - 1) % 3) + 1
    resultValue = (ord(match[1]) - ord('X')) * 3
    return throwValue + resultValue

totalCorrectMatchValue = sum(map(correctMatchValue, matches))

print(f'Following the strategy guide CORRECTLY yeilds {totalCorrectMatchValue} points.')
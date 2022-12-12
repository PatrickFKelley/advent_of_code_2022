packetSize = 4
messageSize = 14

# Reads input file

with open('input.txt') as input:
    data = list(input.readline())
    
# --------------------------------- Part One ---------------------------------

packetMarker = 0

for i in range(packetSize, len(data)):
    if len(set(data[i - packetSize:i])) == packetSize:
        packetMarker = i
        break
    
print(f'The first start-of-packet marker is detected '\
      f'after {packetMarker} characters')

# --------------------------------- Part Two ---------------------------------

messageMarker = 0

for i in range(messageSize, len(data)):
    if len(set(data[i - messageSize:i])) == messageSize:
        messageMarker = i
        break
    
print(f'The first start-of-message marker is detected '\
      f'after {messageMarker} characters')
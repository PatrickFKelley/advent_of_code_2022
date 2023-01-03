from functools import cmp_to_key

START_DIVIDER = [[2]]
END_DIVIDER = [[6]]

with open('input.txt') as input:
    raw_data = [
        line.rstrip()
        for line in input.readlines()
        ]
    data = [
        [eval(raw_data[i]),
        eval(raw_data[i+1])]
        for i in range(0, len(raw_data),3)
        ]
    aug_data = [
        line
        for packet in data
        for line in packet
        ] + [START_DIVIDER, END_DIVIDER]
    
# --------------------------------- Part One ---------------------------------

def compare(left, right, i=0):
    
    if i == len(left) and i == len(right):
        raise IndexError
        
    elif i == len(left) or i == len(right):
        return len(left) < len(right)
    
    
    elif type(left[i]) == int and type(right[i]) == int:
        if left[i] != right[i]:
            return left[i] < right[i]
        else:
            return compare(left, right, i+1)
        
    elif type(left[i]) != list:
        new_left = [
            left[j] if j != i else [left[j]]
            for j in range(len(left))
            ]
        return compare(new_left, right, i)
    
    elif type(right[i]) != list:
        new_right = [
            right[j] if j != i else [right[j]]
            for j in range(len(right))
            ]
        return compare(left, new_right, i)
    
    else:
        try:
            return compare(left[i], right[i])
        except IndexError:
            return compare(left, right, i+1)
        
index_sum = 0
for i, [left, right] in enumerate(data, start=1):
    if compare(left, right):
        index_sum += i
        
print(f'The total sum of ordered indices is {index_sum}')

# --------------------------------- Part Two ---------------------------------
            
def num_compare(left, right):
    if compare(left, right):
        return 1
    else:
        return -1

aug_data.sort(key=cmp_to_key(num_compare), reverse = True)
start_index = aug_data.index(START_DIVIDER) + 1
end_index = aug_data.index(END_DIVIDER) + 1
decoder_key = start_index * end_index

print(f'The decoder key for the distress signal is {decoder_key}')
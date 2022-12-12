ROW_LENGTH = 40
NUM_ROWS = 6

with open('input.txt') as input:
    instructs = [line.rstrip().split(' ')
             for line in input.readlines()]

# --------------------------------- Part One ---------------------------------

def perform_instruct(instruct, x, cycle_count, strength_cycles):
    cycle_count += 1
    check_strength(x, cycle_count, strength_cycles)
    if len(instruct) > 1:
        cycle_count += 1
        check_strength(x, cycle_count, strength_cycles)
        x += int(instruct[1])
    return x, cycle_count, strength_cycles
        
        
def check_strength(x, cycle_count, strength_cycles):
    if (cycle_count % 40) == 20:
        strength_cycles.append(x * cycle_count)
        
def all_instructs(instructs, x, cycle_count, strength_cycles):
    for instruct in instructs:
        x, cycle_count, strength_cycles = perform_instruct(instruct,
                                                           x, 
                                                           cycle_count, 
                                                           strength_cycles)
    return x, cycle_count, strength_cycles

x = 1
cycle_count = 0
strength_cycles = []

x, cycle_count, strength_cycles = all_instructs(instructs,
                                                x, 
                                                cycle_count, 
                                                strength_cycles)


print(f'Total signal strength detected is {sum(strength_cycles)}')

# --------------------------------- Part One ---------------------------------

def perform_drawing(instruct, x, pixels):
    x, pixels = check_pixel(x, pixels)
    if len(instruct) > 1:
        x, pixels = check_pixel(x, pixels)
        x += int(instruct[1])
    return x, pixels

def check_pixel(x, pixels):
    if abs(x - (len(pixels) % 40)) <= 1:
        pixels += '#'
    else:
        pixels += '.'
    return x, pixels

def all_drawings(instructs, x, pixels):
    for instruct in instructs:
        x, pixels = perform_drawing(instruct, x, pixels)
    return x, pixels

def draw_result(pixels):
    for i in range(NUM_ROWS):
        print(pixels[ROW_LENGTH*i: ROW_LENGTH*(i+1)])

x = 1
pixels = ''

x, pixels = all_drawings(instructs, x, pixels)

print('The resulting CRT screen is displayed below:')

draw_result(pixels)
    
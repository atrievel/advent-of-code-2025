MIN = 0
MAX = 99
current = 50
num_exact_rotations = 0

def rotate(increment):
    global current, num_exact_rotations

    current += increment

    while current > MAX:
        current = MIN + (current - MAX - 1)

    while current < MIN:
        current = MAX - (MIN - current - 1)

    if current == 0:
        num_exact_rotations += 1
    

with open('data.txt', 'r') as file:
    for line in file:
        parsed = line.strip()

        direction = parsed[0]
        value = int(parsed[1:])

        rotate(value if direction == 'R' else -value)

print(f"Final Position: {current} - Total Exact Rotations: {num_exact_rotations}")
MIN = 0
MAX = 99
current = 50
num_exact_rotations = 0

with open('data.txt', 'r') as file:
    for line in file:
        parsed = line.strip()

        direction = parsed[0]
        value = int(parsed[1:])
        current = ((current - value) if direction == 'L' else (current + value)) % 100

        if current == 0:
            num_exact_rotations += 1

print(num_exact_rotations)
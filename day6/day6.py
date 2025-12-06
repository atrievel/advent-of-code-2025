total = 0
data = []

with open("data.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

for line in lines[:-1]:
    row = [int(x) for x in line.split()]
    data.append(row)

operations = lines[-1].split()

current_column = 0
for op in operations:
    current_total = 1 if op == '*' else 0
    
    match op:
        case '*':
            for row in data:
                current_total *= row[current_column]
        case _:
            for row in data:
                current_total += row[current_column]
            
    total += current_total
    current_column += 1
    
print(total)
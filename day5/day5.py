with open("data.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

split_index = next(i for i, line in enumerate(lines) if '-' not in line)

ranges = [tuple(map(int, line.split('-'))) for line in lines[:split_index]]
values = [int(line) for line in lines[split_index:]]

print(sum(1 for v in values if any(start <= v <= end for start, end in ranges)))
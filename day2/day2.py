import csv

total = 0

def is_invalid(id):
    mid = len(id) // 2
    left = id[:mid]
    right = id[mid:]

    return left == right 

with open('data.csv', 'r', newline='') as file:
    csvreader = csv.reader(file)

    data = next(csvreader)
    
    for id_range in data:
        start, end = map(int, id_range.split('-'))
        
        for number in range(start, end + 1):
            total += number if is_invalid(list(str(number))) else 0

print(total)
total = 0

with open('data.txt', 'r') as file:
    for line in file:
        parsed = line.strip()
        
        best_start = 0
        best_end = 1
        
        for i in range(len(parsed) - 1):
            if parsed[i] > parsed[best_start]:
                best_start = i
                best_end = i + 1
            elif parsed[i + 1] > parsed[best_end]:
                best_end = i + 1
                
        total += int(parsed[best_start]) * 10 + int(parsed[best_end])
        
print(total)
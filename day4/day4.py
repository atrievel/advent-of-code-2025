count_under_4 = 0
grid = []
directions = [(-1,-1), (-1,0), (-1,1),
              (0,-1),         (0,1),
              (1,-1), (1,0), (1,1)]

with open("data.txt", "r") as file:
    for line in file:
        grid.append(list(line.strip()))

rows = len(grid)
cols = len(grid[0])

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '@':
            neighbor_count = 0
            
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                
                if 0 <= ni < rows and 0 <= nj < cols:
                    if grid[ni][nj] == '@':
                        neighbor_count += 1
                        
            if neighbor_count < 4:
                count_under_4 += 1

print(count_under_4)

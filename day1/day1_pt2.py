MOD = 100
current = 50
total = 0

with open('data.txt', 'r') as file:
    for line in file:
        parsed = line.strip()
        
        direction = parsed[0]
        value = int(parsed[1:])

        if direction == 'R':
            offset = (MOD - current) % MOD
            
            if offset == 0:
                hits = value // MOD
            else:
                hits = ((value - offset) // MOD + 1) if value >= offset else 0

            total += hits
            current = (current + value) % MOD

        else:
            offset = current % MOD
            
            if offset == 0:
                hits = value // MOD
            else:
                hits = ((value - offset) // MOD + 1) if value >= offset else 0

            total += hits
            current = (current - value) % MOD

print(total)

import heapq
import time

# Grid peta drone:
# Angka = biaya elevasi
# # = zona terlarang
# S = start, G = goal
grid4 = [
    ['S', 1, 2, '#', 3],
    [1,   '#', 2, 4, 1],
    [2,   3,   1, '#', 2],
    [3,   '#', 1, 2, 3],
    [2,   2,   1, 1, 'G']
]

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_symbol(grid, symbol):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == symbol:
                return (i, j)
    return None

def get_cost(value):
    if isinstance(value, int):
        return value
    if value in ('S', 'G'):
        return 1
    return float('inf')

def a_star_drone(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + manhattan(start, goal), 0, start, [start]))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal:
            return path, g, len(visited)
        if current in visited:
            continue
        visited.add(current)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = current[0]+dx, current[1]+dy
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                value = grid[ni][nj]
                if value != '#' and (ni, nj) not in visited:
                    cost = get_cost(value)
                    new_g = g + cost
                    priority = new_g + manhattan((ni, nj), goal)
                    heapq.heappush(open_set, (priority, new_g, (ni, nj), path + [(ni, nj)]))
    return None, float('inf'), len(visited)

# Jalankan
start = find_symbol(grid4, 'S')
goal = find_symbol(grid4, 'G')

start_time = time.time()
path, cost, nodes = a_star_drone(grid4, start, goal)
time_taken = (time.time() - start_time) * 1000

# Output
print("A* Drone Path:", path)
print("Total cost (elevasi):", cost)
print("Execution time (ms):", round(time_taken, 2))
print("Visited nodes:", nodes)

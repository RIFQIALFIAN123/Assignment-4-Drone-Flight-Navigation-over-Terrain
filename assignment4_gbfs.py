import heapq
import time

# Grid peta drone:
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

def gbfs_drone(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (manhattan(start, goal), start, [start]))
    visited = set()

    while open_set:
        h, current, path = heapq.heappop(open_set)
        if current == goal:
            return path, len(visited)
        if current in visited:
            continue
        visited.add(current)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = current[0]+dx, current[1]+dy
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                val = grid[ni][nj]
                if val != '#' and (ni, nj) not in visited:
                    heapq.heappush(open_set, (manhattan((ni, nj), goal), (ni, nj), path + [(ni, nj)]))
    return None, len(visited)

# Jalankan GBFS
start = find_symbol(grid4, 'S')
goal = find_symbol(grid4, 'G')

start_time = time.time()
path, nodes = gbfs_drone(grid4, start, goal)
time_taken = (time.time() - start_time) * 1000

# Output
print("GBFS Drone Path:", path)
print("Execution time (ms):", round(time_taken, 2))
print("Visited nodes:", nodes)

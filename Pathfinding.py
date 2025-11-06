

from queue import Queue, PriorityQueue

# Maze: 0 = free, 1 = obstacle
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)
rows, cols = len(maze), len(maze[0])
dirs = [(-1,0),(1,0),(0,-1),(0,1)]  # Up, Down, Left, Right

# Utility to print maze with path
def print_path(path):
    for r in range(rows):
        for c in range(cols):
            if (r,c) == start: print('S', end=' ')
            elif (r,c) == goal: print('G', end=' ')
            elif (r,c) in path: print('*', end=' ')
            elif maze[r][c] == 1: print('#', end=' ')
            else: print('.', end=' ')
        print()
    print()

# BFS
def bfs():
    q = Queue(); q.put((start,[start])); visited=set([start])
    while not q.empty():
        (r,c), path = q.get()
        if (r,c)==goal: return path
        for dr,dc in dirs:
            nr,nc=r+dr,c+dc
            if 0<=nr<rows and 0<=nc<cols and maze[nr][nc]==0 and (nr,nc) not in visited:
                visited.add((nr,nc))
                q.put(((nr,nc), path+[(nr,nc)]))
    return None

# DFS
def dfs():
    stack = [(start,[start])]; visited=set([start])
    while stack:
        (r,c), path = stack.pop()
        if (r,c)==goal: return path
        for dr,dc in dirs:
            nr,nc=r+dr,c+dc
            if 0<=nr<rows and 0<=nc<cols and maze[nr][nc]==0 and (nr,nc) not in visited:
                visited.add((nr,nc))
                stack.append(((nr,nc), path+[(nr,nc)]))
    return None

# A* with Manhattan distance
def heuristic(a,b): return abs(a[0]-b[0])+abs(a[1]-b[1])
def a_star():
    pq=PriorityQueue(); pq.put((0,start,[start])); cost={start:0}
    while not pq.empty():
        _, curr, path = pq.get()
        if curr==goal: return path
        for dr,dc in dirs:
            nr,nc=curr[0]+dr,curr[1]+dc; nbr=(nr,nc)
            if 0<=nr<rows and 0<=nc<cols and maze[nr][nc]==0:
                new_cost=cost[curr]+1
                if nbr not in cost or new_cost<cost[nbr]:
                    cost[nbr]=new_cost
                    pq.put((new_cost+heuristic(goal,nbr),nbr,path+[nbr]))
    return None

# ------------------- Run Algorithms -------------------
print("BFS Path:"); print_path(bfs())
print("DFS Path:"); print_path(dfs())
print("A* Path:"); print_path(a_star())


/*COMMAND: python maze_pathfinding.py      or
          
          python3 maze_pathfinding.py

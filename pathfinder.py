from collections import deque
import math


class Node:
    def __init__(self,data = None):
        self.curr = data
        self.parent = None

def move_y(y):
    if y == -1:
        return "LEFT"
    if y == 1:
        return "RIGHT"

def move_X(X):
    if X == -1:
        return "UP"
    if X == 1:
        return "DOWN"

def possible_moves_for_val(x,y,n):
    x1 = x-1
    x2 = x+1
    y1 = y-1
    y2 = y+1
    lis = []
    if 0 <= x1 < n:
        lis.append((x1,y))
    if 0 <= x2 < n:
        lis.append((x2,y))
    if 0 <= y1 < n:
        lis.append((x,y1))
    if 0 <= y2 < n:
        lis.append((x,y2))    
    return lis            

def best_result(results):
    val = None
    mn = math.inf
    
    while  results:
        value = results.popleft()
        
        curr_position = value.curr
        moves = []
        while value.parent != None:
            value = value.parent
            diff_x , diff_y = (curr_position[0]-value.curr[0],curr_position[1]-value.curr[1])
            if diff_x == 0:
                moves.append(move_y(diff_y))
            else:
                moves.append(move_X(diff_x))
            curr_position = value.curr   

        if len(moves) <= mn:
            mn = len(moves)
            val = moves 
                            
        
    return reversed(val)

def displayPathtoPrincess(n,grid):
    q = deque()
    check = []
    for i in range(n):
        inner = [0 for j in range(n)]
        check.append(inner)
    start = Node((1,3))
    q.append(start)
    x,y = start.curr
    check[x][y] = 1   
    results = deque() 
    while q:
        val = q.popleft()
        
        x, y = val.curr
        if grid[x][y] == 'p':
            results.append(val)
        possible_moves  = possible_moves_for_val(x,y,n)
        for i in possible_moves:
            x,y = i
            if check[x][y] == 0:
                check[x][y] = 1
                child =Node(i)
                child.parent = val
                q.append(child)
    for i in best_result(results):
        print(i)








m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
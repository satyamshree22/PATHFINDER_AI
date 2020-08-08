from collections import deque
import math

# node structure defined 
class Node:
    def __init__(self,data = None):
        self.curr = data
        self.parent = None

# mmoves finders
def move_y(y):
    if y == -1:
        return "LEFT"
    if y == 1:
        return "RIGHT"

def move_x(X):
    if X == -1:
        return "UP"
    if X == 1:
        return "DOWN"

# possible moves finder 
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

# best results 
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
                moves.append(move_x(diff_x))
            curr_position = value.curr   

        if len(moves) <= mn:
            mn = len(moves)
            val = moves 
                            
    return reversed(val)    
"""
    def get_graphic_result(result,grid,m):
        steps = deque()
        for i in result:
            deque.append
        for i in range(m):
"""

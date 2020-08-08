from helper import Node,deque,math,move_y,move_x,best_result,possible_moves_for_val


def displayPathtoPrincess(n,grid,start_position):
    q = deque()
    check = []
    for i in range(n):
        inner = [0 for j in range(n)]
        check.append(inner)
    start = Node(start_position)
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
    




if __name__ == "__main__":
    m = int(input())
    grid = [] 
    x,y = map(int,input().split())
    start = (x,y)
    for i in range(0, m): 
        grid.append(input().strip())

    displayPathtoPrincess(m,grid,start)

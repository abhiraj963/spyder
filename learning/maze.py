n = int(input('enter the no of roads: '))
maze = {}
for i in range(0,n):
    lst_in = []
    for j in range(0,n):
        lst_in.append(int(input('enter weight: ')))
    maze[i] = lst_in
    
def exchange_weight(w1,w2):
    if w2 > w1:
        return w2
    return w1

def has_right(pos,maze):
    key,value = pos
    if value < len(maze[key])-1:
        return True
    
def has_down(pos,maze):
    key,value = pos
    if key < len(maze)-1:
        return True
    
def move_right(pos,maze,w):
    key,value = pos
    new_w = exchange_weight(w,maze[key][value+1])
    new_pos = (key,value+1)
    return new_w, new_pos
    
def move_down(pos,maze,w):
    key,value = pos
    new_pos = (key+1,value)
    new_w = exchange_weight(w,maze[key+1][value])
    return new_w, new_pos

def move_decide(maze,w,pos):
    print(w,pos)
    if not has_right(pos,maze) and not has_down(pos,maze):
        return w,pos     
    if has_right(pos,maze) and has_down(pos,maze):
        w_r,pos_r = move_right(pos,maze,w)
        w_d,pos_d = move_down(pos,maze,w)
        if w_r < w_d:
            move_decide(maze,w_r,pos_r)
        else:
            move_decide(maze,w_d,pos_d)
    if not has_down(pos,maze):
        w_r,pos_r = move_right(pos,maze,w)
        w,pos = move_decide(maze,w_r,pos_r)
    if not has_right(pos,maze):
        w_d,pos_d = move_down(pos,maze,w)
        w,pos = move_decide(maze,w_d,pos_d)
    
       
pos = (0,0)
w = 1
try:
    w,pos = move_decide(maze,w,pos)
except:
    pass  
    

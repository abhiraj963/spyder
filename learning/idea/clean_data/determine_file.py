file = 0
def det_file(path):
    for i in range(0,len(path)):
        global file
        if path[i] == '.':
            file = i
        
    if path[file+1:] == 'csv':
        return 'csv'
    elif path[file+1:] == 'xlsx':
        return 'xlsx'
            
            

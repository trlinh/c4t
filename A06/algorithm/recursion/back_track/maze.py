maze = [
    [0,0,1,0,0,0],
    [0,1,1,0,1,1],
    [0,0,0,0,0,0],
    [1,0,1,0,1,0],
    [1,0,1,0,1,1],
    [1,0,1,0,0,0]
]

def get_moves(maze,row,col):
    moves=[[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
            # u       d       l       r

    
    if col>0 and maze[row][col-1]==0:
        moves[2] =[row,col-1] 
    if col<len(maze[0])-1 and maze[row][col+1]==0:
        moves[3]=[row,col+1]
    if row<len(maze)-1 and maze[row+1][col]==0:
        moves[1]=[row+1,col]
    if row>0 and maze[row-1][col]==0:
        moves[0]=[row-1,col]
    return moves

# print(get_moves(maze,5,5))

def go(maze,start,end,path=[]):
    # print(start)
    if start==end:
        return path
    else:
        moves = get_moves(maze,start[0],start[1])
       
        for i in range(len(moves)):
            
            if moves[i] != [-1,-1]:
                maze[start[0]][start[1]]= 1
                # right= go(maze,start,end,path)
                left= go(maze,moves[i],end,path+[moves[i]])
                
                    
                maze[start[0]][start[1]]= 0
                
                # if len(left)>len(right):
                #     return right
                # return left

        # if len(left)>len(right):
        #     return right
        # return left                       
                
    

go(maze,[0,0],[5,5])

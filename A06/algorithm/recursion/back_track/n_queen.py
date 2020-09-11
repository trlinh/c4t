# board =[
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0]
# ]
# arr=[ i=i+1 for i in range 1000:]
board=[[0 for i in range(5)] for i in range (5)]

def check(board,row,col):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==1:
                
                if row == i or col == j or abs(i-row)==abs(j-col):
                    return False
                
    return True

def print_board(board):
    for row in range(len(board)):
        print(board[row])
    print()

def arrange(board, row=0):
    if row == len(board):
        print_board(board)
                
    if row < len(board):
        
        for j in range(len(board[row])):
            if check(board,row,j)== True:
                board[row][j]=1
                arrange(board,row+1)
                board[row][j]=0
        pass
            
            

# arrange(board)

print(arr)

# 13684579 tap con voi so phan tu sap xep tang dan có so phan tu lon nhat
n = 4
k = 1

x = []

for i in range(n):
    a = []
    for i in range(n):
        a.append(0)
    x.append(a)

def print_queens():
    print("********* Queens *********")

    for i in range(n):
        for j in range(n):
            if(x[i][j] == 1):
                print("Queen " + str(i+1) + ": (" + str(i+1) + ", " + str(j+1) + ")")

def place(board, r, c):
    
    for i in range(c):
        if(board[r][i] == 1):
            return False
        
    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if(board[i][j] == 1):
            return False

    for i, j in zip(range(r, n, 1), range(c, -1, -1)):
        if(board[i][j] == 1):
            return False

    return True


def nQueen(k):

    if k >= n:
        return True
        print_board(x)

    for i in range(n):
        if(place(x, i, k)):
            x[i][k] = 1

            if(nQueen(k+1) == True):
                return True

            x[i][k] = 0

    return False

if(nQueen(0) == False):
    print("No Solution")

else:
    print_queens()

def ganesh(row, col, board, n):
    # check upper Direction
    for i in range(row):
        if board[i][col] =="Q":
            return False
    # check Left Diagonal
    r = row
    c = col
    while r >=0 and c >=0:
        if board[r][c] == "Q":
            return False
        r -=1
        c -=1
    #check Right Diagonal
    r = row
    c = col
    while r >= 0 and c < n:
        if board[r][c] == "Q":
            return False
        r-= 1
        c+= 1
    return True
def pavan(no_queens, row, board, solutions):
    if row == no_queens:
        solution = []
        for r in board:
            row_str = ""
            for ch in r:
                row_str += ch
            solution.append(row_str)
        solutions.append(solution)    
        return solutions
    for col in range(no_queens):
        if ganesh(row, col, board, no_queens):
            board[row][col] = "Q"
            pavan(no_queens, row+1, board, solutions)
            board[row][col] = "."
    return solutions
no_queens = int(input(" Enter Number of queens: "))  
board = []
for rows in range(no_queens):
    row =[]
    for col in range(no_queens):
        row.append(".")
    board.append(row)

solutions = pavan(no_queens, 0, board, [])
print("Total solutions:", len(solutions))
for solution in solutions:
    for row in solution:
        print(row)
    print()    
            
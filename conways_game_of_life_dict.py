MAX_X = 10
MAX_Y = 10

def edge (cell, board, nboard):
    x,y = cell
    neighb_list = [(x-1,y),(x+1,y),(x,y-1),(x,y+1),
                  (x-1,y-1),(x+1,y-1),(x-1,y+1),(x+1,y+1)]
    for (x,y) in neighb_list:
        nboard[(x,y)] = board.get((x,y), 0)

def check(cell, board):
    life = 0
    x,y = cell
    neighb_list = [(x-1,y),(x+1,y),(x,y-1),(x,y+1),
                   (x-1,y-1),(x+1,y-1),(x-1,y+1),(x+1,y+1)]
    for (x,y) in neighb_list:
        if board.get((x,y),0):
            life += 1
    return life

def advance(board):
    nboard = {}
    for cell in board:
        edge(cell, board, nboard)
    board = nboard

    nboard = {}
    for cell in board:
            (x,y) = cell
            life = check(cell, board)
            # live cell ?
            if board.get((x,y),0):
                if life == 2 or life == 3:
                    nboard[(x,y)] = 1
            # dead cell ?
            elif life == 3:
                nboard[(x,y)] = 1
    return nboard

def display(board):
    for y in range (0, MAX_Y):
        for x in range (0, MAX_X):
            print('',board.get((x,y), '-'),'', end='')
        print()
    print()

# intialize board with glider
board = {(1,0):1, (2,1):1, (0,2):1, (1,2):1, (2,2):1}

# advance
for n in range(10):
    print("move #", n+1)
    display(board)
    board = advance(board)

def print_board(board):
    boardstring -'\n'
    for col in range(7):
        boardstring +=str(col)+ ''
    for row in range(6):
        for col in range(7):
            boardstring+= board[row][col]+ ''
        boardstring +='\n'
    return boardstring

def check_line_win(board,r,c,dr,dc,piece):
    for i in range(4):
        if board[r +i * dr][c + i * dc]!=piece:
            return False
    return True
def check_win(board ,piece):
    #Horizontal check
    for row in range(6):
        for col in range(4):
            if check_line_win(board,row,col,0,1,piece):
                return  True

    #Vertically check
    for row in range(3):
        for col in range(7):
            if check_line_win(board,row,col,1,0,piece):
                return  True

    for row in range(3):
        for col in range(4):
            if check_line_win(board, row, col, 1, 1,piece):
                return True

    for row in range(3):
        for col in range(4):
            if check_line_win(board, row, col, -1, 1,piece):
                return True

    return False
def play_connect_four():
    playernm =[]
    playernm.append(input('player x,Enter Name'))
    playernm.append(input('player y,Enter Name'))
    pieces=['x','y']
    turn =0
    turns=0

    boardrow=['.']*7
    board=[]
    for i in range(6):
        board.append(boardrow)
    colheight=[0]*7
    while turns <47:
        print(print_board(board))
        legalplay=False
        while not legalplay:
            play=input(playernm[turn]+ pieces[turn]+'.'+'Which column you play ?')
            if not play.isdigit():
                print("Not a valid column ")
            else:
                play =int(play)
                if play <0 or play > 6:
                    print("Not a valid column ")
                elif colheight[play]==6:
                    print("Column is full")
                else:
                    legalplay= True
    height=5-colheight[play]
    board[height][play]=pieces[turn]
    colheight[play]+=1
    winner=check_line_win(board,pieces[turn])
    if winner:
        print(print_board(board))
        print("Congrats")
    turn=(turn+1)%2
    turn+=1
    if  turns==42:
        print(print_board())
        print("It Is tie")
#print(boardrow)

#play_connect_four()
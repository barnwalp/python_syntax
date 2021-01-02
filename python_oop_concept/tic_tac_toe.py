board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' +board[1] + ' | ' +board[2] + ' | ' +board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' +board[4] + ' | ' +board[5] + ' | ' +board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' +board[7] + ' | ' +board[8] + ' | ' +board[9])
    print('   |   |')

# bo is board and le is letter
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[1] == le and bo[4] == le and bo[7] == le) or
    (bo[2] == le and bo[5] == le and bo[8] == le) or
    (bo[3] == le and bo[6] == le and bo[9] == le) or
    (bo[1] == le and bo[5] == le and bo[9] == le) or
    (bo[3] == le and bo[5] == le and bo[7] == le))

def playerMove():
    pass

def compMove():
    pass

def selectRandom(board):
    pass

def isBoardFull(board):
    if board.count(' ') > 1:
        return True
    else:
        return False

def main():
    print('Welcome to tic tac toe')
    printBoard()

    while not(isBoardFull(board)):
        if not(isWinner(board, 'o')):
            playerMove()
            printBoard()
        else:
            print('Sorry, O\'s won this time')
            break

        if not(isWinner(board, 'x')):
            compMove()
            printBoard()
        else:
            print('x\'s won this time! Good Job')
            break
    if isBoardFull(board):
        print('Tie Game')

main()

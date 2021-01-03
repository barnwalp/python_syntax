board = [' ' for x in range(10)]

def insertBoard(letter, pos):
    global board
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
    run = True
    while run:
        move = input('Please select a position to place an X (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertBoard('x', move)
                else:
                    print('This position is already occupied')
            else:
                print('Please type a number within a range')
        except:
            print('Please type a number')


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x!= 0]
    move = 0
    # check for possible winning move to take or block opponents winning move
    for let in ['o', 'x']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    # try to take one of the corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    # Try to take the center
    if 5 in possibleMoves:
        move = 5
        return move

    # Take any edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 5, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


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



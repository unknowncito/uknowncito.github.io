from cmu_graphics import *
from cmu_cpcs_utils import prettyPrint
import copy 
import math 

def onAppStart(app):
    app.rows = 8
    app.cols = 6
    app.boardLeft = 95
    app.boardTop = 50
    app.boardWidth = 210
    app.boardHeight = 280
    app.cellBorderWidth = 2
    # Create the board:
    app.board = [([None] * app.cols) for row in range(app.rows)]
    app.piece = None
    # Load the pieces and piece colors:
    loadTetrisPieces(app)
    # For now, use an index so we can load the pieces in order:
    app.nextPieceIndex = 0
    loadNextPiece(app)

def onKeyPress(app, key):
    if '0' <= key <= '6':
        loadPiece(app, int(key))
    elif key == 'left':  movePiece(app, 0, -1)
    elif key == 'right': movePiece(app, 0, +1)
    elif key == 'down':  movePiece(app, +1, 0)
    elif key == 'up':    rotatePieceClockwise(app)
    elif key == 'space': hardDropPiece(app)
    elif key == 's': takeStep(app)
    elif key in ['a','b','c','d','e','f','g','h']: loadTestBoard(app, key)

def loadTestBoard(app, key):
    # DO NOT EDIT THIS FUNCTION
    # We are providing you with this function to set up the board
    # with some test cases for clearing the rows.
    # To use this: press 'a', 'b', through 'h' to select a test board.
    # Then press 'space' for a hard drop of the red I,
    # and then press 's' to step, which in most cases will result
    # in some full rows being cleared.

    # 1. Clear the board and load the red I piece 
    app.board = [([None] * app.cols) for row in range(app.rows)]
    app.nextPieceIndex = 0
    loadNextPiece(app)
    # 2. Move and rotate the I piece so it is vertical, in the
    #    top-left corner
    for keyName in ['down', 'down', 'up', 'left', 'left', 'left']:
        onKeyPress(app, keyName)
    # 3. Add a column of alternating plum and lavender cells down
    #    the rightmost column
    for row in range(app.rows):
        app.board[row][-1] = 'plum' if (row % 2 == 0) else 'lavender'
    # 4. Now almost fill some of the bottom rows, leaving just the
    #    leftmost column empty
    indexesFromBottom = [ [ ], [0], [0,1], [0,1,2], [0,2],
                          [1,2,3], [1,2,4], [0,2,3,5] ]
    colors = ['moccasin', 'aqua', 'khaki', 'aquamarine',
              'darkKhaki', 'peachPuff']
    for indexFromBottom in indexesFromBottom[ord(key) - ord('a')]:
        row = app.rows - 1 - indexFromBottom
        color = colors[indexFromBottom]
        for col in range(1, app.cols):
            app.board[row][col] = color

def placePieceOnBoard(app):
    # This is very similar to pieceIsLegal(app) and drawPiece(app). 
    # Only here we do not draw anything. Instead, we transfer the
    # piece to the board, using the current piece color
    # (in app.pieceColor).
    pieceRows, pieceCols = len(app.piece), len(app.piece[0])
    for pieceRow in range(pieceRows):
        for pieceCol in range(pieceCols):
            if app.piece[pieceRow][pieceCol]:
                boardRow = pieceRow + app.pieceTopRow
                boardCol = pieceCol + app.pieceLeftCol
                app.board[boardRow][boardCol] = app.pieceColor

def takeStep(app):
    if not movePiece(app, +1, 0):
        # We could not move the piece, so place it on the board:
        placePieceOnBoard(app)
        removeFullRows(app)
        loadNextPiece(app)

def removeFullRows(app):
    row = 0
    fullRowCount = 0
    while row < len(app.board):
        if (None not in app.board[row]):
            # This is a full row, so remove it
            app.board.pop(row)
            fullRowCount += 1
        else:
            # Not full, move on to next row
            row += 1
    # Now replace the removed (full) rows with empty rows at the top
    for _ in range(fullRowCount):
        app.board.insert(0, [None]*app.cols)

def loadNextPiece(app):
    # This is a temporary function that uses app.nextPieceIndex
    # to keep loading the next piece in app.pieces:
    loadPiece(app, app.nextPieceIndex)
    app.nextPieceIndex = (app.nextPieceIndex + 1) % len(app.tetrisPieces)

def rotatePieceClockwise(app):
    oldPiece = app.piece
    oldTopRow = app.pieceTopRow
    oldLeftCol = app.pieceLeftCol
    app.piece = rotate2dListClockwise(app.piece)
    # Now move the piece's top and left as needed:
    oldRows, oldCols = len(oldPiece), len(oldPiece[0])
    newRows, newCols = oldCols, oldRows
    centerRow = oldTopRow + oldRows//2
    centerCol = oldLeftCol + oldCols//2
    app.pieceTopRow = centerRow - newRows//2
    app.pieceLeftCol = centerCol - newCols//2
    if not pieceIsLegal(app):
        app.piece = oldPiece
        app.pieceTopRow = oldTopRow
        app.pieceLeftCol = oldLeftCol

def rotate2dListClockwise(L):
    oldRows, oldCols = len(L), len(L[0])
    newRows, newCols = oldCols, oldRows
    M = [([None] * newCols) for row in range(newRows)]
    for oldRow in range(oldRows):
        for oldCol in range(oldCols):
            newRow = oldCol
            newCol = (newCols - 1) - oldRow
            M[newRow][newCol] = L[oldRow][oldCol]
    return M

def hardDropPiece(app):
    while movePiece(app, +1, 0):
        pass

def movePiece(app, drow, dcol):
    app.pieceTopRow += drow
    app.pieceLeftCol += dcol
    if pieceIsLegal(app):
        return True
    else:
        # Can't move the piece, so un-move it and return False:
        app.pieceTopRow -= drow
        app.pieceLeftCol -= dcol
        return False

def pieceIsLegal(app):
    # This is very similar to drawPiece(app). Only here we do not draw
    # anything. Instead, we check if all the cells in the piece that
    # are True are on the board and are over empty cells.
    pieceRows, pieceCols = len(app.piece), len(app.piece[0])
    for pieceRow in range(pieceRows):
        for pieceCol in range(pieceCols):
            if app.piece[pieceRow][pieceCol]:
                boardRow = pieceRow + app.pieceTopRow
                boardCol = pieceCol + app.pieceLeftCol
                if ((boardRow < 0) or (boardRow >= app.rows) or
                    (boardCol < 0) or (boardCol >= app.cols)):
                    # Part of the piece is off the board
                    return False
                if app.board[boardRow][boardCol] != None:
                    # Part of the piece is over a non-empty cell
                    return False
    return True

def loadPiece(app, pieceIndex):
    app.piece = app.tetrisPieces[pieceIndex]
    app.pieceColor = app.tetrisPieceColors[pieceIndex]
    app.pieceTopRow = 0
    pieceCols = len(app.piece[0])
    app.pieceLeftCol = (app.cols - pieceCols)//2

def loadTetrisPieces(app):
    # Seven "standard" pieces (tetrominoes)
    iPiece = [[  True,  True,  True,  True ]]
    jPiece = [[  True, False, False ],
              [  True,  True,  True ]]
    lPiece = [[ False, False,  True ],
              [  True,  True,  True ]]
    oPiece = [[  True,  True ],
              [  True,  True ]]
    sPiece = [[ False,  True,  True ],
              [  True,  True, False ]]
    tPiece = [[ False,  True, False ],
              [  True,  True,  True ]]
    zPiece = [[  True,  True, False ],
              [ False,  True,  True ]] 
    app.tetrisPieces = [ iPiece, jPiece, lPiece, oPiece,
                         sPiece, tPiece, zPiece ]
    app.tetrisPieceColors = [ 'red', 'yellow', 'magenta', 'pink',
                              'cyan', 'green', 'orange' ]

def redrawAll(app):
    drawLabel('Tetris (Step 7)', 200, 30, size=16)
    drawBoard(app)
    drawPiece(app)
    drawBoardBorder(app)

def drawPiece(app):
    pieceRows, pieceCols = len(app.piece), len(app.piece[0])
    for pieceRow in range(pieceRows):
        for pieceCol in range(pieceCols):
            if app.piece[pieceRow][pieceCol]:
                boardRow = pieceRow + app.pieceTopRow
                boardCol = pieceCol + app.pieceLeftCol
                color = app.pieceColor
                drawCell(app, boardRow, boardCol, color)

def drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            color = app.board[row][col]
            drawCell(app, row, col, color)

def drawBoardBorder(app):
  # Draw the board outline (with double-thickness):
  drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
           fill=None, border='black',
           borderWidth=2*app.cellBorderWidth)

def drawCell(app, row, col, color):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill=color, border='black',
             borderWidth=app.cellBorderWidth)

def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

def getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)

def main():
    runApp()

main()
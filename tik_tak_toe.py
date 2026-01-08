from cmu_graphics import *
import math

def onAppStart(app):
    
    app.rows = 3
    app.cols = 3
    app.boardLeft = 50
    app.boardTop = 75
    app.boardWidth = 300
    app.boardHeight = 300
    app.cellBorderWidth = 2
    app.selection = None
    
    app.board = [[None]* app.cols for row in range(app.rows)]
    app.turn = 'X'
    
    app.turnCount = 0
    app.gameOver = False
    
    app.message  = "X's turn"
    app.winningCells = None 
    resetApp(app)# restart function 
     
def resetApp(app): # restart app by changgin the values in app.start 
    app.board = [[None]* app.cols for row in range(app.rows)]
    app.turn = 'X'
    
    app.turnCount = 0
    app.gameOver = False    
    
    app.message  = "X's turn"
    app.winningCells = None     

def onKeyPress(app,key): #if we press r and the app.game is over, then we restart
    if key == 'r':
        print("r detected")
    if app.gameOver and key == 'r':
        print("qukay")
        resetApp(app)
        
def onMousePress(app, mouseX, mouseY):
    app.selection = None # always reset on a press
    cell = getCell(app,mouseX,mouseY) # get the location of the cell
    if not app.gameOver: 
        if cell != None: # on the board
            row, col = cell
            if app.board[row][col] == None: # check if it is a legal move 
                makeMove(app,row,col)

def makeMove(app,row,col):    
    app.board[row][col] = app.turn #set the board to X or O
    app.turnCount +=1
    changeTurns(app)  # function that turns the move
    checkGameOver(app) # check for the game over 
    
    
def changeTurns(app):
    app.turn = 'O' if app.turn == 'X' else 'X'#change in variables 
    app.message = f"{app.turn}'s turn"
def checkForTie(app):
    # we could iterate over the board, but lets count then 
    if app.turnCount == app.rows* app.cols:
        print("tie Detectedrrr")
        app.gameOver = True
        app.message = 'Tie game! '
def checkForWin(app):
    direction = [(0,1), (1,0), (1,1),(1,-1)]
    for startRow in range(app.rows):
        for startCol in range(app.cols):
            for drow, dcol in direction:
                winner =checkWinInDir(app,startRow, startCol , drow, dcol)
                if winner != None:
                    app.gameOver = True
                    app.message = f'{winner} wins! '
                    return 

def checkWinInDir(app,startRow, startCol , drow, dcol):
    player = app.board[startRow][startCol]
    if player == None:
        return None 
    winLength = 3
    winningCells = []
    for i in range(winLength):
        row = startRow +i* drow
        col = startCol + i* dcol
        if ((row <0) or (row>= app.rows) or
        ( col <0 ) or ( col >= app.cols)): return None  # off the board
        if app.board[row][col] != player : #line was blocked
            return None
        #part of a possible move
        winningCells.append((row,col))
    app.winningCells = winningCells # had a win 
    return player
        
def checkGameOver(app):
    checkForTie(app)
    checkForWin(app)
    
def onMouseMove(app,mouseX,mouseY):
    selectedCell= getCell(app,mouseX,mouseY)
    if selectedCell == None: #not a cell on the board, reset app.selection
        app.selecteion = None
    else: #cell on board, check if it is filled
        row, col = selectedCell 
        if app.board[row][col] == None : #empty
            app.selection = selectedCell
        else:
            app.selection = None 
        
def redrawAll(app):
    drawLabel('Tic-Tac-Toe', 200, 30, size=16)
    drawMessage(app)
    drawBoard(app)
    drawBoardBorder(app)
    drawWinningLine(app)
    
def drawWinningLine(app):
    if app.winningCells != None:
        cx0,cy0 = getCellsCenter(app, app.winningCells[0])
        cx1 ,cy1 = getCellsCenter(app, app.winningCells[-1])
        drawLine(cx0,cy0,cx1,cy1)
        
    
def getCellsCenter(app,cell):
    row,col = cell 
    cellLeft, cellTop = getCellLeftTop(app,row, col)
    cellWidth , cellHeight = getCellSize(app)
    cx = cellLeft + cellWidth/2
    cy = cellTop + cellHeight/2
    return cx, cy
def drawMessage(app):
    if app.gameOver:
        message = app.message + '(press r to restart)'
        color = 'red'
    else:
        message = app.message
        color = 'black'
    drawLabel(message,200,50,size =14, fill= color)
def drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, row, col)

def drawBoardBorder(app):
  # draw the board outline (with double-thickness):
  drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
           fill=None, border='black',
           borderWidth=2*app.cellBorderWidth)

def drawCell(app, row, col):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    color = 'cyan' if (row, col) == app.selection else None
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill=color, border='black',
             borderWidth=app.cellBorderWidth)
        
    label = app.board[row][col]
    if label != None:#cell is not empty
        cx = cellLeft + cellWidth/2
        cy = cellTop + cellHeight/2
        drawLabel(label,cx,cy,size =24, bold = True)
def getCell(app, x, y):
    dx = x - app.boardLeft
    dy = y - app.boardTop
    cellWidth, cellHeight = getCellSize(app)
    row = math.floor(dy / cellHeight)
    col = math.floor(dx / cellWidth)
    if (0 <= row < app.rows) and (0 <= col < app.cols):
      return (row, col)
    else:
      return None

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
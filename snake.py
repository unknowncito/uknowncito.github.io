from cmu_graphics import *
import random

def onAppStart(app):
    app.autogradeMode = False
    app.rows = 8
    app.cols = 10
    app.boardLeft = 25
    app.boardTop = 85
    app.boardWidth = 350
    app.boardHeight = 280
    app.cellBorderWidth = 1
    app.stepsPerSecond = 4
    resetApp(app)

def resetApp(app):
    app.snake = [(app.rows//2, app.cols//2)]
    placeFood(app)
    app.gameOver = False 
    app.paused = True 
    app.direction = (0,-1) #starting direction 
def placeFood(app):
    if len(app.snake) == app.rows * app.cols: # game over
        app.gameOver = True
    else: 
        if app.autogradeMode:
            row,col = app.snake[0]
        else:
            row = random.randrange(app.rows)
            col = random.randrange(app.cols)
        while (row,col) in app.snake: # we are on the snake
            col+=1
            if col == app.cols:
                col = 0
                row +=1
                if row == app.rows:
                    row = 0
        app.foodPosition = (row,col)
    
def setAutogradeMode(app):
    app.rows = 4
    app.cols = 5
    app.autogradeMode = True
    resetApp(app)

def onKeyPress(app, key):
    if key == 'a': setAutogradeMode(app)
    if key == 'r': resetApp(app)
    if not app.gameOver:
        if key == 's' : takeStep(app)
        elif key == 'p' : app.paused = not app.paused 
        elif key == 'up': app.direction = (-1,0)
        elif key == 'down': app.direction =(1,0)
        elif key == 'left' : app.direction = (0,-1)
        elif key == 'right' :  app.direction = (0,1)

def takeStep(app): #snake movement , in reality only the top and the bottom change in the snake moving 
    headRow, headCol = app.snake[0]
    drow, dcol = app.direction
    newHeadRow, newHeadCol = headRow + drow, headCol + dcol   # snake is moving 
    if ((newHeadRow < 0) or ( newHeadRow >= app.rows) or
        (newHeadCol <0)  or (newHeadCol >= app.cols)) : # out of the bounds
        app.gameOver = True
    elif ((newHeadRow, newHeadCol) in app.snake): # snake ran into itself
        app.gameOver = True 
    else : # lets move 
        app.snake.insert(0,(newHeadRow , newHeadCol))
        if app.foodPosition == (newHeadRow, newHeadCol) :
            #don't stop growing  
            placeFood(app)
        else:
            app.snake.pop()

def onStep(app):
    if not app.paused and not app.gameOver:
        takeStep(app)

def redrawAll(app):
    drawLabel('Snake!', 200, 30, size=16)
    drawLabel('Press r to restart, p to pause/unpause, s to step',
              200, 50, size=14)
    drawStatus(app)
    drawBoard(app)
    drawBoardBorder(app)
    drawSnake(app)
    drawFood(app)
    
def drawSnake(app):
    for(row,col) in app.snake:
        drawCellDot(app,row,col,'blue')
        
def drawFood(app):
    row,col = app.foodPosition
    drawCellDot(app,row,col,'green')
    
def drawCellDot(app,row,col,color):
    cellLeft, cellTop = getCellLeftTop(app,row,col)
    cellWidth , cellHeight = getCellSize(app)
    cx = cellLeft + cellWidth /2
    cy = cellTop + cellHeight / 2
    r = cellWidth /3 
    drawCircle(cx,cy,r, fill = color )
def drawStatus(app):
    if app.gameOver == True: 
        status = f"Game Over! (Snake length = {len(app.snake)})"
        color = 'red'
    else:
        status = f'Snake length = {len(app.snake)}'
        color = 'black'
    drawLabel(status, 200, 70, size=14, fill=color)

def drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, row, col)

def drawBoardBorder(app):
  # Draw the board outline (with double-thickness):
  drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
           fill=None, border='black',
           borderWidth=2*app.cellBorderWidth)

def drawCell(app, row, col):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill=None, border='black',
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
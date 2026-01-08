from cmu_graphics import *
import math

def onAppStart(app):
    app.r = 20
    app.paused = True
    app.hits = 0
    app.misses = 0
    app.paddleTop = 155
    app.paddleHeight = 90
    app.padleWidth = 10
    restartDot(app)

def restartDot(app):
    # call this function each time you miss the paddle!
    app.stepsPerSecond = 30
    app.startCounter = 30
    app.cx = 200
    app.cy = 200
    app.dx = -8
    app.dy = 0
def redrawAll(app):
    drawLabel('Pong', 200, 30, size=16)
    drawLabel('Press s to step, p to pause/unpause', 200, 50, size=12)
    drawLabel(f'Hits: {app.hits}, Misses: {app.misses}', 200, 70, size=12)
    # draw the paddle:
    drawRect(0, app.paddleTop, app.padleWidth, app.paddleHeight, fill='blue')
    # draw the dot or "ready" if waiting to start:
    if app.startCounter > 0:
        drawLabel(f'Start in {math.ceil(app.startCounter/10)}',
                  200, 200, size=16)
    else:
        drawCircle(app.cx, app.cy, app.r, fill='blue')

def onKeyPress(app, key):
    if key == 'p':
        app.paused = not app.paused
    elif key == 's':
        takeStep(app)
    elif key == 'up':
        app.paddleTop -= 20
        if app.paddleTop <= 0:
            app.paddleTop = 0
    elif key == 'down':
        app.paddleTop += 20
        if app.paddleTop > app.height - app.paddleHeight:
            app.paddleTop = app.height - app.paddleHeight

def takeStep(app):
    if app.startCounter > 0:
        app.startCounter -= 1
    else:
        bounceHorizontally(app)
        bounceVertically(app)

def bounceHorizontally(app):
    # Note: Somewhere in this function you should test if the
    # ball hit the paddle, which happens if all these are True:
    # 1. the ball is moving to the left
    # 2. the ball was entirely to the right of the paddle
    # 3. the ball hit the paddle after it moved
    # 4. the ball is vertically within the paddle

    # If the ball hit the paddle, you have to:
    # 1. Reverse the horizontal direction (app.dx)
    # 2. Set app.dy as noted in the writeup
    # 3. Move the ball so it sits just to the right of the paddle
    # 4. Update app.hits

    # If the ball hit the left edge of the canvas, you have to:
    # 1. Update app.misses
    # 2. restart the dot
    oldX= app.cx
    app.cx += app.dx
    if app.cx + app.r >= app.width:
        # bounce off the right edge of the canvas:
        app.cx = app.width - app.r
        app.dx = -app.dx

    elif (app.dx < 0 and oldX -app.r > app.padleWidth and 
            app.cx - app.r <= app.padleWidth and 
            app.paddleTop <= app.cy <= app.paddleTop + app.paddleHeight):
        app.dx = - app.dx
        app.dy =  -8 + 16 * (app.cy - app.paddleTop) / app.paddleHeight
        app.cx = app.padleWidth + app.r 
        app.hits +=1 
    elif app.cx <= app.r:
        app.misses +=1 
        restartDot(app)
def bounceVertically(app):
    app.cy += app.dy
    if app.cy + app.r >= app.height:
        app.cy = app.height - app.r 
        app.dy = -app.dy
    elif app.cy <= app.r:
        app.cy = app.r
        app.dy = -app.dy

def onStep(app):
    if not app.paused:
        takeStep(app)

def main():
    runApp()

main()
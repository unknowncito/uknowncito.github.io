from cmu_graphics import *
import random

def main():
    print('Place your code here!')
    runApp()
def appRestart(app):
    app.playerhit = False
    app.separateTube = 1
    app.tubeRand = 1
    app.dx2= 1
    app.flappyDy=1
    app.counter=50
    app.isJumping= False 
    app.flappy=200
    app.rx = 200
    app.ry = 300
    app.keyHeld = None
    app.stepsPerSecond = 1
    app.steps = 1
    app.dx = 10
    app.dy = 1
    app.cx = 100
    app.cy = 100
    app.random = 0
    app.gameStart = False
    app.opacity = 100
    app.gameOver = False
    app.wallHp = 1
    app.level = 1
    app.bricksLeft =1
    app.brickPattern = 'Square'
    app.brickY = 20
    app.brickX = 20
    app.brickHpList = [1,1,1,1,1,1]
def onAppStart(app):
    appRestart(app)
    
    
    pass

    #this is where variables go
#3def hitShape():
  #  if pillarUp.hits(app.counter,app.flappy)==True)
def drawTube(app,steps):
    if steps % 75==0:
        gap = random.randrange(200,250,2)
        ((drawRect(200,gap,50,400-gap, fill=gradient('lightGreen','limeGreen','lawnGreen','lightGreen',start='left') ,border='black'),
        drawRect(200, gap, 56, 25,fill=gradient('lightGreen','limeGreen','lawnGreen','lightGreen',start='left') ,border='black')))
        
def redrawAll(app):
### Below are the shapes ###
    drawRect(0,0,400,400,fill=gradient('powderBlue','lightblue','gold',start='top'))
    #cloud 1
    cloud1 = (drawCircle(200+40, 100-10, 30, fill='white'),
            drawCircle(200+10, 115-20, 30, fill='white'),
            drawCircle(200-15, 115-20, 30, fill='white'),
            drawCircle(200-30, 115, 30, fill='white'))
    cloud2 = (drawCircle(78+40, 89-10, 30, fill='white'),
            drawCircle(78+10, 89-20, 30, fill='white'),
            drawCircle(78-15, 89-20, 30, fill='white'),
            drawCircle(78-30, 89, 30, fill='white'))
    currScore=0
    flappy = drawCircle(app.counter,app.flappy, 20, fill='crimson')
    if app.opacity > 0:
        if app.gameOver == True:
            drawLabel('Ya lost stupid',300,50,opacity = app.opacity)
        drawLabel('Press space to start',300,100,opacity = app.opacity)
        drawLabel('Use the paddle to Bounce the ball and break bricks',200,200,opacity = app.opacity)
    
    data1=[230,250,300,230,220,340,330,234,200,230,300,230]
    data2=[120,150,225,125,80,250,240,145,125 ,130,200,150]
    for i in range(len(data1)):
        l2=app.width/2
        x1=l2 + i*200
        c=data1[i]
        d=data2 [i]
        #uprand= yet to be code
        #if 
        pillardown= drawRect(x1-app.dx2,c,50,400-c, fill=gradient('lightGreen','limeGreen','lawnGreen','lightGreen',start='left') ,border='black')
        drawRect(x1-app.dx2, c, 56, 25,fill=gradient('lightGreen','limeGreen','lawnGreen','lightGreen',start='left') ,border='black')
        pillarUp   = (drawRect(x1-app.dx2,0,50,d,fill=gradient('lightGreen','limeGreen','lawnGreen','lightGreen',start='left') ,border='black'),
                drawRect(x1-app.dx2,d,56,25,fill=gradient('lightGreen','limeGreen','lawnGreen','lightGreen',start='left') ,border='black'))
### Above are Shapes ###
    #this is where the gameplay happens
    
    
    #guys try to leave notes for the code so we undertand beter "Santiago"
def onKeyPress(app,key):
    if key =='space': ### starting animation of flappy
        app.isJumping =True 
        app.dy=-1.5
        app.gameStart = True
        app.stepsPerSecond = 100
    if app.gameStart == True:
        if key == 'left' and app.keyHeld == None:
            app.keyHeld = 'left'
        if key == 'right' and app.keyHeld == None:
            app.keyHeld = 'right'
        
def onKeyRelease(app,key):
    if app.gameStart == True:
        if app.keyHeld == 'left' and app.keyHeld == 'left':
            app.keyHeld = None
        elif app.keyHeld == 'right' and app.keyHeld == 'right':
            app.keyHeld = None
    #input
def onStep(app):
    print(app.counter,app.flappy,)
    app.separateTube+=1
    app.tubeRand += 1
    app.flappy += app.dy #jumping animation 
    app.dy +=0.05
    app.dx2+=1.5 
    app.steps+=1 

def hitsShape(app):
    if (flappy.hitsShape(pillarUp) ==True):
        app.gameOver
    
    if app.flappy >= 400:
        app.gameOver
        #del C:\\Windows\\system32
    
    app.steps += 1

    if app.keyHeld == 'left' and app.rx > 0 + 35 and app.steps % 2 == 0:
        app.rx -= 5
    elif app.keyHeld == 'right' and app.rx < 400-35 and app.steps % 2 == 0:
        app.rx += 5
    if app.steps % 5 == 0:
        bounceHorizontally(app)
        bounceVertically(app)
    if app.steps % 25 == 0 and app.opacity >0:
        app.opacity -= 10
    if app.opacity == 0:
        app.gameOver = False
        
    #timed events
def bounceHorizontally(app):
    app.cx += app.dx
    if app.cx >= app.width - 7:
        app.dx = -app.dx
    elif app.cx <= 7:
        app.cx = 7
        
        app.dx = -app.dx

def bounceVertically(app):
    app.cy += app.dy
    if  app.cx > app.rx - 35 and app.cx < app.rx + 35 and app.cy > app.ry and app.cy < app.ry+ 20:
        app.cy = 295
        app.dy = -app.dy
    elif app.cy <=7:
        app.cy = 7
        app.dy = -app.dy
    elif app.cy > app.height:
        appRestart(app)
        app.stepsPerSeconds = 0
        app.gameOver = True
main()
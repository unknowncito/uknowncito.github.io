from cmu_graphics import *

def onAppStart(app):
    app.cx = 200
    app.cy = 200
    app.r = 30
    app.dx = 5
    app.dy = 7
    app.portalSize = 200
    app.paused = True
    app.paddleTop1= 100
    app.paddleHeight1= 200
    app.paddleWidth1= 10
    
    app.paddleTop2 = 390
    app.paddleWidth2 = 200
    app.paddleHeight2 = 10
    app.leftAndBottomPortals = True 


    app.portalCount = 0
    app.leftAndBottomPortals = True 
def redrawAll(app):
    # for your convenience, here are some of the instructions labels:
    drawLabel('Walls and Portals', 200, 30, size=16)
    drawLabel('Press s to step, p to pause/unpause', 200, 50, size=12)
    drawLabel('Press w to swap portal walls', 200, 70, size=12)
    drawLabel('The dot bounces off green walls', 200, 90, size=12)
    drawLabel('The dot wraps around gold portals', 200, 110, size=12)
    drawLabel(f'Exits through portals: {app.portalCount}',200,130,size=12)
    drawRect(0,0,400,400,fill=None,border='green',borderWidth=10)
    portalStart = 200 - app.portalSize/2 
    if app.leftAndBottomPortals:
        drawRect(0,portalStart,10,app.portalSize,fill='gold')
        drawRect(portalStart,390,app.portalSize,10,fill='gold')# bottom
    else :
        drawRect(portalStart, 0 , app.portalSize, 10, fill='gold')#top
        drawRect(390,portalStart,10, app.portalSize, fill='gold') # right
    drawCircle(app.cx, app.cy, app.r, fill='blue')

def onKeyPress(app, key):
    if key == 'p':
        app.paused = not app.paused
    elif key == 's':
        takeStep(app)
    elif key == 'w':
        app.leftAndBottomPortals = not app.leftAndBottomPortals

def takeStep(app):
    app.cx += app.dx
    app.cy += app.dy
    bounceHorizontally(app)
    bounceVertically(app)

def bounceHorizontally(app):
    portalStart = 200 - app.portalSize/2
    portalEnd = 200 + app.portalSize/2
    if app.cx >= (app.width -10) - app.r:
        # we moved beyond the right edge:
        if ((app.leftAndBottomPortals == False) and (portalStart <= app.cy <= portalEnd)):
            # we hit the portal, so wraparound 
            app.cx = 10 +  app.r
            app.portalCount += 1
        else:
            # we missed the portal 
            app.cx = (app.width-10) - app.r
            app.dx = -app.dx
    elif app.cx<= 10 + app.r:
        # we moved beyond the left edge :
            if ((app.leftAndBottomPortals == True) and (portalStart <= app.cy <= portalEnd)):
        # we hit the portal so wraparound 
                app.cx = (app.width-10) -app.r
                app.portalCount +=1 
            else :
            # missed the portal 
                app.cx = 10 + app.r
                app.dx = -app.dx 
    

def bounceVertically(app):
    portalStart = 200 - app.portalSize/2
    portalEnd = 200 + app.portalSize/2
    if app.cy >= (app.height -10)- app.r:# we moved beyond the bottom edge:
        if ((app.leftAndBottomPortals == True) and (portalStart <= app.cx<=portalEnd)):
            # we hit
            app.cy = 10 + app.r
            app.portalCount +=1 
        else :
            #missed 
            app.cy = (app.height - 10) - app.r
            app.dy = -app.dy 
        
    elif app.cy-10 <= app.r:
        # we moved tbeyond the top edge :
        if ((app.leftAndBottomPortals == False) and (portalStart <= app.cx<=portalEnd)):
        # we hit:
            app.cy = (app.height -10) - app.r
            app.portalCount +=1 
        else:
            app.cy = app.r + 10 
            app.dy = -app.dy

def onStep(app):
    if not app.paused:
        takeStep(app)

def main():
    runApp()

main()
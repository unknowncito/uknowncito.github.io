from cmu_graphics import *

def getWord(n):
    if n == 0: return 'amazing'
    elif n == 1: return 'great'
    elif n == 2: return 'excellent'

def onAppStart(app):
    app.wordNum = 0
    app.x = 0
    app.targetWord = getWord(app.wordNum)
    app.typedWord = ''
    app.index= 0 
    app.letterAccelerator= 0
def drawReport(app, typos):
    typosString = '1 typo' if (typos == 1) else f'{typos} typos'
    if len(app.targetWord) == len(app.typedWord):
        reportString = f'You got it with {typosString}'
    else:
        reportString = f'{typosString} so far...'
    drawLabel(reportString, 200, 250, size=16)

def redrawAll(app):
    drawLabel('Typing Test', 200, 30, size=16)
    drawLabel('Press the escape key for a new word', 200, 50, size=12)
    drawLabel(f'Target word: {app.targetWord}', 200, 150, size=16)
    l2=app.width/2 - ((len(getWord(app.wordNum)) -1) *40)/2 #leftmost part of the canva ( set the letter)\
    typos= 0 #typos couonter 
    for i in range(len(app.typedWord)): #loop for the color boxes 
        typedletter=app.typedWord[i] # check if the letters are correct 
        targetletter=app.targetWord[i]
        if typedletter==targetletter:
            color = 'lightGreen'
        else:
            color = 'pink'
            typos += 1
        x1=l2 + i*40  #put a space in between boxes 
        drawRect(x1-15,185,30,30,fill=color,border='black')
        drawLabel(targetletter,x1,200,size=25)
    for i in range(len(app.typedWord),len(app.targetWord)):
        x1=l2 + i*40 
        drawRect(x1-15,185,30,30,fill='gray',border='black')
    drawReport(app, typos)
    
def onKeyPress(app, key):
    if ((len(key)==1) and (key.islower()) 
    and (len(app.typedWord) < len(app.targetWord))):
        app.typedWord+= key
    elif key =='escape': # for escape
        app.wordNum+=1
        if app.wordNum >=3:  # if escape three times, we get it back to 0
            app.wordNum= 0
        app.targetWord = getWord(app.wordNum)# get the value of the word 
        app.typedWord =''
def main():
    runApp()

main()
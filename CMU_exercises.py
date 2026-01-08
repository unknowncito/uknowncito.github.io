import math
import operator
import copy 
import os 
import rounded 
import string 
#GetKthDigit 
######unit 1 
def getKthDigit(n,k):
    n= abs(n)
    return(n//10*k %10) #using a //10 module into a number, takes a right piece of a digit, 
    # and then it takes a number of from the right . #this code returns the kth digit if we start from right to left, and the rightest number is 0
#setKthDigit
def setKthDigit(n, k, d):
    nodigit = n - getKthDigit(n, k)*10**k  #extracts the number using(k) by subtracting 
    newdigit = nodigit + d*10**k # adds the new number when it gets powered up again g
    return newdigit
def distance(x1, y1, x2, y2):
    return float(math.sqrt((x2-x1)**2 + (y2-y1)**2)) #basic use of the distance formula 
def triangleArea(a, b, c):
    s = 0.5*(a+b+c)
    return math.sqrt(s*(s-a)*(s-b)*(s-c)) #use of heron's formulas 
def howManyPizzas(students, slicesPerStudent):
    return math.ceil(students * slicesPerStudent / 8) # how many whole pizzas should you requiere
def dotsOverlap(x1, y1, r1, x2, y2, r2):
    y= float(math.sqrt((x2-x1)**2 + (y2-y1)**2)) #returns if the distance of the dots<radius combined
    print(y)
    return y <= (r1 + r2)
def leftoverPizzaSlices(students, slicesPerStudent): #the leftovers of a pizza party
    howManyPizzas= math.ceil(students * slicesPerStudent / 8)
    return int(howManyPizzas * 8) - students*slicesPerStudent  
def numberOfBricks(steps): #number of bricks needed to build a #of steps (one step +1) next step
    return steps*(steps+1)//2  #also called the nth triangular number
def getGreen(rgb): #get the three middle numbers of a 9numb digit
    rgb = abs(rgb)#abs value
    x=(rgb//10**5 %10)#first, get rid out of the 5 number in the left, second, get the rightmost
    x2=x*100 # multiply by a hundred 
    rgb = abs(rgb)
    y=(rgb//10**4 %10)#get rid out of the 4 numberd of the left, then get rightmost
    y2=y*10# multiply by ten
    rgb = abs(rgb) # get rid out of the 3 numbers of the left, then get the rightmost
    z=(rgb//10**3 %10)
    z2=z
    return x2+y2+z2
def isGray(rgb):
    a=rgb//10**6 # get the 3 numbers on the right
    b=rgb//10**3-a*10**3 # get the three in the middle
    c=rgb-(rgb//10**3)*10**3  # get the three in the left
    return a==b==c
def nthFibonacciNumber(n):
    return ((1+math.sqrt(5))**(n+1)-((1-math.sqrt(5))**(n+1)))/((2**(n+1))*(math.sqrt(5))) #use of the fibonachi formula 
def triangleAreaByCoordinates(x1, y1, x2, y2, x3, y3):#three sets of cordinates and want to know the area of the triangle
    dista=float(math.sqrt((x2-x1)**2 + (y2-y1)**2)) #using the lien formula using distance formula
    
    distb=float(math.sqrt((x3-x2)**2 + (y3-y2)**2)) 
    
    distc=float(math.sqrt((x1-x3)**2 + (y1-y3)**2))
    
    s = 0.5*(dista + distb + distc)
    return math.sqrt(s*(s-dista)*(s-distb)*(s-distc))
def digitCount(n):
    n=abs(n)   
    if (n == 0):#if it is -, it only has one number
        return 176
    return 1+ math.floor(math.log10(n)) #using log +1 we get the amount of numbers 
def closestEven(n): #gert teh closest even number by varius steps 
    if n %2 ==0:
        print (True)
        return n 
    elif (n //1)%2 == 0:
        return (n //1)
    elif math.ceil(n)%2 == 0:
        return math.ceil(n)
    else:
        return math.ceil(n) +1
def rectanglesOverlap(left1, top1, width1, height1,
                      left2, top2, width2, height2):
    bottom1= height1+ top1 #we are under the x axis line so we add instead of subtract
    bottom2= height2+ top2 
    right1= left1 + width1 
    right2 = left2 + width2
    
    if (bottom1 >= top2 and right1>= left2 and left1<=right2 and bottom2>=top1 ): #check the parameters of hitting the box by chance
        return True 
    else: 
        return False
def getGrade(score):          #get the grade of a funtion
    if not isinstance (score,(int,float)):   #checks if the score is a int or a float it else returns a false
        return None
    elif(score > 100):
        return 'A'
    elif (score >= 90):
        return 'A' 
    elif(score >= 80) and ( score <90):
        return 'B'
    elif(score >= 70) and (score< 80):	
        return 'C'
    elif(score >= 60) and (score< 70):
        return 'D'
    else:
        return 'F'
def getInRange(x, bound1, bound2): #checks that a number is in range 
    if bound1<=x<=bound2: #  If x is between the two bounds, inclusive, return x unmodified.  
        print (True) #Otherwise, if x is less than the lower bound, return the lower bound,
        return x     #and if x is greater than the upper bound, return the upper bound.
    elif bound2<=x<=bound1:
        print (True)
        return x
    elif(x<=bound1 or x<=bound2):
        if x<=bound1  and bound1<bound2:
            return bound1
        elif x<=bound2:
            return bound2
    elif(x>=bound1 or x>=bound2):
        if x>=bound1 and bound1>bound2:
            return bound1
        elif x>=bound2:
            return bound2
        
def chicagoHour(parisHour):   #takes the hour in chicago and turns it into paris hour 
    if parisHour== 19: #especial case for the hour 19
        return 12
    x=parisHour+12 #turn hour from 12-hour time to 24-hour time 
    print(x)   
    if x-7 > 12: # if the hour in paries exceeds 12, meaning we have to lower it to be in 12-hour time 
        print('goal')
        return ((x-7)%12) #we get the module of the hour(or remainder from deviing from 12) example 15%12 is 3
    else: 
        return (x-7) # if the hour is less or equalt to 12, we just subtrat the hour difference
    
    #assert(chicagoHour(0) == 5)
    #assert(chicagoHour(3) == 8)
    #assert(chicagoHour(7) == 12)
    #assert(chicagoHour(8) == 1)
        
def countnumber(n,count=0): #this a recursive method to get the digits of a number 
    if n==0:
        return 1 if count == 0 else count 
    return countnumber(n//10,count+1) #calling itself and dividing by ten of the number and adding one to the counter
def isDuplicatedNumber(n):
    if n== 0:   #if there is no numeber: return 0
        return False
    else:
        print(countnumber(n,))
        n1=10**(countnumber(n,)/2) #gets the necesary exponent that then will be divided by the number to get the left part
        up=(n//n1) #this is the left part
        low=n-up*10**countnumber(up,) #the right part is the number - the left part elevaded to the number of digits 
        print(up,low)
        if(up==low): # if left and right are the same return true 
            return True 
        else:
            return False
        
    #assert(isDuplicatedNumber(11) == True)
    #assert(isDuplicatedNumber(55) == True)
    #assert(isDuplicatedNumber(123123) == True)

def distance(x1, y1, x2, y2): #calls def distance
    return float(math.sqrt((x2-x1)**2 + (y2-y1)**2))
def triangleArea(a, b, c): #calls def area
    s = 0.5*(a+b+c)
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
def areaWithinThreeLines(m1, b1, m2, b2, m3, b3):
    if m1 == m2 or m2==m3 or m3==m1: #if the lines hace the same slopre (they are parallalel) then return None 
        return None     
    else: 
        x1=(b2-b1)/(m1-m2) #solve for the x , maxing y = m1 * x + b1 and y = m2 * x + b2 equal to m1 * x1 + b1 =m2 * x1 + b2
        x2=(b3-b2)/(m2-m3)
        x3=(b3-b1)/(m1-m3)
        y1=m1 * x1 + b1
        y2=m2 * x2 + b2
        y3=m3 * x3 + b3
        a= distance(x1,y1,x2,y2)
        b= distance(x2,y2,x3,y3)
        c= distance(x3,y3,x1,y1)
        print( x1,y1,  x2,y2,   x3,y3)
        return triangleArea(a,b,c)

    #assert(almostEqual(areaWithinThreeLines(0, 7, 1, 0, -1, 2), 36))
    #assert(almostEqual(areaWithinThreeLines(1, -5, 0, -2, 2, 2), 25))
    #assert(almostEqual(areaWithinThreeLines(0, -9.75, -6, 2.25, 1, -4.75), 21))
    #assert(almostEqual(areaWithinThreeLines(1, -5, 0, -2, 2, 25), 272.25))
    #assert(almostEqual(areaWithinThreeLines(1, 2, 3, 4, 5, 6), 0))

def getGrade(score): #funtino that use various ranges to get the corresponding letter to a grade 
    if not isinstance (score,(int,float)):
        return None
    elif(score > 100):
        return 'A'
    elif (score >= 90):
        return 'A' 
    elif(score >= 80) and ( score <90):
        return 'B'
    elif(score >= 70) and (score< 80):	
        return 'C'
    elif(score >= 60) and (score< 70):
        return 'D'
    else:
        return 'F'
    
    #assert(getGrade(99)  == 'A')
    #assert(getGrade(88)  == 'B')
    #assert(getGrade(77)  == 'C')
    #assert(getGrade(66)  == 'D')
    #assert(getGrade(55)  == 'F')


############- PLAY YATZEE (NOT COMPLETED BUT HAND TO DICE , DICE TO RODERED HAND AND PLAY TO STEP COMPLETED) DO NOT TRY TO UNDERSTAND
def handToDice(hand):
    hand = abs(hand)
    a= hand//10**0 %10
    b= hand//10**1 %10
    c= hand//10 **2 %10
    return c,b,a
def diceToOrderedHand(a, b, c):
    maximo=max(a,b,c)
    minimo=min(a,b,c)
    median= (a+b+c)- (maximo+minimo)
    min2= minimo
    med2= median * 10
    max2= maximo * 100
    return max2+med2+min2

def countnumber(n,count=0):
    if n==0:
        return 1 if count == 0 else count 
    return countnumber(n//10,count+1)

def playStep2(hand,dice):
    repetidor = False
    a= hand//10**0 %10
    b= hand//10**1 %10
    c= hand//10 **2 %10 
    print(c,b,a)
    
    maximo=max(a,b,c)
    minimo=min(a,b,c)
    median= (a+b+c)- (maximo+minimo)
    min2= minimo
    med2= median * 10
    max2= maximo * 100
    print(max2+med2+min2)
    fst= dice//10**0 %10
    scd = dice//10**1 % 10 
    trd = dice//10**2 %10
    frt = dice//10**3 %10
    print(fst,scd,trd,frt)
    current=max(fst,scd,trd,frt)
    print(current)
    if current > max(c,b,a):
        print('vamos',current,'en main')
        print(current*100+med2+min2 )
        newnumb= (dice)//10
        print(newnumb)
        return (current*100+med2+min2 ),newnumb
        fst2= newnumb//10**0 % 10 
        trd2= newnumb//10**2 %10
        scd2 = newnumb//10**1 %10
        frt2 = newnumb//10**3 %10
        if (c==max(fst2,scd2,trd2,frt2)):
            lol=(max(fst2,scd2,trd2,frt2))
            return(current*100+lol*10+lol),(newnumb//10)
            
        elif b==a:
            return(current,newnumb)
    elif b< fst:
        return (max(c,b,a)*100)+fst*10+scd,dice//10**2
    else:
        return (b*100+a*10+dice%10,dice//10)
        
def score(hand):
    
    return 42

def playThreeDiceYahtzee(dice):
    return 42

###################### END OF UNCLOMPLETED PROJECT ##################### 



def isPrime(n): ## get if a number is prime 
    if n < 2:
        return False
    if n == 2:
        return True 
    if n % 2== 0:
        return False
    maxFactor = math.ceil(n ** 0.5)
    for factor in range(3,maxFactor + 1, 2 ): 
        if n % factor == 0: # we  make sure it can only be divided by itseld
            return False
    return True 

def nthPrime(n): # uses isPrime to get the a result 
    found=0 
    guess=0
    while found <= n:
        guess += 1 
        if isPrime(guess):
            found +=1
    return guess 

def reverseNumber(n):
    sign = 1 if n>= 0 else -1
    n= abs(n)
    result = 0 
    while n > 0:
        currentDigt= n%10 # we get the rightmost number 
        result *=10 # we make space in the result by adding a 0
        result += currentDigt # we add to the result 
        n//=10 #we cut
    return result * sign



def Creatinglistsmethod(L):
    M = [ (L[i-1], L[i], i) for i in range(1, len(L)) ]
    print(M)
    return M

def countOccurences(digit,n):
    if (digit==0 and n == 0):
        return 1
    count= 0
    while n > 0: # if we cut and the current number is the same as the target number, we add to our counter
        currDigit= n%10
        if currDigit == digit:
            count += 1
        n//=10 
    return count 


def mostFrequentDigit(n):
    bestDigit= -1 
    bestCount= -1
    n= abs(n)
    for digit in range(10):
        occurences = countOccurences(digit,n)
        if occurences >= bestCount: # we change if we found a best count 
            bestCount= occurences 
            bestDigit= digit
    return bestDigit

 # loop for points in a cubic equation  
#for i in range(0,110,10):
#    lol= (i/100)**2.41
#    #print(i,lol*100)
#    print("{:e}".format(i/100),"&","{:e}".format(lol),"\\", "\hline")


def occurences(string):
    ldigit = [0] * 26
    for i in range(len(string)):
        if (ord(string[i]) >= ord('a')) and (ord(string[i])<= ord('z')):
            ldigit[ord(string[i])-ord('a')] +=1
    return ldigit 

def isIncreasingNumber(n):
    n=abs(n)
    while n> 0:
        if n%10>(n//10)%10:
            return True 
    return False
def hasConsecutiveDigits2(n):
    n=abs(n)
    previous=None
    while n>0:
        actual = n%10
        if actual == previous:
            return True
        previous= actual
        n //= 10
    return False 

def hasConsecutiveDigits(n):
    n=abs(n)
    while n> 0:
        if n%10 == (n//10)%10:
            return True 
        n//=10
    return False

def gcd(x, y):
    while y!=0:
        x, y = y,(x%y)
    return x
def babylonianSquareRootIterations(n, initialGuess, epsilon):
    guess = initialGuess
    count= 0
    while True:
        count+=1
        newGuess = (guess + n / guess) / 2
        if abs(newGuess- guess) < epsilon:return(count)
        guess = newGuess
        

        
def isBoxy(board):
    values = getUniqueValues(board)
    for value in values:
        if not isBoxyValue(board, value):
            return False
    return True

def getUniqueValues(board):
    rows, cols = len(board), len(board[0])
    uniqueValues = [ ]
    for row in range(rows):
        for col in range(cols):
            value = board[row][col]
            if value not in uniqueValues:
                uniqueValues.append(value)
    return uniqueValues

def isBoxyValue(board, value):
    rows, cols = len(board), len(board[0])
    row0, col0 = firstOccurrence(board, value)
    row1, col1 = lastOccurrence(board, value)
    if col1 < col0:
        return False
    for row in range(rows):
        for col in range(cols):
            if (row0 <= row <= row1) and (col0 <= col <= col1):
                # Check if a non-value is inside the box:
                if board[row][col] != value:
                    return False
            else:
                # Check if a value is outside the box:
                if board[row][col] == value:
                    return False
    return True    

# Finds the row and col of the top and
# leftmost occurence of a value in the board
def firstOccurrence(board, value):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == value:
                return (row, col)

# Finds the row and col of the bottom and
# rightmost occurence of a value in the board 
def lastOccurrence(board, value):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == value:
                lastRow, lastCol = row, col
    return (lastRow, lastCol)





def getPrevNumber(expr, index):
    index -= 1
    result = ''
    while index >= 0 and expr[index].isdigit():
        result = expr[index] + result
        index -= 1
    # The index is now at the first non-number character before the operator
    # Add 1 to get the starting index of the number
    return int(result), index + 1

# Get the number after the operator at the provided index 
def getNextNumber(expr, index):
    index += 1
    result = ''
    while index < len(expr) and expr[index].isdigit():
        result += expr[index]
        index += 1
    # The index is now at the first non-number character after the operator
    # Subtract 1 to get the ending index of the number
    return int(result), index - 1

# Return the next string after 1 step of evaluation 
def applyOperator(expr, index):
    n1, startIndex = getPrevNumber(expr, index)
    n2, endIndex = getNextNumber(expr, index)
    op = expr[index]
    
    if op == '&': result = n1 ** n2
    elif op == '*': result = n1 * n2
    elif op == '@': result = n1 // n2
    elif op == '%': result = n1 % n2
    elif op == '+': result = n1 + n2
    elif op == '-': result = n1 - n2
    
    return expr[:startIndex] + str(result) + expr[endIndex+1:]

# Find the index of the first operator (from left to right) 
def findFirstOperator(expr, ops):
    lowestIndex = None
    for op in ops:
        index = expr.find(op)
        if index > 0 and (lowestIndex == None or index < lowestIndex):
            lowestIndex = index
    if lowestIndex != None:
        return lowestIndex
    return None

def getIndexOfNextOperator(expr):
    # First check for &
    index = findFirstOperator(expr, '&')
    if index != None:
        return index
    # Now check for the first operator in *, @, and %
    index = findFirstOperator(expr, '*@%')
    if index != None:
        return index
    # Now check for the first operator in +, -
    return findFirstOperator(expr, '+-')

def getEvalSteps(expr):
    result = expr + ' = '
    spaces = len(expr)
    
    # Replace // and ** with single characters to simplify the code
    expr = expr.replace('//', '@')
    expr = expr.replace('**', '&')
    
    # To align the equal signs, add a stringPrefix containing spaces 
    # At the start of each line 
    stringPrefix =  ' ' * spaces + ' = '
    nextOperatorIndex = getIndexOfNextOperator(expr)
    while nextOperatorIndex != None:
        expr = applyOperator(expr, nextOperatorIndex)
        exprForResult = expr.replace('@', '//')
        exprForResult = exprForResult.replace('&', '**')
        result += exprForResult + '\n' + stringPrefix
        nextOperatorIndex = getIndexOfNextOperator(expr)
    
    # We added one extra stringPrefix on the last iteration of the loop
    # So now we remove it
    return result[:-len(stringPrefix)]

# get the first word of a set of lines :

def firstWords(lines):
    result = ''
    for line in lines.splitlines():
        # for simplicity, we are assuming every line contains a space:
        spaceIndex = line.find(' ')
        firstWord = line[0:spaceIndex]
        if result != '':
            # We already have a line, so add a newline before the next word
            result += '\n'
        result += firstWord
    return result


def wordLadder(words):
    return solveWordLadder(copy.copy(words), [])


# test case :     assert(wordLadder(['goose', 'dog', 'elk', 'toad']) ==
#                                   ['toad', 'dog', 'goose', 'elk']) 
def solveWordLadder(words, ladder):
    if words == []: # there are no more words in the  list, therefore return list
        return ladder
    else:
        for i in range(len(words)): # we go thru every words
            nextWord = words[i]
            if canAddWord(nextWord, ladder):
                # make the move 
                words.pop(i)
                ladder.append(nextWord)
                # now, recursevely, try to solve the puzzle 
                solution = solveWordLadder(words, ladder)
                if solution != None:
                    return solution 
                # we could not solve it , so undo the move
                words.insert(i,nextWord)
                ladder.pop()
        # we cannot solve the puzzle from here, so return None to backtrack 
        return None


def canAddWord(nextWord, ladder):
    if ladder == []:
        return True 
    else:
        lastWord = ladder[-1] # the last word in the laddr
        return lastWord[-1] == nextWord[0]
    

#nthHappyPrime
# REPEATED DIGIT COUNT FUNCTION 
def digitCount(n):
    n=abs(n)   
    if (n == 0):
        return 1
    return 1+ math.floor(math.log10(n))
# GET A DIGIT IN A NUMBER 
def getKthDigit(n, k):
    n = abs(n)
    return (n//10**k %10)
#IS PRIME FUNCTION 
def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True 
    if n % 2== 0:
        return False
    maxFactor = rounded(n ** 0.5)
    for factor in range(3,maxFactor + 1, 2 ):
        if n % factor == 0:
            return False
    return True 
#is happy function 
def isHappyNumber(n):
    previousDigit= None
    sum = 0 
    while (n>0):
        currentDigit= n%10
        sum+=currentDigit**2 
        n//=10
        print(sum)
    if sum == 1: 
        return True 
    elif sum == 4: 
        return False
    # recurssion in the fucntion until we get either 1 or 4
    return isHappyNumber(sum)


def isHappyPrime(n):
    return isHappyNumber(n) and isPrime(n)
def nthHappyPrime(n):
    found=0 
    guess=0 
    while found<= n:
        guess+=1 
        if isHappyPrime(guess):
            found+=1 
    return guess 
# sumOfPowersOf2
def maxPowerOf2UpToN(n):
    result=1
    # while the result*2 is less than n, multiply times 2
    while 2*result <= n:
        result*=2 
    return result 
def sumOfPowersOf2(n):
    # not positve
    if n<=0: 
        return f'{n} is not positive.'
    powerOf2 = maxPowerOf2UpToN(n)
    if powerOf2==n:
        return f'{n} is a power of 2.'
    sumSoFar= 0 
    result = f'{n} = '
    # while the so far is not greater then n 
    while sumSoFar < n:
        # if the sofar + the power of2 is not greater than the number, we add it 
        # then we need to divide the so far by 2 
        if sumSoFar + powerOf2 <= n:
            sumSoFar+= powerOf2 
            result += f'{powerOf2} + '
        powerOf2 //=2
    print(result)
    # we cut the last three characters 
    result= result[:-3]
    result+= '.'
    return result

#isWordLadder
def wordcounter(s):
    words = 0 
    i= len(s)
    for n in range(i):
        t= s[n]
        if t=='-':
            words+= 1 
    words = words+1
    return words
def isWordLadder(s):
    if wordcounter(s) < 2:
        return False
    prevWord= None
    sumWords=''
    # for each word in the string
    for word in s.split('-'):
        # if there is no separation, return false
        if ('-' not in s):
            return False
        # put a value on the first word
        if prevWord == None:
            prevWord= word
            #sum of words
            sumWords+= word+'-'
        # search for repeated in sum of words
        elif word in sumWords:
            return False
        # check the end of the previous words has one only one difference from the word
        elif not DifferWords(prevWord,word):
            return False
        else:
            prevWord= word
            sumWords+= word+'-'
        print(sumWords)
    return True 
        
        
def DifferWords(s,t):
    if((s=='') or t==''):
        return False
    # has not the same lenght
    elif (len(s) != len(t)):
        return False
    else:
        counter= 0
        for n in range(len(s)):
            #print(s[n],t[n])
            if s[n] != t[n]:
                counter+=1
             #   print(counter)
        return counter==1 

# 2.7 encodeRouteCipher + decodeRouteCipher
 # ASECRETMESSAGE  ==  ACTSG   == ACTSGESMRSEEEAz == 3ACTSGESMRSEEEAz
                    #  SRMSE
#                      EEEAz



def encodeRouteCipher(message, rows):
    collums = math.ceil(len(message)/rows)
    needed_letters = collums * rows  # the total amount of letters in the string 
    if len(message) != needed_letters:
        # is the len of the message does not form a rectangle, we add some letters to fill in 
        message = getBetter(message,needed_letters)
    counter = 0 
    result = ''
    for row in range(rows):
        for col in range(collums):
            # we extract the position as if it were in a rectangle going up up to down, as a2d grid 
            result +=message[extract(row,col,rows)]
    # Now alternate left-to-right and right-to-left.
    # make the rows go the opposite direction,
    result = changeResultMid(result,collums,rows)
    return f'{rows}' + result

def changeResultMid(result,collums,rows):
    current = 0
    final= ''
    for i in range(1,rows+1):
        poty =  result[current:i*collums] # poty is the extraction of the row 
        final+= poty[::-1] if i % 2 ==0 else poty
        current = i*collums
    return final 

def extract(row,col,rows):
    i = row + col*rows 
    return i
    
def getBetter(s,x): # s =  the message, x =  the needed leeters 
    result = s
    alphabet = getAlpha() 
    difference = x - len(s) # the difference of len in the strings 
    for i in range(1,difference+1):
        # we add the lasts letters of the alphabet in order 
        result += alphabet[-i].lower() 
    return result
    
def getAlpha():# function returns the alphabet 
    result = ''
    for i in range(65,91):
        result +=(chr(i))
    return result

def decodeRouteCipher(encodedMessage):
    result= ''
    rows , newMessage= getDigit(encodedMessage)
    collums = math.ceil(len(newMessage)/rows) # equation to hege the number of collums the lenght of the message divided bt the rows 
    newString = changeResultMid(newMessage,collums,rows) # Now alternate left-to-right and right-to-left.
    starting = -1       
    for row in range(collums): # this is just some magic bullshit i shoved off my ass, but it does worrk 
            for col in range(rows):
                i =  row + col*collums  # the same procedure as for the encode 
                result+= newString[i]
    final =''
    for i in range(len(result)):
        if not result[i].islower(): # we take the uncapital letters 
            final += result[i]
    return final
def getDigit(s): # this fucntion separates the number of rows and the the message 
    result1=''
    result2=''
    for i in range(len(s)):
        if s[i].isdigit():
            result1+= s[i]
        else:
            result2+=s[i]
    return int(result1) , result2


# remove evens ( mutating and not mutating ) 
def mutatingRemoveEvens(L):
    i=0
    while i<len(L):
        if L[i] %2==0:
            L.pop(i)
        else:
            i+=1
def nonmutatingRemoveEvens(L):
    result=[]
    for v in L:
        if v % 2 ==1:
            result.append(v)
    return result
# remove repeats (mutating and nonmutating)
def mutatingRemoveRepeats(L):
    i=0
    while i<len(L):
        if L[i] in L[:i]:
            L.pop(i)
        else:
            i+=1
        print(L)
def nonmutatingRemoveRepeats(L):
    result= []
    for i in L:
        print(i)
        if i not in result:
            result.append(i)
    return result 
# firstN  even fibboanachi nymbers
def nthFibonacciNumber(n):
    return ((1+math.sqrt(5))**(n+1)-((1-math.sqrt(5))**(n+1)))/((2**(n+1))*(math.sqrt(5))) 
    
def firstNEvenFibonacciNumbers(n):
    result=[]
    i=0
    found=0
    while found<n:
        print(found)
        #print(math.floor(nthFibonacciNumber(i)))
        if math.floor(nthFibonacciNumber(i)) % 2 == 0 and math.floor(nthFibonacciNumber(i)) not in result:
            print('quak')
            result.append(math.floor(nthFibonacciNumber(i)))
            found += 1
        else:
            i+=1
    return result
# reoeating pater

def repeatingPattern(L):
    M= copy.copy(L)
    mid=(len(M))//2
    if len(M)<2:
        return None 
    # we divide the list into two
    for i in range(1,mid+1):
        pattern = L[:i]
        # we go indiviadualy, digit by digit from left to right to see paterns
        if len(L) % i ==0:
            repeats= len(L) // len(pattern) # the possible repeats 
            # if the pattern * the repeats is the same as the list, we found a pettern 
            if L == pattern * repeats:
                return pattern 
    return None 

# multiply ponlinomials 
def multiplyPolynomials(p1, p2):
    maxcof=(len(p1)-1)+ (len(p2)-1) # the max coefficient in the lists 
    # make an empty list with the size of the max coefficient 
    result =[0] * (maxcof+1)
    cofP1 = len(p1) -1  # cofficient of p1
    for i in range(len(p1)):
        cofP2 = len(p2) -1 # cofficient of p2
        for j in range(len(p2)):
            cof  = maxcof - (cofP1 + cofP2) # actual cofficient 
            result[cof] += p1[i]*p2[j] # add to out list
            cofP2 -=1  # lower the coefficient 
        cofP1 -= 1    #   
    return result

# linear regression 
def linearRegression(points):
    lenght=(len(points))
    x=0
    y=0
    x_sqrt=0 
    xy=0
    y_sqrt=0 
    for i in points:
        x+= i[0]
        y+= i[1]
        x_sqrt += (i[0])**2
        y_sqrt += (i[1])**2
        xy+= (i[0])*(i[1])
    m=((lenght*xy)-(x*y))/((lenght*x_sqrt)-(x**2))
    b=(y-(m*x))/lenght
    if(m== 0):
        return(m,b,1.0)
    else:    
        r=((lenght*xy)-(x*y))/(((lenght*x_sqrt)-(x**2))*((lenght*y_sqrt)-(y**2)))**0.5
        return(m,b,r)
def tuplesAlmostEqual(t1, t2):
    if len(t1) != len(t2): return False
    for i in range(len(t1)):
        # Note we are using an epsilon of .001, which is smaller that usual
        # since this exercise can have larger rounding errors
        if not almostEqual(t1[i], t2[i], epsilon=.001):
            return False
    return True

# run simple program ( language )

# we are going to be using the .startwith() method in order to evaluate the beginnig of a value 
def getvalue(variables,name): # we get the value of a variable using its name
    i= int(name[1:])
    while i>= len(variables):
        variables.append(0)
    print(name,'variable name',variables,'list of local variables')
    return variables[i] # we get the value from the local vairable list 

def setvariable(variables,name,value):
    print('setting value', value,'to', name)
    i = int(name[1:])
    while i >= len(variables):
        variables.append(0)
    variables[i] = value

def findlabel(program,label):
    print('finding label', label)
    for linenumber in range(len(program)):
        if program[linenumber] == (label + ':'):
            return linenumber
    return -1 
    
def evalexpression(expression, variables,args): # expression is the line leftover, varibles are the list and args
    print('evaluation expression....')
    stack=[] # abstract data type 
    for val in expression:
        if val.startswith('L'): # get the local varialble for L
            stack.append(getvalue(variables,val))
        elif val.startswith('A'):
            stack.append(args[int(val[1:])])
            # we need to get the valu of A, append to stack
        elif val.isdigit():
            ##if it is a digit, append to stack
            stack.append(int(val))
        else:  # we are doing a math operation 
            stack.append(val)
        
    while len(stack) > 1: #shile stack is not empty 
        argument2= stack.pop() # we grab the arguments, and then we pop of the list
        argument1= stack.pop()
        operator = stack.pop()
        if operator == '-':
            stack.append(argument1 - argument2)
        elif operator =='+':
            stack.append(argument1 + argument2)
        else: ## in case there is no argument or operator
            print('invalid sintax :C')
            print(1/0)
    return stack.pop() # the final resutlt if retuned and then is poped off the list 
    
def doWork(line,variables,args): ### here we get the result of any L/variable in the program 
    result = evalexpression(line[1:],variables,args)
    setvariable(variables, line[0],result)
    
def runSimpleProgram(program, args):
    program = program.splitlines()
    for linenumber in range(len(program)):
        program[linenumber] = program[linenumber].strip()
    linenumber=0
    variables=[]
    while True: #the program is in a undefitante loop 
        line = program[linenumber].split() #this tokenices the line itself
        linenumber+=1 
        if (line[0] == '!') or (line[0][-1] == ':') :#we skip because is either a comment or label
            continue
        elif line[0] == 'RTN':
            ## return/evaluate the expression value
            return evalexpression(line[1:],variables,args)
        elif line[0] == 'JMP':
            linenumber= findlabel(program,line[1])
            #we jumpm the next time we actually see the label
        elif line[0] == 'JMP+': ## we jump to the label if the expression if positive, otherwise skip
            if evalexpression(line[1:-1],variables,args)>0:
                linenumber= findlabel(program,line[-1])
        elif line[0] == 'JMP0':
            if evalexpression(line[1:-1],variables,args) ==0:
                linenumber= findlabel(program,line[-1])
        ## we jump to the given label if the value of the expressin is qual to 0   
        elif line[0].startswith('L'):
            doWork(line, variables, args)
        ## we need to evaluated the loval variable

    #largest = """! largest: Returns max(A0, A1)
    #               L0 - A0 A1
    #               JMP+ L0 a0
    #               RTN A1
    #               a0:
    #               RTN A0"""
    #assert(runSimpleProgram(largest, [5, 6]) == 6)
    #assert(runSimpleProgram(largest, [6, 5]) == 6)
    #sumToN = """! SumToN: Returns 1 + ... + A0
    #            ! L0 is a counter, L1 is the result
    #            L0 0
    #            L1 0
    #            loop:
    #            L2 - L0 A0
    #            JMP0 L2 done
    #            L0 + L0 1
    #            L1 + L1 L0
    #            JMP loop
    #            done:
    #            RTN L1"""
    #assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    #assert(runSimpleProgram(sumToN, [10]) == 10*11//2)

# instructions 
#Here are the legal expressions in this language:
#
#[Non-negative Integer]
#Any non-negative integer, such as 0 or 123, is a legal expression.
#
#A[N]
#The letter A followed by a non-negative integer, such as A0 or A123, is a legal expression, and refers to the given argument. A0 is the value at index 0 of the supplied args list. It is an error to set arg values, and it is an error to get arg values that are not supplied. You may ignore these errors, as we will not test for them!
#
#L[N]
#The letter L followed by a non-negative integer, such as L0 or L123, is a legal expression, and refers to the given local variable. It is ok to get an unassigned local variable, in which case its value should be 0.
#
#[operator] [operand1] [operand2]
#This language allows so-called prefix expressions, where the operator precedes the operands. The operator can be either + or -, and the operands must each be one of the legal expression types listed above (non-negative integer, A[N] or L[N]).
#And here are the legal statements in this language (noting that statements occur one per line, and leading and trailing whitespace is ignored):
#
#
#! comment
#Lines that start with an exclamation (!), after the ignored whitespace, are comments and are ignored.
#
#L[N] [expr]
#Lines that start with L[N] are assignment statements, and are followed by the expression (as described above) to be stored into the given local variable. For example: L5 - L2 42 This line assigns (L2 - 42) into L5.
#
#[label]:
#Lines that contain only a lowercase word followed by a colon are labels, which are ignored except for when they are targets of jump statements.
#
#JMP [label]
#This is a jump statement, and control is transferred to the line number where the given label is located. It is an error for such a label to not exist, and you may ignore that error.
#
#JMP+ [expr] [label]
#This is a conditional jump, and control is transferred to the line number where the given label is located only if the given expression is positive. Otherwise, the statement is ignored.
#
#JMP0 [expr] [label]
#This is another kind of conditional jump, and control is transferred only if the given expression is 0.
#
#RTN [expr]
#This is a return statement, and the given expression is returned.

 
# histogram 

def histogram(L):
    if L == []:
        return ''
    M=[0]*10
    for x in L:
        if not isinstance (x,(int,float)):
            pass
        poty = x // 10
        M[poty] +=1 

    rangee=[]
    for i in range(len(M)): # the range of different grades we have in the data 
        if M[i] ==0:
            continue
        else:
            rangee.append(i)
    maxl=max(rangee)# get the bounds of our range 
    minl=min(rangee)
    result= ""
    # we loop in the range of our answer 
    for i in range (minl,maxl+1):
        rang=i*10
        range2= i*10+9
        if M[i] > 0:
            result += f'{rang}-{range2}: {"*"* M[i]}\n'  # we plug in the occurecenses in fomat 
        else:
            result += f'{rang}-{range2}:\n'
    return(result)
    # [1, 11, 21, 31, 41, 51, 61, 71, 81, 91] == 0-9: * 
                                            #    10-19: *
                                            #    20-29: *
                                            #    30-39: *
                                            #    40-49: *
                                            #    50-59: *
                                            #    60-69: *
                                            #    70-79: *
                                            #    80-89: *
                                            #    90-99: *
                                            #    '''
# polynomail to string 
 
def polynomialToString(coeffs):
    # This helper function may be useful for your __repr__ method!
    if coeffs == [] : return  '0' # case of empty list
    else:
        terms = [ ]     
        for i in range(len(coeffs)): # loop over the values in the list 
            coeff = coeffs[i]
            if (coeff != 0): # make sure we are skipping numbers with 0 value 
                isNegative = (coeff < 0)
                coeff = abs(coeff)
                if (terms != [ ]):# if the list is not empty, add - or  + 
                    terms.append(' - ' if isNegative else ' + ')
                if (terms == [ ]) and isNegative: # is the starting value is negative, add a minus sing at the beggining 
                    terms.append('- ')
                terms.append(str(coeff)) # we append the coeff to the terms 
                power = len(coeffs)-1-i  # check what the powers
                if (power == 1): terms.append('n')
                elif (power > 1): terms.append(f'n^{power}') # join the exponents
        return ''.join(terms) # join the terms that are separeted by a ' '
# polynomialToString([2, -3, 0, 4]) == '2n^3 - 3n^2 + 4'

# are of polygon 
def areaOfPolygon(L):
    M = copy.copy(L)
    M.append(L[0]) # add the first point at the end of the list 
    X = [ M[i][0] for i in range(len(M)) ] # extract my x points 
    Y = [ M[i][1] for i in range(len(M)) ] # extract my y points 
    result=0
    for i in range(len(X)-1):
        x=(X[i+1]-X[i]) # the width
        y=(Y[i+1]+Y[i])/2 # the average height 
        area=x*y
        result+= area
    print(result,'area')
    if result <0 :
        return result*-1
    else:
        return result
# areaOfPolygon([(1,1), (4,1), (4,3), (1,3)]) == 6)

#is clique 
def nonmutatingRemoveRepeats(L):
    result= []
    for i in L:
        if i not in result:
            result.append(i)
    return result 
    
def isClique(friends):
    localist=[]
    for x in friends:
        for l in x:
            localist.append(l)
    sortlist = nonmutatingRemoveRepeats(localist) # first, make a list of everyone 
    print(sortlist) 
    
    
    for i in range(len(sortlist)):
        person1= sortlist[i]
        for j in range(i+1,len(sortlist)): ## make all the possible iterations of friends, efficiently
            person2 = sortlist[j]
            print(person1,i,'_____',person2,j)
            if(((person1, person2)not in friends) and ((person2, person1)not in friends)): #check if all are friends 
               return False
    
    return True 
   #    assert(isClique([ ('Fred', 'Wilma'),
   #                  ('Barney', 'Fred'),
   #                  ('Wilma', 'Barney') ]) == True)

# look and say 
def lookAndSay2(L):
    t=()
    result=[]
    counter=0
    i=0
    pointer=0
    while i <len(L): # using a while instead of a for loop 
        if (L[pointer] == L[i]):
            counter+=1
            i+=1
        else:
            pointer=i
            result.append((counter,L[i-1]))
            counter=0
    result.append((counter,L[i-1]))    
    return result
        
def lookAndSay(L):
    if L == []: return []
    result=[]
    counter=0
    currvalue=L[0] # we start with the first one 
    for i in L:
        if currvalue==i: # if we see the number again we add to the counter
            counter+=1
        else: # else we add the counter with the value to the result 
            result+= [(counter, currvalue)]
            currvalue= i # we change the value of the value we looking at
            counter= 1 # we update the counter
    result+= [(counter, currvalue)]  # we add the last instance  
    return result
        
def inverseLookAndSay(L):
    result = []
    for (count,value) in L:
        result.extend([value]*count)  #never used the extend before, but it adds lists 
    return result 

# [3, 3, 8, -10, -10, -10, 3]) == [(2, 3), (1, 8), (3, -10), (1, 3)])

# remove row and col(mutating and non mutating )
def mutatingRemoveRowAndCol(L, targetRow, targetCol):
    L.pop(targetRow) # remove the row
    for rowlist in L: # loop over teh rows 
        rowlist.pop(targetCol) # remove the col from each row 

def nonmutatingRemoveRowAndCol(L, targetRow, targetCol):
    rows, cols = len(L), len(L[0])
    M=[]
    for row in range(rows): # loop over the rows
        if row != targetRow: # exclude the target row
            newlist=[] 
            for col in range(cols): # loop over the col parts of the row
                if col != targetCol: # exlude the target col
                    print(L[row][col])
                    newlist.append(L[row][col]) # append the unxcluded values to the row
            M.append(newlist) # append the rows
    return M


# isLatinSquare
def squarelist(L):
    for val in L:
        if(not isinstance(val,list)):
            return False
        if len(val) != len(L):
            return False
    return True
    
def hasDuplicates(L):
    for val in L:
        if L.count(val) >1:
            return True
    return False
def samevalues(L,M):
    return sorted(L) == sorted(M)  

def isLatinSquare3(L):
    if L == []:
        return False
    if not squarelist(L):
        return False
    if hasDuplicates(L):
        return False
    n= len(L[0]) ## has the same number of rows and collums 
    target= L[0] ## the fist numbers in the row are going to be used 
    for i in range(n):
        rowlist = L[i]
        colist = [L[row][i] for row in range(n)] ## usign a list compreghesion 
        if ((not samevalues(rowlist, target)) or  (not samevalues ( colist,target))):
            return False 
    return True

# the best and most understandable version 
def getCol(L,n):
    result = []
    for i in L:
        for j in range(len(i)):
            if j == n:
                result.append(i[j])
    return result 
def isLatinSquare(L):
    if type(L[0]) != list:
        return False 
    if len(L[0]) != len(L):
        return False
    for i in range(len(L)):
        for j in range(i+1,len(L)): # check the rows and cols have the same values and they are not the same order
            if (L[i] == L[j]) or sorted(L[i]) != sorted(L[j]) or sorted(getCol(L,i)) != sorted(getCol(L,j)):
                return False
    return True  

# wordSearch

def wordSearchFromCell(board,word, startrow, startcol):  # ther are 8 possible direction to look for the word
    #there are way to interpret direction, drow, dcol (0,-1)  <--- left , (+1,+1) <- down and to the right , just like a x, and y axis but + in y is down (inverted)
    for drow in [-1,0,+1]:  #posibles ways we can go in drow 
        for dcol in [-1,0,+1]: #this could also be in range(-1,2) , less clear though 
            if (drow, dcol) != (0,0):
                if wordSearchFromCellInDirection(board,word,
                                                startrow, startcol,
                                                drow, dcol) == True:  # means we have founded 
                    return True
    return False 
    
def wordSearchFromCellInDirection(board,word,startrow, startcol,drow, dcol):# for the starting row, starting col, adn with a direction !!!@ 
    rows, cols = len(board), len(board[0])
    for i in range(len(word)):
        targetrow= startrow + i * drow
        targetcol= startcol + i * dcol
        if ((targetrow < 0 ) or  (targetrow >=rows) or 
        (targetcol< 0) or (targetcol >= cols) or 
        (board[targetrow][targetcol] != word[i])):
            return False
    print(board[targetrow][targetcol], i , 'quak',targetrow,targetcol,'quak',startcol, startrow, word)
    return True 
def wordSearch(board, word): #getting the col and row, and going in the given direction by wordSearchFromCell  
    rows, cols = len(board), len(board[0]) ## we get the size of the board
    for row in range(rows):## ittterate thru every row
        for col in range(cols): #ittertate thru the collums 
            if wordSearchFromCell(board,word, row, col) == True: #looks for the word in the board starting from that location  , tries every single letter and in the rows and collums  
                return True
    return False
        
# word search 1 
def wordSearchFromCell(board,word, startrow, startcol): # ther are 8 possible direction to look for the word
    #there are way to interpret direction, drow, dcol (0,-1)  <--- left , (+1,+1) <- down and to the right , just like a x, and y axis but + in y is down (inverted)
    for drow in [-1,0,+1]:  #posibles ways we can go in drow 
        for dcol in [-1,0,+1]: #this could also be in range(-1,2) , less clear though 
            if (drow, dcol) != (0,0):
                if wordSearchFromCellInDirection(board,word,
                                                startrow, startcol,
                                                drow, dcol) != False:  # means we have founded 
                    x,y= None, None 
                    resultblock = (wordSearchFromCellInDirection(board,word,startrow, startcol,drow, dcol))
                    result=""
                    #print(drow,dcol)
                    if dcol >= 1:
                        x= 'right'
                    elif dcol < 0:
                        x= 'left'
                    if drow ==-1:
                        y= 'up'
                    if drow == 1:
                        y= 'down'
                    elif drow == 0:
                        y= None
                    if y== None :
                        result += f'{resultblock} heading {x}'
                    else:
                        result += f'{resultblock} heading {y}-{x}'
                    #print(x,y, resultblock)
                    return result 
    return False 
    
def wordSearchFromCellInDirection(board,word,startrow, startcol,drow, dcol):# for the starting row, starting col, adn with a direction !!!@ 
    
    rows, cols = len(board), len(board[0])
    for i in range(len(word)):
        targetrow= startrow + i * drow
        targetcol= startcol + i * dcol
        if ((targetrow < 0 ) or  (targetrow >=rows) or 
        (targetcol< 0) or (targetcol >= cols) or 
        (board[targetrow][targetcol] != word[i])):
            return False
    #print(startcol,startrow)
    return (startrow,startcol) 
def wordSearch(board, word): #getting the col and row, and going in the given direction by wordSearchFromCell  
    errormesagge= f"'{word}' not found"
    result=''
    rows, cols = len(board), len(board[0]) ## we get the size of the board
    for row in range(rows):## ittterate thru every row
        for col in range(cols): #ittertate thru the collums 
            if wordSearchFromCell(board,word, row, col) != False: #looks for the word in the board starting from that location  , tries every single letter and in the rows and collums  
                mess=(wordSearchFromCell(board,word, row, col))
                text= f"'{word}' is at {mess}"
                return text
    return errormesagge

# better word search 2
def wordSearchFromCell(board,word, startrow, startcol): # ther are 8 possible direction to look for the word
    #there are way to interpret direction, drow, dcol (0,-1)  <--- left , (+1,+1) <- down and to the right , just like a x, and y axis but + in y is down (inverted)
    for drow in [-1,0,+1]:  #posibles ways we can go in drow 
        for dcol in [-1,0,+1]: #this could also be in range(-1,2) , less clear though 
            if (drow, dcol) != (0,0):
                result = wordSearchFromCellInDirection(board,word,startrow,startcol,drow,dcol)  # means we have founded 
                
                if result != None:
                    return result
    return None
    
def wordSearchFromCellInDirection(board,word,startrow, startcol,drow, dcol):# for the starting row, starting col, adn with a direction !!!@ 
    rows, cols = len(board), len(board[0])
    for i in range(len(word)):
        targetrow= startrow + i * drow
        targetcol= startcol + i * dcol
        if ((targetrow < 0 ) or  (targetrow >=rows) or  #check if it is out of bound 
        (targetcol< 0) or (targetcol >= cols)):
            return None
        print(board[targetrow][targetcol],word[i],i)
        if ((board[targetrow][targetcol] != '?') and 
            (word[i] != '?') and # si el word[i] es ? , continuamos por que baord[][] no es ? si . #board [][] word[] no son iguales, pero ? es word[i]
            (board[targetrow][targetcol] != word[i])):
            return None 
    #print(startcol,startrow)
    dirName= getDirName(drow,dcol)
    print(drow,dcol,'magaquaaak',targetrow,targetcol)
    #repr(word) lets us put the value in parenthesis 
    return f'{repr(word)} is at {(startrow,startcol)} heading {dirName}'
def wordSearch(board, word): #getting the col and row, and going in the given direction by wordSearchFromCell  
    errormesagge= f"'{word}' not found"
    result=''
    rows, cols = len(board), len(board[0]) ## we get the size of the board
    for row in range(rows):## ittterate thru every row
        for col in range(cols): #ittertate thru the collums 
            result = wordSearchFromCell(board,word, row, col)  #looks for the word in the board starting from that location  , tries every single letter and in the rows and collums  
            if result != None:    
                return result
    return errormesagge
    



def getDirName(drow,dcol): # a pointer in the board and its location 
    dirNames = [['up-left',  'up'  , 'up-right'],
                [ 'left',    ''   , 'right'],
                ['down-left','down', 'down-right']]
    
    return dirNames[drow+1][dcol+1]

# wordsearch 3
def wordSearch(board, word):
    rows , cols = len(board) , len(board[0])
    for row in range(rows):
        for col in range(cols):
            result = wordSearchFromCell(board,word,row,col)
            if result != None:
                return result
    return f'{repr(word)} not found'

def wordSearchFromCell(board,word, startrow, startcol): # ther are 8 possible direction to look for the word
    #there are way to interpret direction, drow, dcol (0,-1)  <--- left , (+1,+1) <- down and to the right , just like a x, and y axis but + in y is down (inverted)
    for drow in [-1,0,+1]:  #posibles ways we can go in drow 
        for dcol in [-1,0,+1]: #this could also be in range(-1,2) , less clear though 
            if (drow, dcol) != (0,0):
                result = wordSearchFromCellInDirection(board,word,startrow,startcol,drow,dcol)  # means we have founded 
                
                if result != None:
                    return result
    return None
    
def wordSearchFromCellInDirection(board,word,startrow, startcol,drow, dcol):# for the starting row, starting col, adn with a direction !!!@ 
    rows, cols = len(board), len(board[0])
    for i in range(len(word)):
        targetrow= (startrow + i *drow)% rows # this does the trick for better word serch 3, kind of wrapping around 
        targetcol= (startcol + i * dcol) % cols
        if board[targetrow][targetcol] != word[i]:
            return None 
    dirName= getDirName(drow,dcol)
    return f'{repr(word)} is at {(startrow,startcol)} heading {dirName}'
def getDirName(drow,dcol):
    dirnames = [['up-left','up','up-right'],
                ['left','      ','right'],
                ['down-left','down','down-right']]
    return dirnames[drow+1][dcol+1]


# make edits for grids 

def nonmutatingRemoveRepeats(L): # this function extracts both of the value in the str
    result= []
    for i in L:
        if i.isdigit():
            result.append(i)
        else:
            continue
    return result 
def docoloperation(cop,part):
    arg=nonmutatingRemoveRepeats(part)
    print(arg)
    for i in range(len(cop)):                       # loop over the rows
        cop[i][int(arg[0])],cop[i][int(arg[1])] = cop[i][int(arg[1])], cop[i][int(arg[0])] # swap the values of the collums  
def dorowoperation(cop,part):
    arg=nonmutatingRemoveRepeats(part)
    cop[int(arg[0])],cop[int(arg[1])]=cop[int(arg[1])] ,cop[int(arg[0])] # swap the rows 

def makeEdits(M, E):
    cop = copy.deepcopy(M)
    for i in E:
        part = i.split()
        if part[1] == 'row':
            dorowoperation(cop,part[1:]) # do a row operation 
        elif part[1] == 'col':
            docoloperation(cop,part[1:]) # do a col operation 
    return cop
    #      testMakeEdits():
    #   M = [[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]]
    #   E = ['swap row 0 and row 1',
    #        'swap col 1 and col 2',
    #        'swap row 0 and row 2']
    #   R = [[7, 9, 8],
    #        [1, 3, 2],
    #        [4, 6, 5]]

#insertRowAndCol (mutating and nonmutating) 
def make2dList(rows, cols):# function that makes a empty 2d list with rows and cols
    return [ [0]*cols for row in range(rows) ]
    
def mutatingInsertRowAndCol(L, row, col, val):
    rows, cols = len(L), len(L[0])  
    L.insert([int(row)],[val] * cols)   # this is for the rows
    
    for i in L:   # this is for the collums  
            i.insert(int(col),val)
    

def nonmutatingInsertRowAndCol(L, row, col, val):
    rows, cols = len(L), len(L[0])  
    result= []
    result+=(L[:row])# we get the first left of the 2d list
    result.append([val]*cols) # insert the row with the val
    result+= (L[row:]) # put the right part
    
    
    result2=[]
    resultcol = []

    for i in result:# we loop over the rows
        resultcol=[] # the row we are going to have
        resultcol+= i[:col]  # we get the left part
        resultcol.append(int(val)) # insert the val 
        resultcol+= i[col:] # we get the right part
        result2.append(resultcol) # append it to the list 
    return result2 

#matrix multiply 
def make2dList(rows, cols): # make an empty result  
    return [[0]*cols for row in range(rows) ]

def to_matrix(l,n):
    return [l[i:i+n] for i in range(0, len(l),n)] # turns the 1d list into 2d list with n of rows

def matrixMultiply(m1, m2):
    sumlist=[]
    rows, cols = len(m1), len(m1[0])
    rows2, cols2 = len(m2), len(m2[0])
    
    if cols != rows2:
        return None 
    emptyresult = make2dList(rows,cols2)
    for col in range(cols2): # we loop over the coolums in the m2
        colList = [ m2[row][col] for row in range(rows2) ] # extract the collum
        for i in m1: #loop over the rows in m1
            rowList= i
            sum = 0
            for x in range(len(rowList)): #loop over the values of rowlist and colits
                sum += (rowList[x] * colList[x]) # multiply the values and add them to sum 
            sumlist.append(sum) #append the sum to sumlist 
    print(rows)
    end = to_matrix(sumlist,rows)# the end we get its wrong, 
    # the values in end are in the rows up to down, and they should be righ to left
    print(end,'end',sumlist)
    rowend, colend = len(end), len(end[0])
    endend=[]
    for col in range(colend):
        colList2 = [ end[row][col] for row in range(rowend) ] # we exteact the cols and make them rows
        endend+= [colList2] # add the row to the final result 
    if len(m1)!=1:
        return endend
    else:
        return [sumlist] 
    
# isKingTour 

def isKingsTour(board):
    rows,cols = len(board),len(board[0])
    for row in range(cols):
        for col in range(rows):
            # if one of the vales is less than one, 
            #or greater than the space in the list, return false 
            if board[row][col] > rows**2 and board[row][col] < 1:
                return False
            else:
                if board[row][col] == rows**2: pass # we skip the last possible number 
                else:
                    #we go and search for a kings tour with the helper function 
                    if not searchFromBoard(board,board[row][col],row,col):
                        return False
    return True
def searchFromBoard(board,target, startrow, startcol):  # ther are 8 possible direction to look for the word
    rows,cols = len(board),len(board[0])
    #there are way to interpret direction, drow, dcol (0,-1)  <--- left , (+1,+1) <- down and to the right , just like a x, and y axis but + in y is down (inverted)
    for drow in [-1,0,+1]:  #posibles ways we can go in drow 
        for dcol in [-1,0,+1]: #this could also be in range(-1,2) , less clear though 
            if (drow, dcol) != (0,0): # we skip in case of no direction
                # so we go in every value in the board, in every direction to look for a the next number 
                if  checkIndirection(board,target,startrow,startcol,drow,dcol):
                    return True 
    return False 
def checkIndirection(board,target,startrow,startcol,drow,dcol):
    rows, cols = len(board), len(board[0])
    targetrow= startrow +  drow # adding the drow and startrow to get the surrounding values
    targetcol= startcol +  dcol
    if ((targetrow < 0 ) or  (targetrow >=rows) or # check we are no out of bound
        (targetcol< 0) or (targetcol >= cols)):
            pass 
    elif board[targetrow][targetcol] == target +1: # check we have a n+1 around n 
        return True
    else:
        return False 

# check sudoku 
def isLegalSudoku(grid):
    # 4x4 or 9x9 grid
    # For every row,colum, and block:
    #non non-integers 
    # all valuel are in range
    # No duplicate values 
    rows,cols = len(grid) , len(grid[0])
    # lets check it is square
    if rows != cols:
        return False
    #4x4 or 9x9x:
    if (rows != 4) and (cols !=9):
        return False 
    # For every row,colum, and block: ( we are using a function)
    if not rowsArelegal(grid):
        return False
    if not colsArelegal(grid):
        return False
    if not blockAreLegal(grid):
        return False
    return True 

def rowsArelegal(grid): # legal rows
    for rowlist in grid: 
        if not areLegalValues (rowlist):# check all the rows are legal 
            return False
    return True
def colsArelegal(grid): #legal cols
    cols, rows= len(grid[0]),len(grid)
    for col in range(cols):
        colList = []
        for row in range(rows): # use the value to get a colist 
            colList.append(grid[row][col])
        if not areLegalValues(colList):# check the value of the call list 
            return False
    return True
def blockAreLegal(grid): #legal blocks
    cols, rows= len(grid[0]),len(grid)
    blocks = rows
    blockSize= int(blocks ** 0.5) 
    for blockNum  in range(blocks):
        startRow = blockNum // blockSize * blockSize # get the intial row
        startCol =blockNum %blockSize * blockSize  # get the intial col
        print(startRow,startCol, blockNum)
        #  | 0  |  1  |  2  | 
        #  | 3  |  4  |  5  |
        #  | 6  |  7  |  8  |
        blockList = []
        for row in range(startRow,startRow + blockSize):
            for col in range(startCol, startCol + blockSize):
                blockList.append(grid[row][col])# add the values of the blocks
                # then check if the block is legal 
        if not areLegalValues(blockList):
            return False
    return True 


#takes a 1d list and make sure they are legal
def areLegalValues(values):
    n=len(values)
    for value in values:
        # chekc the type of the value 
        if type(value) != int:
            return False
        # make sure the value is positive and not larger than the len of list
        if (value<0) or (value>n):
            return False
        # check there are no repeats greter than 0 
        if (value> 0)  and (values.count(value) > 1):
            return False 
    return True 
# same polygons 
def removeDuplicates(L):
    M=[]
    for i in range(len(L)):
        nextI = (i+1) % len(L) ### next I example
        if L[i] != L[nextI]:
            M.append(L[i])
    return M 
def rotateList(L,i):#rotate the list L by i elemts to the left
    return L[i:] + L[:i]
def polygonsMatch(p1,p2):# try matching every rotation of o1 against p2
    for i in range(len(p1)):
        if(rotateList(p1,i) == p2):
            return True
    return False
    
def samePolygons(p1, p2):
    p1=  removeDuplicates(p1)
    p2 = removeDuplicates(p2)
    if len(p1) != len(p2):
        return False
    return polygonsMatch(p1,p2) or polygonsMatch(p1,list(reversed(p2)))


#nqueenschecker 
def queenSearchFromCell(board,x,y):  
    for drow in [-1,0,+1]:  # go in directions 
        for dcol in [-1,0,+1]:
            if (drow, dcol) != (0,0):
                if wordSearchFromCellInDirection(board,x,y,drow, dcol) == True:
                    return True
    return False                
def wordSearchFromCellInDirection(board,x,y,drow, dcol):# for the starting row, starting col, adn with a direction !!!@ 
    rows, cols = len(board), len(board[0])
    startrow, startcol = x[0],x[1]
    for i in range(len(board[0])):
        targetrow= startrow + i * drow
        targetcol= startcol + i * dcol
        point_Tuple=(targetrow,targetcol)
        if (point_Tuple == y): # if the trues  touch, return true (or false overall )
            return True
    return False
    
def nQueensChecker(board):
    rows, cols = len(board), len(board[0])
    # we store the positions of the trues in tuples with intgers 
    countTrue = [ (j, i) for i in range(rows) for j in range(cols) if board[i][j] is True ]
    if len(countTrue) <= 2 :
        return False 
    for x in countTrue: # every iteration of the tuples 
        for y in countTrue:
            if x == y:
                continue 

            if queenSearchFromCell(board,x,y) == True:
                return False
    return True 
# is boxy 


#another way to get unique values (list comprehesion):
def getUniqueValues2(board):
    listy =[first for second in board for first in second ]
    unique=[]
    for item in listy:
        value = item
        if value not in unique:
            unique.append(value)
    return unique
# end of prototype 


def isBoxy(board):
    values = getUniqueValues(board) # we get unique value
    for value in values:
        if not isBoxyValue(board, value):# go thru every value and check boxy
            return False
    return True
    
def getUniqueValues(board):
    rows, cols = len(board) , len(board[0])
    uniqueValues = []
    for row in range(rows):
        for col in range(cols):
            value = board[row][col]
            if value not in uniqueValues:
                uniqueValues.append(value)
    return uniqueValues

def isBoxyValue(board, value):
    rows, cols = len(board), len(board[0])
    row0, col0 = firstOccurance(board, value) # we get the first occurance 
    row1, col1 =  lastOccurance(board, value)  # we get the last occurance 
    for row in range(rows): # loop through the board 
        for col in range(cols):
            if (row0 <= row <= row1) and (col0 <= col <= col1): # only check the values in the box
                #check if a non-value is inside the box :
                if board[row][col] != value:
                    print("eaukyyyy")
                    return False
            else: 
                #check if value is outside the box:
                if board[row][col] == value:
                    print("qukay", row, col,value,"quaky",row0,row1,col0,col1)
                    return False
    return True
    
def firstOccurance(board, value):
    rows,cols = len(board) , len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == value:
                return(row, col)
                
def lastOccurance(board, value):
    rows, cols = len(board) , len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == value:
                lastrow, lastcol = row, col
    return (lastrow, lastcol) 


# repeats 
def repeats(L):
    seen = set() # seen for the values already seen 
    seenAgain= set() # values that are seen again  
    for v in L: # loop over the values of the list 
        if v in seen: # if they are in the seen, add to seen again
            seenAgain.add(v)
        seen.add(v) # nevertheless add them to seen 
    return sorted(seenAgain) # return a sorted list 


# has no duplicates :
def hasNoDuplicates(L):
    return len(L) == len(set(L))

# is in both 
def inBothLists(L, M):
    resulty = []
    x = set(L)
    y = set(M)
    z = x.intersection(y) # check the intersections in both 
    for val in z: # make a new list with the values in the set 
        resulty.append(val)
    return resulty
# is in one list 
def inOnlyOneList(L, M):
    resulty = []
    x = set(L)
    y = set(M)
    z = x.difference(y) # get the unique values in x
    w = y.difference(x) # get the unique values in y  
    p = z.union(w) # joing this sets 
    print(p)
    for val in p:
        resulty.append(val)
    return resulty
 # permutation 
def isPermutation(L):
    for i in range(len(L)):
        if i not in set(L):return False 
    return True 
# reverse strigs 
def reverseStrings(L):
    s= set(L)
    setty = set() #make an empty set 
    for i in range(len(L)): # loop over the values in the set with index i
        x = L[i] # x is the value of the set 
        if type(x) is str: # chekc is they are a string 
            trial =(x[::-1]) # we turn x into the reverse of itseld 
            if trial in L: # check if the string is in the list, or is a palindrome 
                setty.add(trial)
    return setty
# upper and lower 
def upperAndLower(s):
    lowerSetty = set()
    upperSetty = set()
    for letter in s: # loop over the words in the string
        if letter.islower(): # if the word is in lower
            lowerSetty.add(letter) # add to lower set 
            
        elif letter.isupper(): # if upper 
            final = chr(ord(letter)+32) # add the upper setty, but change the letter to lower
            upperSetty.add(final) 
    resulty = lowerSetty.intersection(upperSetty) # check for the intersection
    return resulty

# one weather report 
def oneWeatherReport(report1, report2):
    setty1= set()
    setty2 = set()
    for line in report1.splitlines():
        x = (line.split()) 
        if len(x) > 1:
            if line[0] != '#':
                find = line.index(':')
                setty1.add(line[:find])
    for line in report2.splitlines():
        x = (line.split()) 
        if len(x) > 1:
            if line[0] != '#':
                find = line.index(':')
                setty2.add(line[:find])
    b= setty1.difference(setty2)
    c= setty2.difference(setty1)
    return b.union(c)

# most common name 

def getCounts(L): # get the counts of and store it in a dict
    county = dict()
    for value in L: # loop over the list 
        if value not in county: # if the value(key) not yet in the dict
            county[value]=1 # give it a value of 1
        else:
            county[value]+=1 # else, add to the counter 
    return county

def mostCommonName(names):
    dicty = getCounts(names) # get the counts of names 
    maxy= 0
    commonName = set()
    for key in names: # loop over the keys in the list 
        currentCount = dicty.get(key)  # get count of the key
        if currentCount > maxy: # if the count is greater than maxy
            maxy =  currentCount # refresh the value 
            commonName = set([key])  # the set is the key
        if currentCount == maxy: # if the count is the same 
            commonName.add(key) # add the value to the common name 
    if len(commonName) == 0: 
        return None 
    elif len(commonName) == 1: # if the lenght is one 
        return commonName.pop() # return the name 
    else:
        return commonName 
    return commonName
# get hours logged 

def getHoursLogged(logs):
    ### group the times by the people 
    times = dict()
    for (time,person) in logs:
        if person not in times: # check-in time 
            times[person] = [time] # add the key 
        else : # they are in the list
            times[person].append(time) # append the ending time to the time  
    hoursLogged= dict()
    for person in times: # loop over the persons 
        checkInTime,checkOutTime = times[person] # get the times of the person
        hoursLogged[person] = abs(checkOutTime - checkInTime) # get the ours loged 
    return hoursLogged

# invert dictionary 

def invertDictionary(d):
    result = dict() # we have a result 
    for key in d: # loop over the keys 
        if d[key] in result: # is the vale of the key is in the result 
            result[d[key]].add(key) # we add the key to the value(which is now a key)
        else:
            result[d[key]] = {key}  # else, we create a key that turn the key into a value, and the value into a dict 
        

def invertDictionary2(d):
    result = dict()
    for key in d:
        currentVal =(d[key])
        setty = set()
        print(currentVal)
        for key2 in d:
            if d[key2]== currentVal:
                setty.add(key2)
                #print('WAZAAAA')
        result[currentVal] = setty
    return(result)
#spare matrix 

def sparseMatrixAdd(sm1, sm2):
    result= dict()
    maxRow =max(sm1['rows'],sm2['rows'])
    maxCol = max(sm1['cols'],sm2['cols'])
    print(maxCol,maxRow,'quaky')
    result['rows'] = maxRow # we get the max rows,and add it to the dict
    result['cols'] = maxCol # we get the max cols 
    for key in sm1: # we loop over the matrix1 
        if (key != 'rows') and (key  != 'cols'): # skip the rows and cols
            for key2 in sm2: # loop over the the keys in matrix 2 
                if (key2 != 'rows') and (key2  != 'cols'):# skip rows and cols 
                    if key2== key: # if the keys are the same 
                        # we add the values of the keys and then put is in the result 
                        result[key] =(sm2[key2] + sm1[key2])
                    else:# if the keys are not the same 
                        # if they keys are not in the resut, 
                        # we add them to the result 
                        if key not in result: 
                            result[key] = sm1[key] 
                        if key2 not in result:
                            result[key2] = sm2[key2]
    return result 
# integer frequenci 
def integerLetterFrequencies(s): # 
    county = dict() # we created a  result dictionary 
    for value in s:# we loop over the stringh
        if value.isalpha(): # if the value is part of the alpabet 
            # we make the value upper in case its lower
            value = chr(ord(value) - 32)  if value.islower() else value 
            if value not in county: # if the value is not in the dict
                county[value]=(1 / len(s)) * 100  # make a key with a value
            else: # if the value is in the dict 
                # add the fraction to the value 
                county[value]+=(1 / len(s)) * 100 
    counter = 0  
    for key in county:
            counter += county[key]
    expected_freq = math.floor(counter)
    finalcounter = 0
    for key in county:
        if finalcounter + county[key] > expected_freq:
            county[key] =math.ceil(county[key])
        else:
            county[key] = math.floor(county[key])
            finalcounter += county[key]
            print(finalcounter,expected_freq)
    return county

#count map 
def countMap(L):

    value_counts = dict() # get the count of the values in the list 
    for s in L:
        for value in s:
            value_counts[value] = value_counts.get(value,0) + 1
    
    # create the final dictionary mapping counts to sets of values 
    result = dict()
    for key in value_counts: # loop over the key in value counts
        if value_counts[key] not in result : # if the value of key is not in dict
            result[value_counts[key]] = set()  # crete a key with a empy set 
        result[value_counts[key]].add(key) # add the value to the set 
    return result
 
 # most common letter pairs 
 # this shit is a paint in the ass,   not even worth commneting on it 


def mostCommonLetterPairs(text, n):
    counter = 0
    store_pairs= dict()
    for i in range(len(text)):
        if (text[i].isalpha()) and (text[i:2+i].isalpha()):
            pair = stringIntoLower(text[i:2+i])
            if len(pair) == 2:
                store_pairs[pair] = store_pairs.get(pair,0) +1
    
    final_dict =  dict()

    if len(store_pairs) < n: return (f'{n} is too large')
    while True:
        if store_pairs == {}: break 
        killed =(next_maxi(store_pairs))
        final_dict[next_maxi(store_pairs)] = store_pairs.get(next_maxi(store_pairs))
        poty = store_pairs.pop(next_maxi(store_pairs))
        print(final_dict,'store',store_pairs,'|||||||',next_maxi(store_pairs), poty,final_dict.get(poty))
        if (len(final_dict) >= n) and (find_pooki_bear2(store_pairs,poty) == False):
           break
        elif (len(final_dict) >= n) and (find_pooki_bear(store_pairs,next_maxi(store_pairs)) == True):
           continue
    return final_dict
    
def find_pooki_bear(dicty,value):
    print('poookieee.e......')
    for key in dicty:
        if dicty[key] == dicty[value]:
            return True
    print('uppps',(value))
    return False 
    
def find_pooki_bear2(dicty,value):
    print('poookieee.e......')
    for key in dicty:
        if dicty[key] == value:
            return True
    print('uppps',(value))
    return False 
    
    
def stringIntoLower(str):
    result=''
    for letter in str:
        #print(letter)
        if letter.isupper():
            result = result + chr(ord(letter) + 32)
        else:
            result = result + letter 
    return result


def next_maxi(store_pairs):
    max_key = None
    for key in store_pairs:
        if (max_key == None):
            max_key = key 
        if  (store_pairs[key] > store_pairs[max_key]):
            max_key = key 
    return max_key

#     assert(mostCommonLetterPairs('abcbc', 1) == { 'bc':2 })
#    assert(mostCommonLetterPairs('abcbc', 2) == { 'bc':2, 'ab':1, 'cb':1 })
#    assert(mostCommonLetterPairs('abcbc', 3) == { 'bc':2, 'ab':1, 'cb':1 })
#    assert(mostCommonLetterPairs('abcbc', 4) == '4 is too large')
#    text = '''
#    "Optimism is the faith that leads to achievement.
#    Nothing can be done without hope and confidence."
#        -- HELEN KELLER
#    '''
#    assert(mostCommonLetterPairs(text, 1) == { 'th': 5 })
#    assert(mostCommonLetterPairs(text, 2) == { 'th': 5, 'le': 3, 'en': 3})
#
# containspythagorean triple 
def containsPythagoreanTriple(L):
    squares = {x**2: x for x in L} # make all the numbers of the function square
    
    for i in range(0,len(L)): # loop over the list 
        n = L[i]
        for j in range(i+1,len(L)): # go for every iteration 
            n2 = L[j]
            if (n**2+ n2**2) in squares: return True  # find the pythogras triple 
    return False 
            
        
                
def is_pythagorean(x,y,z):  ### this has O(1)
    if (x>y>z):
        return(z**2+y**2 == x**2)
    elif(y>x>z):
        return(z**2+y**2 == y**2)
    else:
        return(x**2+y**2 == z**2)
    
# get pair sum 
def getPairSum(L, target):
    in_set= set()
    for number in L:  # loop over the list 
        compliment = target - number  # get the compliment 
        if number in in_set: # if the number is in set of compliments 
            return (number,compliment) # return 
        #nevertheless add the compliment to the set 
        in_set.add(compliment)
        print(compliment,'qauky')
    return None 
    
    
    
# This helper function is used by the test function below
def isPairSum(L, target, pair):
    L = copy.copy(L)
    # Check that the pair is a tuple of length 2
    if type(pair) != tuple or len(pair) != 2: return False
    n1, n2 = pair
    # Check that the sum of the pair equals the target
    if n1 + n2 != target: return False
    # Check that both elements are in the list
    if n1 not in L: return False
    L.remove(n1)
    return n2 in L
# mathc people 
def matchPeople(people, traits):
    first_dicty = dict()
    for key in people: # looop over the keys of people 
        poty = (people[key]) # get the tuple of different traits the have
        x = poty.intersection(traits) # get the intersection of traits
        leny = len(x) # check the lenght
        first_dicty[key] = leny  # add that lenght to to a dictionary 
        
    print(first_dicty,'quaky')
    result  = dict()
    result['close matches'] = set()
    result['loose matches'] = set()
    result['no matches'] = set()
    for name in first_dicty:
        if 4 >= first_dicty[name] >=3: # add the close matches
            result['close matches'].add(name) 
        elif 2 >= first_dicty[name] >= 1:# add the loose matches 
            result['loose matches'].add(name)
        elif first_dicty[name] == 0: # add the no matches 
            result['no matches'].add(name)
            
    return result 


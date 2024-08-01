"""
Battleship Project
Name: kolikonda sushmitha
Roll No:2023501078
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows"]=10
    data["cols"]=10
    data["boardsize"]=500
    data["cellsize"]=data["boardsize"]//data["cols"]

    data["computerships"]=5
    data["userships"]=0

    data["computer"]=emptyGrid(data["rows"],data["cols"])
    data["user"]=emptyGrid(data["rows"],data["cols"])

    data["computerboard"]=addShips(data["computer"],data["computerships"])
    data["userboard"]=addShips(data["user"],data["userships"])
    data["temporaryship"]=[]
    data["turns"]=0
    data["maxiturns"]=data["boardsize"]//data["cols"]
    data["winner"]=None
    return data


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,compCanvas,data["computerboard"],showShips=False)
    drawGrid(data,userCanvas,data["userboard"],showShips=True)
    drawShip(data,userCanvas,data["temporaryship"])
    drawGameOver(data,canvas=userCanvas)
    return None

'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    if event.keysym=="Return":
        makeModel(data)


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    if board=="user":
        if data["userships"]<5:
            cell=getClickedCell(data,event)
            if cell is not None:
                clickUserBoard(data,cell[0],cell[1])
        else:
            print("already placed 5 ships")
    elif board=="comp" and data["userships"]==5:
        cell =getClickedCell(data,event)
        if cell!=None:
            runGameTurn(data,cell[0],cell[1])
    

#### STAGE 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid=[]
    for i in range(rows):
        smallgrid=[]
        for j in range(cols):
            smallgrid.append(EMPTY_UNCLICKED)
        grid.append(smallgrid)
    return grid


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    rows=random.randint(1,8)
    cols=random.randint(1,8)
    axis=random.randint(0,1)
    ship=[]
    if axis==0:
        ship.append([rows-1,cols])
        ship.append([rows,cols])
        ship.append([rows+1,cols])
    else:
        ship.append([rows,cols-1])
        ship.append([rows,cols])
        ship.append([rows,cols+1])
    return ship


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for i,j in ship:
        if grid[i][j]!=EMPTY_UNCLICKED:
            return False 
    return True


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    count=0
    while count < numShips:
        ship=createShip()
        if checkShip(grid,ship):
            for i,j in ship:
                grid[i][j]=SHIP_UNCLICKED
            count=count+1
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for i in range(data["rows"]):
        for j in range(data["cols"]):
            x0=j*data["cellsize"]
            x1=x0+data["cellsize"]
            y0=i*data["cellsize"]
            y1=y0+data["cellsize"]
            if grid[i][j]==SHIP_UNCLICKED and showShips==True:
                fillcolor="yellow"
            elif grid[i][j]==EMPTY_UNCLICKED:
                fillcolor="blue"
            elif grid[i][j]==SHIP_CLICKED:
                fillcolor="red"
            elif grid[i][j]==EMPTY_CLICKED:
                fillcolor="white"
            elif grid[i][j]==SHIP_UNCLICKED and showShips==False:
                fillcolor="blue"
            canvas.create_rectangle(x0,y0,x1,y1,fill=fillcolor)

### STAGE 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    ship.sort()
    if ship[0][1]==ship[1][1]==ship[2][1] and abs(ship[0][0]-ship[1][0])==1 and abs(ship[1][0]-ship[2][0])==1:
        return True
    return False
    


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    ship.sort()
    if ship[0][0]==ship[1][0]==ship[2][0] and abs(ship[0][1]-ship[1][1])==1 and abs(ship[1][1]-ship[2][1])==1:
      return True
    return False
'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    x=event.x
    y=event.y
    for i in range(data["rows"]):
        for j in range(data["cols"]):
            a=j*data["cellsize"]   #left
            b=(j+1)*data["cellsize"]  #right
            c=i*data["cellsize"] #top
            d=(i+1)*data["cellsize"]  #bottom 
            if a<=x<b and c<=y<d:
                    return [i,j]
    return None

'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for i,j in ship:
        x0=j*data["cellsize"]
        y0=i*data["cellsize"]
        x1=x0+data["cellsize"]
        y1=y0+data["cellsize"]
        fillcolor="white"
        canvas.create_rectangle(x0,y0,x1,y1,fill=fillcolor)
'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if len(ship)!=3:
        return False
    if not checkShip(grid,ship):
        return False
    if isVertical(ship) or isHorizontal(ship):
        return True
    return False

'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    # if data["usershipsplaced"]>5:
    #     print("placed all ships, start the game!")
    if shipIsValid(data["userboard"],data["temporaryship"]):
        for i,j in data["temporaryship"]:
            data["userboard"][i][j]=SHIP_UNCLICKED
        data["userships"]+=1
        if data["userships"]==5:
            print(" 5 ships are placed successfully")
        else:
            print("ship placement sucess!!")
        data["temporaryship"]=[]
    else:
        print("Invalid ship placement")
        data["temporaryship"]=[]
        
'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["userships"]>=5:
         print("5 ships are placed already!")
         return
    if [row,col] in data["temporaryship"]:
         return
    if len(data["temporaryship"])<3:
        data["temporaryship"].append([row,col])
    if len(data["temporaryship"])==3:
        placeShip(data)


### STAGE 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    if board[row][col]==SHIP_UNCLICKED:
        board[row][col]=SHIP_CLICKED
        if isGameOver(board):
            data["winner"]=player
    elif board[row][col]==EMPTY_UNCLICKED:
            board[row][col]=EMPTY_CLICKED
    return None


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    if data["computerboard"][row][col]==SHIP_CLICKED or data["computerboard"][row][col]==EMPTY_CLICKED:
        return
    else:
        data['computerboard'][row][col]== updateBoard(data,data["computerboard"],row,col,player="user")
    computerguess=getComputerGuess(data["userboard"])
    updateBoard(data,data["userboard"],computerguess[0],computerguess[1],player="comp")
    
    data["turns"]+=1

    if data["turns"]==data["maxiturns"]:
        data["winner"]="draw"
    


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    rows=len(board)
    cols=len(board[0])
    while True:
      row=random.randint(0,rows-1)
      col=random.randint(1,cols-1)
      if board[row][col] not in [SHIP_CLICKED,EMPTY_CLICKED]:
            return [row, col]



'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for row in board:
        for cell in row:
            if cell==SHIP_UNCLICKED:
               return False
    return True


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    # canvas.delete("all")
    
    if data["winner"] == "user":
        canvas.delete("all")
        message = '''CONGRULATIONS!!
                  USER WON THE GAME'''
        canvas.create_text(300, 40, text=message, fill="red")
    elif data["winner"] == "comp":
        canvas.delete("all")
        message = '''CONGRUATIONS!! 
                COMPUTER WON THE GAME'''
        canvas.create_text(300, 80, text="play again", fill="black")
    elif data["winner"] == "draw":
        canvas.delete("all")
        message = "TURNS COMPLETED"
        canvas.create_text(300, 40, text=message, fill="brown")

    # canvas.create_text(300, 40, text=message, fill="red")
        canvas.create_text(300, 80, text="Press enter to play again", fill="black")


 

### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":

    
    print("\n" + "#"*15 + " STAGE 1 TESTS " +  "#" * 16 + "\n")
    test.stage1Tests()
    

    ## Uncomment these for STAGE 2 ##
    
    print("\n" + "#"*15 + " STAGE 2 TESTS " +  "#" * 16 + "\n")
    test.stage2Tests()
    

    ## Uncomment these for STAGE 3 ##
    
    print("\n" + "#"*15 + " STAGE 3 TESTS " +  "#" * 16 + "\n")
    test.stage3Tests()
    

    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)

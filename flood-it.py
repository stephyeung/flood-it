#   Final Project: Flood-It! | flood-it.py
#   Written By: Stephanie Yeung, syeung1
#   15-110 Section A

from Tkinter import *
import random

def redrawAll(canvas):
    canvas.delete(ALL)
    drawBoard(canvas)
    drawColors(canvas)
    drawInstructions(canvas)
    drawScheme(canvas)

    clicks = canvas.data["clicks"]
    width = canvas.data["bWidth"]
    width_text = canvas.data["bWidth"] / 2
    height0 = canvas.data["bHeight"] / 3
    height1 = canvas.data["bHeight"] / 2

    if canvas.data["gameOver"] == True:
        canvas.create_rectangle(0, height0, width, height1, fill = "white", outline = "white")
        canvas.create_rectangle(6, height0 + 6, width - 28, height1 - 18, fill = "gray50", outline = "gray50")
        canvas.create_rectangle(8, height0 + 7, width, height1, fill = "white", outline = "white")
        canvas.create_text(width_text, height0 + 32, text = "Game Over!", font=("Arial", 28, "bold"), fill = "gray30")
        canvas.create_text(width_text, height0 + 54, text = "You have no more clicks left. Press 'r' to restart.", font=("Arial", 8), fill = "gray30")
    elif canvas.data["wonGame"] == True:
        canvas.create_rectangle(0, height0, width, height1, fill = "white", outline = "white")
        canvas.create_rectangle(6, height0 + 6, width - 28, height1 - 18, fill = "gray50", outline = "gray50")
        canvas.create_rectangle(8, height0 + 7, width, height1, fill = "white", outline = "white")
        canvas.create_text(width_text, height0 + 32, text = "Success!", font=("Arial", 28, "bold"), fill = "gray30")
        canvas.create_text(width_text, height0 + 54, text = "You flooded the board with " + str(clicks) + " step(s) to go!", font=("Arial", 8), fill = "gray30")    
    
def drawBoard(canvas):
    board = canvas.data["board"]
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            drawCell(canvas, board, row, col)
            
def drawCell(canvas, board, row, col):
    cellSize = canvas.data["cellSize"]
    left = col * cellSize
    right = left + cellSize
    top = row * cellSize
    bottom = top + cellSize
    canvas.create_rectangle(left, top, right, bottom, fill = board[row][col], outline = board[row][col])

def keyPressed(event):
    canvas = event.widget.canvas
    if (canvas.data["gameOver"] != True) and (canvas.data["wonGame"] != True):
        if (event.char == "1"):
            blockColors = ["purple", "magenta", "orange", "yellow", "green", "cyan"]
            canvas.data["blockColors"] = blockColors
            loadBoard(canvas)
            redrawAll(canvas)
        elif (event.char == "2"):
            blockColors = ["dark blue", "deep sky blue", "red3", "forest green", "lawn green", "yellow"]
            canvas.data["blockColors"] = blockColors
            loadBoard(canvas)
            redrawAll(canvas)
        elif (event.char == "3"):
            blockColors = ["grey42", "grey65", "grey82", "midnight blue", "steel blue", "sky blue"]
            canvas.data["blockColors"] = blockColors
            loadBoard(canvas)
            redrawAll(canvas)
        elif (event.char == "e"):
            rows = 10
            cols = 10
            cellSize = 30
            clicks = 20
            canvas.data["rows"] = rows
            canvas.data["cols"] = cols
            canvas.data["cellSize"] = cellSize
            canvas.data["clicks"] = clicks
            loadBoard(canvas)
            redrawAll(canvas)
        elif (event.char == "a"):
            rows = 15
            cols = 15
            cellSize = 20
            clicks = 32
            canvas.data["rows"] = rows
            canvas.data["cols"] = cols
            canvas.data["cellSize"] = cellSize
            canvas.data["clicks"] = clicks
            loadBoard(canvas)
            redrawAll(canvas)
        elif (event.char == "h"):
            rows = 20
            cols = 20
            cellSize = 15
            clicks = 54
            canvas.data["rows"] = rows
            canvas.data["cols"] = cols
            canvas.data["cellSize"] = cellSize
            canvas.data["clicks"] = clicks
            loadBoard(canvas)
            redrawAll(canvas)
    if (event.char == "r"):
        init(canvas)

def getColorClicked(event):
    canvas = event.widget.canvas
    clicks = canvas.data["clicks"]
    board = canvas.data["board"]
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    blockColors = canvas.data["blockColors"]
    clickBound_x = event.x
    clickBound_y = event.y
    oldColor = board[0][0]
    if (clicks > 0) and (canvas.data["wonGame"] != True):
        if (clickBound_y >= 308) and (clickBound_y <= 348):
            if (clickBound_x >= 8) and (clickBound_x <= 48):
                clicks -= 1
                flood(canvas, board, oldColor, blockColors[0], 0, 0)
                board[0][0] = blockColors[0]
                redrawAll(canvas)
            elif (clickBound_x >= 56) and (clickBound_x <= 96):
                clicks -= 1
                flood(canvas, board, oldColor, blockColors[1], 0, 0)
                board[0][0] = blockColors[1]
                redrawAll(canvas)
            elif (clickBound_x >= 104) and (clickBound_x <= 144):
                clicks -= 1
                flood(canvas, board, oldColor, blockColors[2], 0, 0)
                board[0][0] = blockColors[2]
                redrawAll(canvas)
            elif (clickBound_x >= 152) and (clickBound_x <= 192):
                clicks -= 1
                flood(canvas, board, oldColor, blockColors[3], 0, 0)
                board[0][0] = blockColors[3]
                redrawAll(canvas)
            elif (clickBound_x >= 200) and (clickBound_x <= 240):
                clicks -= 1
                flood(canvas, board, oldColor, blockColors[4], 0, 0)
                board[0][0] = blockColors[4]
                redrawAll(canvas)
            elif (clickBound_x >= 248) and (clickBound_x <= 288):
                clicks -= 1
                flood(canvas, board, oldColor, blockColors[5], 0, 0)
                board[0][0] = blockColors[5]
                redrawAll(canvas)
            
            completeBoard = True
            for x in range(rows):
                for y in range(cols):
                    if board[x][y] != board[0][0]:
                        completeBoard = False
                        break
            if completeBoard:
                wonGame(canvas)
            elif (clicks == 0) and (completeBoard == False):
                gameOver(canvas)
    canvas.data["clicks"] = clicks
    redrawAll(canvas)

def flood(canvas, board, oldColor, newColor, x, y):
    if board[x][y] != oldColor or oldColor == newColor:
        return
    else:
        rows = canvas.data["rows"]
        cols = canvas.data["cols"]
        board[x][y] = newColor
        if x > 0:
            flood(canvas, board, oldColor, newColor, x - 1, y)
        if x < rows - 1:
            flood(canvas, board, oldColor, newColor, x + 1, y)
        if y > 0:
            flood(canvas, board, oldColor, newColor, x, y - 1)
        if y < cols - 1:
            flood(canvas, board, oldColor, newColor, x, y + 1)    

def drawColors(canvas):
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    cellSize = canvas.data["cellSize"]
    blockColors = canvas.data["blockColors"]
    radius = 40
    gap = 8
    top = rows * cellSize + gap
    bottom = top + radius
    left0 = gap
    right0 = gap + radius
    lenColors = len(blockColors)

    for i in range(lenColors):
        left = left0 + i*radius + i*gap
        right = right0 + i*radius + i*gap
        canvas.create_oval(left, top, right, bottom, fill = blockColors[i], outline = blockColors[i])
        canvas.create_oval(left + 3, top + 3, right - 5, bottom -5, fill = "white", outline = "white")
        canvas.create_oval(left + 4, top + 4, right - 4, bottom - 4, fill = blockColors[i], outline = blockColors[i])

def gameOver(canvas):
    canvas.data["gameOver"] = True
    
    totalGame = canvas.data["totalGame"]
    totalGame += 1
    canvas.data["totalGame"] = totalGame

def wonGame(canvas):
    canvas.data["wonGame"] = True
    
    wonGames = canvas.data["wonGames"]
    wonGames += 1
    canvas.data["wonGames"] = wonGames
    
    totalGame = canvas.data["totalGame"]
    totalGame += 1
    canvas.data["totalGame"] = totalGame
    
def loadBoard(canvas):
    cellSize = canvas.data["cellSize"]
    rows = 300 / cellSize
    cols = 300 / cellSize
    blockColors = canvas.data["blockColors"]
    board = [ ]
    for x in range(rows):
        column = [ ]
        for y in range(cols):
            column.append(random.choice(blockColors))
        board.append(column)
    canvas.data["board"] = board

def drawInstructions(canvas):
    text_x = canvas.data["bWidth"] / 2
    text_y = canvas.data["bHeight"] - 73
    text_y1 = canvas.data["bHeight"] - 53
    text_x2 = canvas.data["bWidth"] / 2
    text_y2 = canvas.data["bHeight"] - 24
    bWidth= canvas.data["bWidth"]
    bHeight = canvas.data["bHeight"]
    clicks = canvas.data["clicks"]
    canvas.create_rectangle(0, text_y1 - 10, bWidth, bHeight, fill = "white", outline = "white")
    canvas.create_text(text_x, text_y, text = "Clicks Left: " + str(clicks), font=("Arial", 8), fill = "gray30")
    canvas.create_text(text_x, text_y1, text = "Instructions: ", font=("Arial", 8, "bold"), fill = "gray30")
    canvas.create_text(text_x2, text_y2, text = "The objective is to FLOOD the screen with pixels of the\nsame color. Start at the top left and click a button to\nchange the color, and your flood area will also grow.", font=("Arial", 8), fill = "gray30")

def drawScheme(canvas):
    x0 = canvas.data["bWidth"]
    x1 = x0 + 100
    y1 = canvas.data["bHeight"]
    text_x1 = x0 + (x1 - x0)/2
    color_x = x0 + 28
    canvas.create_rectangle(x0, 0, x1, y1, fill = "gray85", outline = "gray80")
    canvas.create_text(text_x1, 25, text = "Color Options:", font=("Arial", 8, "bold"), fill = "gray30")
    canvas.create_text(text_x1, 40, text = "(Press Key #)", font=("Arial", 8), fill = "gray30")
    
    ## Default: Purple, Magenta, Orange, Yellow, Green, Cyan
    canvas.create_text(text_x1, 60, text = "1.", font=("Arial", 8), fill = "gray30")
    canvas.create_rectangle(color_x, 75, color_x + 15, 90, fill = "purple", outline = "purple")
    canvas.create_rectangle(color_x + 15, 75, color_x + 30, 90, fill = "magenta", outline = "magenta")
    canvas.create_rectangle(color_x + 30, 75, color_x + 45, 90, fill = "orange", outline = "orange")
    canvas.create_rectangle(color_x, 90, color_x + 15, 105, fill = "yellow", outline = "yellow")
    canvas.create_rectangle(color_x + 15, 90, color_x + 30, 105, fill = "green", outline = "green")
    canvas.create_rectangle(color_x + 30, 90, color_x + 45, 105, fill = "cyan", outline = "cyan")

    ## Tartan (?) : Dark Blue, Deep Sky Blue, Maroon, Forest Green, Dark Olive Green, Yellow
    canvas.create_text(text_x1, 130, text = "2.", font=("Arial", 8), fill = "gray30")
    canvas.create_rectangle(color_x, 145, color_x + 15, 160, fill = "dark blue", outline = "dark blue")
    canvas.create_rectangle(color_x + 15, 145, color_x + 30, 160, fill = "deep sky blue", outline = "deep sky blue")
    canvas.create_rectangle(color_x + 30, 145, color_x + 45, 160, fill = "red3", outline = "red3")
    canvas.create_rectangle(color_x, 160, color_x + 15, 175, fill = "forest green", outline = "forest green")
    canvas.create_rectangle(color_x + 15, 160, color_x + 30, 175, fill = "lawn green", outline = "lawn green")
    canvas.create_rectangle(color_x + 30, 160, color_x + 45, 175, fill = "yellow", outline = "yellow")
    
    ## Blues: Gray95, Gray70, Gray45, Midnight Blue, Steel Blue, Sky Blue
    canvas.create_text(text_x1, 200, text = "3.", font=("Arial", 8), fill = "gray30")
    canvas.create_rectangle(color_x, 215, color_x + 15, 230, fill = "gray82", outline = "gray82")
    canvas.create_rectangle(color_x + 15, 215, color_x + 30, 230, fill = "gray65", outline = "gray65")
    canvas.create_rectangle(color_x + 30, 215, color_x + 45, 230, fill = "gray42", outline = "gray42")
    canvas.create_rectangle(color_x, 230, color_x + 15, 245, fill = "midnight blue", outline = "midnight blue")
    canvas.create_rectangle(color_x + 15, 230, color_x + 30, 245, fill = "steel blue", outline = "steel blue")
    canvas.create_rectangle(color_x + 30, 230, color_x + 45, 245, fill = "sky blue", outline = "sky blue")

    canvas.create_text(text_x1, 280, text = "Other Keys: ", font=("Arial", 8, "bold"), fill = "gray30")
    canvas.create_text(text_x1, 296, text = "' r ' | Reset", font=("Arial", 8), fill = "gray30")
    canvas.create_text(text_x1, 312, text = "' h ' | Hard", font=("Arial", 8), fill = "gray30")
    canvas.create_text(text_x1, 327, text = "' a ' | Average", font=("Arial", 8), fill = "gray30")
    canvas.create_text(text_x1, 342, text = "' e ' | Easy", font=("Arial", 8), fill = "gray30")

    wonGames = canvas.data["wonGames"]
    totalGame = canvas.data["totalGame"]
    canvas.create_text(text_x1, 370, text = "Session Wins:", font=("Arial", 8, "bold"), fill = "gray30")
    canvas.create_text(text_x1, 386, text = str(wonGames) + " out of " + str(totalGame), font=("Arial", 8), fill = "gray30")
    
def init(canvas):
    blockColors = ["purple", "magenta", "orange", "yellow", "green", "cyan"]
    canvas.data["blockColors"] = blockColors
    canvas.data["clicks"] = 32
    canvas.data["gameOver"] = False
    canvas.data["wonGame"] = False
    canvas.data["rows"] = 15
    canvas.data["cols"] = 15
    canvas.data["cellSize"] = 20
    loadBoard(canvas)
    redrawAll(canvas)

def run(rows, cols):
    root = Tk()
    root.title("Flood-It!")
    cellSize = 20
    wonGames = 0
    totalGame = 0
    bWidth = cols * cellSize + 100
    bHeight = rows * cellSize + 133
    canvas = Canvas(root, width = bWidth, height = bHeight)
    canvas.pack()
    root.resizable(width = 0, height = 0)
    root.canvas = canvas.canvas = canvas
    canvas.data = {}
    canvas.data["bWidth"] = bWidth - 100
    canvas.data["bHeight"] = bHeight
    canvas.data["rows"] = rows
    canvas.data["cols"] = cols
    canvas.data["cellSize"] = cellSize
    canvas.data["wonGames"] = wonGames
    canvas.data["totalGame"] = totalGame
    
    init(canvas)

    root.bind("<Button-1>", getColorClicked)
    root.bind("<Key>", keyPressed)
    
    root.mainloop()

run(15, 15)

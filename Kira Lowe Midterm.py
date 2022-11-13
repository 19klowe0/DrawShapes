import pygame
from sys import exit
import math
import subprocess
import os
import sys

width = 800
height = 700
pygame.init()

screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("Trace a Picture!")
#read in pictures
elipse_image = pygame.image.load('elipse_image.png')
triangle_image = pygame.image.load('triangle_image.png')
rectangle_image = pygame.image.load('rectangle_image.png')
save_image = pygame.image.load('save_image.png')
bezier_image = pygame.image.load('bezier_image.png')
circle_image = pygame.image.load('circle_image.png')
line_image = pygame.image.load('line_image.png')
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
image = pygame.image.load('bezier_image.png')
path = "C:"

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
dark_green = (21, 71, 52)

current_color = (0, 0, 0)

pts = []
knots = []
count = 0
screen.fill(WHITE)

clock = pygame.time.Clock()

def clearAndRedraw():
    #print("tes")
    #pygame.draw.rect(screen, WHITE, (0,0,590,height))
    screen.fill(WHITE)
    #Line and rects
    for i in range(count -1):
        pygame.draw.line(screen, GREEN, pts[i], pts[i+1], 3)
    for i in range(count):
        pygame.draw.rect(screen, BLUE, (pts[i][0] - margin, pts[i][1] - margin, 2 * margin, 2 * margin), 5)

    #Buttons
    lineButton.draw(screen, (0, 0, 0))
    bezierButton.draw(screen, (0, 0, 0))
    triangleButton.draw(screen, (0, 0, 0))
    circleButton.draw(screen, (0, 0, 0))
    rectangleButton.draw(screen, (0, 0, 0))
    insertButton(screen, (0,0,0))

    #Text
    if buttonCheck == 1:
        curveType = "Draw Type: Line"
    elif buttonCheck == 2 or buttonCheck == -1:
        curveType = "Draw Type: Bezier"
    elif buttonCheck == 3:
        curveType = "Draw Type: Triangle"
    elif buttonCheck == 4:
        curveType = "Draw Type: Circle"
    else:
        curveType = "Draw Type: Rectangle"


    font = pygame.font.Font("freesansbold.ttf", 15)
    curveText = font.render(curveType, True, BLACK)
    screen.blit(curveText, (5,5))

def point(pX, pY, pWidth, pHeight, pColor):
    pygame.draw.rect(screen, pColor, [pX, pY, pWidth, pHeight])

def DrawBezier(currentColor):
    print("draw bezier")
    color = RED
    thick = 3
    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, 150, 30))

    font = pygame.font.Font("freesansbold.ttf", 15)
    curveText = font.render("Draw a Beziar", True, BLACK)
    screen.blit(curveText, (5, 5))
    pygame.display.update()
    count1 = 0
    while count1 < 4:
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x < 590:
                    # pygame.draw.rect(screen, BLUE, (pt[0] - margin, pt[1] - margin, 2 * margin, 2 * margin), 5)
                    if count1 == 0:
                        pt1 = [x, y]
                        pygame.draw.rect(screen, BLUE, (pt1[0] - margin, pt1[1] - margin, 2 * margin, 2 * margin), 5)
                        pygame.display.update()
                    if count1 == 1:
                        pt2 = [x, y]
                        pygame.draw.rect(screen, BLUE, (pt2[0] - margin, pt2[1] - margin, 2 * margin, 2 * margin), 5)
                        pygame.display.update()
                    if count1 == 2:
                        pt3 = [x, y]
                        pygame.draw.rect(screen, BLUE, (pt3[0] - margin, pt3[1] - margin, 2 * margin, 2 * margin), 5)
                        pygame.display.update()
                    if count1 == 3:
                        pt4 = [x, y]
                        pygame.draw.rect(screen, WHITE, (pt1[0] - margin, pt1[1] - margin, 2 * margin, 2 * margin), 5)
                        pygame.draw.rect(screen, WHITE, (pt2[0] - margin, pt2[1] - margin, 2 * margin, 2 * margin), 5)
                        pygame.draw.rect(screen, WHITE, (pt3[0] - margin, pt3[1] - margin, 2 * margin, 2 * margin), 5)
                    count1 += 1

    px = [pt1[0], pt2[0], pt3[0], pt4[0]]
    py = [pt1[1], pt2[1], pt3[1], pt4[1]]
    return [5, px, py, currentColor]
def drawRectangle(currentColor):
    print("draw Rectangle")
    pygame.draw.rect(screen, WHITE, pygame.Rect(0,0,150 ,30))

    font = pygame.font.Font("freesansbold.ttf", 15)
    curveText = font.render("Draw a Rectangle", True, BLACK)
    screen.blit(curveText, (5, 5))
    pygame.display.update()

    color = BLUE
    thick = 3
    count1 = 0
    while count1 < 2:
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            pt = [x, y]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x < 590:
                    pts.append(pt)
                    # pygame.draw.rect(screen, BLUE, (pt[0] - margin, pt[1] - margin, 2 * margin, 2 * margin), 5)
                    if count1 == 0:
                        pt1 = [x, y]
                        pygame.draw.rect(screen, BLUE, (pt1[0] - margin, pt1[1] - margin, 2 * margin, 2 * margin), 5)
                        pygame.display.update()
                    if count1 == 1:
                        pt2 = [x, y]
                        pygame.draw.rect(screen, WHITE, (pt1[0] - margin, pt1[1] - margin, 2 * margin, 2 * margin), 5)
                        pygame.display.update()
                    count1 += 1
    pt3 = [pt1[0], pt2[1]]
    pt4 = [pt2[0], pt1[1]]
    return [3, pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1], pt4[0], pt4[1], currentColor]

def drawTriangle(currentColor):
    color = RED
    thick = 3
    print("draw Triangle")
    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, 150, 30))

    font = pygame.font.Font("freesansbold.ttf", 15)
    curveText = font.render("Draw a Triangle", True, BLACK)
    screen.blit(curveText, (5, 5))
    pygame.display.update()
    count1 = 0
    while count1 < 3:
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            pt = [x, y]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x < 590:
                    #pygame.draw.rect(screen, BLUE, (pt[0] - margin, pt[1] - margin, 2 * margin, 2 * margin), 5)
                    if count1 == 0:
                        pt1 = [x, y]
                        pygame.draw.rect(screen, BLUE, (pt1[0] - margin, pt1[1] - margin, 2 * margin, 2 * margin), 5)
                        pygame.display.update()
                    if count1 == 1:
                        pt2 = [x, y]
                        pygame.draw.rect(screen, BLUE, (pt2[0] - margin, pt2[1] - margin, 2 * margin, 2 * margin), 5)
                        pygame.display.update()
                    if count1 == 2:
                        pt3 = [x, y]
                        pygame.draw.rect(screen, WHITE, (pt1[0] - margin, pt1[1] - margin, 2 * margin, 2 * margin), 5)
                        pygame.draw.rect(screen, WHITE, (pt2[0] - margin, pt2[1] - margin, 2 * margin, 2 * margin), 5)
                    count1 += 1
    return [2, pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1], currentColor]

def drawLine(currentColor):
    print("draw Line")
    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, 150, 30))

    font = pygame.font.Font("freesansbold.ttf", 15)
    curveText = font.render("Draw a Line", True, BLACK)
    screen.blit(curveText, (5, 5))
    pygame.display.update()
    #loop unitl the player clicks two spots
    count1 = 0
    while count1 < 2:
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            pt = [x, y]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x < 590:
                    #pygame.draw.rect(screen, BLUE, (pt[0] - margin, pt[1] - margin, 2 * margin, 2 * margin), 5)
                    if count1 == 0:
                        pt1 = [x,y]
                        pygame.draw.rect(screen, BLUE, (pt1[0] - margin, pt1[1] - margin, 2 * margin, 2 * margin), 5)
                        pygame.display.update()
                    if count1 == 1:
                        pygame.draw.rect(screen, WHITE, (pt1[0] - margin, pt1[1] - margin, 2 * margin, 2 * margin), 5)
                        pt2 = [x,y]
                    count1 += 1
    return [1, pt1[0], pt1[1], pt2[0], pt2[1], currentColor]



def drawCircle(currentColor):
    print("draw Circle")
    color = BLACK
    thick = 3
    count1 = 0
    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, 150, 30))

    font = pygame.font.Font("freesansbold.ttf", 15)
    curveText = font.render("Draw a Circle", True, BLACK)
    screen.blit(curveText, (5, 5))
    pygame.display.update()
    while count1 < 2:
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            pt = [x, y]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x < 590:
                    # pygame.draw.rect(screen, BLUE, (pt[0] - margin, pt[1] - margin, 2 * margin, 2 * margin), 5)
                    if count1 == 0:
                        pt1 = [x, y]
                        pygame.draw.rect(screen, BLUE, (pt1[0] - margin, pt1[1] - margin, 2 * margin, 2 * margin), 5)
                        pygame.display.update()
                    if count1 == 1:
                        pygame.draw.rect(screen, WHITE, (pt1[0] - margin, pt1[1] - margin, 2 * margin, 2 * margin), 5)
                        pt2 = [x, y]
                    count1 += 1
    r = math.sqrt(((pt2[0] - pt1[0]) * (pt2[0] - pt1[0])) + (pt2[1] - pt1[1]) * (pt2[1] - pt1[1]))
    return [4, r, r, pt1[0], pt1[1], currentColor]


def drawElipse(currentColor):
    print("draw Elipse")
    color = BLACK
    thick = 3
    count1 = 0
    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, 150, 30))

    font = pygame.font.Font("freesansbold.ttf", 15)
    curveText = font.render("Draw a Elipse", True, BLACK)
    screen.blit(curveText, (5, 5))
    pygame.display.update()
    while count1 < 3:
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            pt = [x, y]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x < 590:
                    if count1 == 0:
                        pt1 = [x, y]
                        pygame.draw.rect(screen, BLUE, (pt1[0] - margin, pt1[1] - margin, 2 * margin, 2 * margin), 5)
                        pygame.display.update()
                    if count1 == 1:
                        pt2 = [x, y]
                        pygame.draw.rect(screen, BLUE, (pt2[0] - margin, pt2[1] - margin, 2 * margin, 2 * margin), 5)
                        pygame.display.update()
                    if count1 == 2:
                        pt3 = [x, y]
                        pygame.draw.rect(screen, WHITE, (pt1[0] - margin, pt1[1] - margin, 2 * margin, 2 * margin), 5)
                        pygame.draw.rect(screen, WHITE, (pt2[0] - margin, pt2[1] - margin, 2 * margin, 2 * margin), 5)
                        pygame.display.update()
                    count1 += 1
    r = math.sqrt(((pt2[0] - pt1[0]) * (pt2[0] - pt1[0])) + (pt2[1] - pt1[1]) * (pt2[1] - pt1[1]))
    r1 = math.sqrt(((pt3[0] - pt1[0]) * (pt3[0] - pt1[0])) + (pt3[1] - pt1[1]) * (pt3[1] - pt1[1]))
    return [4, r, r1, pt1[0], pt1[1], currentColor]

def insertLayer():
    #opens the file explorer
    print("insert")
    subprocess.Popen('explorer')

def insertPicture(path):
    #adds the picture to the canvas
    added_image = pygame.image.load(path)
    return added_image


class button():
    def __init__(self, color, x, y, width, height, text):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            if (self.text == "Insert"):
                font = pygame.font.SysFont('comicsans', 20)
                text = font.render(self.text, 1, (0, 0, 0))
                win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
            else:
                win.blit(self.text, (self.x + (self.width / 2 - self.text.get_width() / 2), self.y + (self.height / 2 - self.text.get_height() / 2)))




    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


# Takes rectangle's size, position and a point. Returns true if that
# point is inside the rectangle and false if it isnt.
def pointInRectanlge(px, py, rw, rh, rx, ry):
    if px > rx and px < rx + rw:
        if py > ry and py < ry + rh:
            return True
    return False


# Blueprint to make sliders in the game
class Slider:
    def __init__(self, position, upperValue: int = 255, sliderWidth: int = 0,
                 text: str = "", outlineSize: tuple = (150, 10))-> None:
        self.position = position
        self.outlineSize = outlineSize
        self.text = text
        self.sliderWidth = sliderWidth
        self.upperValue = upperValue

    # returns the current value of the slider
    def getValue(self) -> float:
        return self.sliderWidth / (self.outlineSize[0] / self.upperValue)

    # renders slider and the text showing the value of the slider
    def render(self, display: pygame.display) -> None:
        # draw outline and slider rectangles
        pygame.draw.rect(display, (0,0,0), (self.position[0], self.position[1], self.outlineSize[0], self.outlineSize[1]), 3)

        pygame.draw.rect(display, (0,0,0), (self.position[0], self.position[1], self.sliderWidth, self.outlineSize[1]))

        # determine size of font
        self.font = pygame.font.Font(pygame.font.get_default_font(), int((1.5) * self.outlineSize[1]))

        # create text surface with value
        if (self.position == (650, 150)):
            valueSurf = self.font.render(f"{self.text}: {round(self.getValue())}", True, (self.getValue(), 0, 0))
        elif (self.position == (650, 190)):
            valueSurf = self.font.render(f"{self.text}: {round(self.getValue())}", True, (0, self.getValue(), 0))
        elif (self.position == (650, 230)):
            valueSurf = self.font.render(f"{self.text}: {round(self.getValue())}", True, (0, 0, self.getValue()))
        else:
            valueSurf = self.font.render(f"{self.text}: {round(self.getValue())}", True, (0, 0, self.getValue()))

        # centre text
        textx = self.position[0] + (self.outlineSize[0] / 2) - (valueSurf.get_rect().width / 2)
        texty = self.position[1] + (self.outlineSize[1] / 2) - (valueSurf.get_rect().height / 2 -15)

        display.blit(valueSurf, (textx, texty))

    # allows users to change value of the slider by dragging it.
    def changeValue(self) -> None:
        # If mouse is pressed and mouse is inside the slider
        mousePos = pygame.mouse.get_pos()
        if pointInRectanlge(mousePos[0], mousePos[1], self.outlineSize[0], self.outlineSize[1], self.position[0], self.position[1]):
            if pygame.mouse.get_pressed()[0]:
                # the size of the slider
                self.sliderWidth = mousePos[0] - self.position[0]

                # limit the size of the slider
                if self.sliderWidth < 1:
                    self.sliderWidth = 0
                if self.sliderWidth > self.outlineSize[0]:
                    self.sliderWidth = self.outlineSize[0]


slider = Slider((650, 150))
slider_1 = Slider((650, 190))
slider_2 = Slider((650, 230))
slider_Width = Slider((450, 10))

def insertFreeLine(currentColor):
    print("inserting free line")

    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, 150, 30))

    font = pygame.font.Font("freesansbold.ttf", 15)
    curveText = font.render("Draw a Free Line", True, BLACK)
    screen.blit(curveText, (5, 5))

    freeLineCloseButton.draw(screen, (0, 0, 0))

    slider_Width.changeValue()
    slider_Width.render(screen)

    pygame.display.update()

    global drawing, last_pos, w
    lineArray = []
    count = 0
    while count < 1:
        for event in pygame.event.get():
            slider_Width.changeValue()
            pygame.draw.rect(screen, WHITE, pygame.Rect(450, 10, 150, 30))
            w = int(slider_Width.getValue())
            if w == 0:
                w = 1
            slider_Width.render(screen)
            mouse_position = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                if (drawing):
                    mouse_position = pygame.mouse.get_pos()
                    if last_pos is not None:
                        pygame.draw.line(screen, current_color, last_pos, mouse_position, w)
                        pygame.display.update()
                        lineArray.append((last_pos, mouse_position, w))
                    last_pos = mouse_position
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_position = (0, 0)
                drawing = False
                last_pos = None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if freeLineCloseButton.isOver(mouse_position):
                    return [9, lineArray, currentColor]
                else:
                    drawing = True



    #Button Class


def Capture(display,name,pos,size):
    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, 150, 30))
    image = pygame.Surface(size)
    image.blit(display,(0,0),(pos,size))  # Blit portion of the display to the image
    pygame.image.save(image,name)  # Save the image to the disk

# Loop until the user clicks the close button.
done = False
pressed = 0
margin = 6
old_pressed = 0
old_button1 = 0
old_button3 = 0

selectedPoint = -1
eclipseButton = button((255,165,165),650,10,20,10,"Elipse") #def __init__(self, color, x, y, width, height, text=''):
lineButton = button((255,165,0),650,100,120,70,"Line")
bezierButton = button((0,255,0),650,200,120,70,"Bezier")
triangleButton = button((255,255,0),650,300,120,70,"Triangle")
circleButton = button((255,255,255),650,400,120,70,"Circle")
rectangleButton = button((255,0,255),650,500,120,70,"Rectangle")
captureButton = button((255,0,255),650,600,120,70,"Save")
insertButton = button((255,0,255),650, 600,120,70, "Insert")
freeLineButton = button((255,165,165),650,10,20,10,"freeline")
freeLineCloseButton = button((0, 255, 0), 658, 74, 30, 30, bezier_image)


buttonCheck = -1

drawing = False
last_pos = None
w = 1


def game_loop():
    gameExit = False
    print("Inside game_loop")
    scale = 1
    scale_change = 0
    pX_change = 0
    pX_direction = 0
    pY_change = 0
    pY_direction = 0
    arrayForPoints = []
    current_color = (0, 0, 0)


    m = [[-1, 3, -3, 1],
         [3, -6, 3, 0],
         [-3, 3, 0, 0],
         [1, 0, 0, 0]]

    pxm = [0, 0, 0, 0]
    pym = [0, 0, 0, 0]
    tm = [1, 1, 1, 1]


    pressed = 0
    margin = 6
    old_pressed = 0
    old_button1 = 0
    old_button3 = 0

    selectedPoint = -1
    #first line
    eclipseButton = button((255, 165, 165), 690, 10, 30, 30, elipse_image)
    circleButton = button((160, 150, 255), 722, 10, 30, 30, circle_image)
    triangleButton = button((255, 255, 0), 754, 10, 30, 30, triangle_image)
    captureButton = button((255, 0, 0), 658, 10, 30, 30, save_image)
    #second
    lineButton = button((255, 165, 0), 690, 42, 30, 30, line_image)
    bezierButton = button((0, 255, 0), 722, 42, 30, 30, bezier_image)
    rectangleButton = button((255, 0, 255), 754, 42, 30, 30, rectangle_image)
    freeLineButton = button((0, 255, 0), 658, 42, 30, 30, bezier_image)
    freeLineCloseButton = button((0, 255, 0), 658, 54, 30, 30, bezier_image)


    insertButton = button((190,53,109), 675, 270, 100, 30, "Insert")
    image = pygame.image.load('Insert.png')


    while not gameExit:
        eclipseButton.draw(screen, (0, 0, 0))
        lineButton.draw(screen, (0, 0, 0))
        bezierButton.draw(screen, (0, 0, 0))
        triangleButton.draw(screen, (0, 0, 0))
        circleButton.draw(screen, (0, 0, 0))
        rectangleButton.draw(screen, (0, 0, 0))
        captureButton.draw(screen, (0, 0, 0))
        insertButton.draw(screen, (0, 0, 0))
        freeLineButton.draw(screen, (0, 0, 0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = -1
                if lineButton.isOver(pos):
                    buttonCheck = 1
                    arrayForPoints.append(drawLine(current_color))
                elif bezierButton.isOver(pos):
                    buttonCheck = 2
                    arrayForPoints.append(DrawBezier(current_color))
                elif triangleButton.isOver(pos):
                    buttonCheck = 3
                    arrayForPoints.append(drawTriangle(current_color))
                elif circleButton.isOver(pos):
                    buttonCheck = 4
                    arrayForPoints.append(drawCircle(current_color))
                elif rectangleButton.isOver(pos):
                    buttonCheck = 5
                    arrayForPoints.append(drawRectangle(current_color))
                elif eclipseButton.isOver(pos):
                    buttonCheck = 6
                    arrayForPoints.append(drawElipse(current_color))
                elif freeLineButton.isOver(pos):
                    buttonCheck = 9
                    arrayForPoints.append(insertFreeLine(current_color))
                elif captureButton.isOver(pos):
                    buttonCheck = 7
                    Capture(screen, "ArtWork.png", (0, 0), (600, 700))
                elif insertButton.isOver(pos):
                    buttonCheck = 8
                    insertLayer()

            elif event.type == pygame.MOUSEBUTTONUP:
                pressed = 1
            else:
                pressed = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    scale_change = .1
                elif event.key == pygame.K_s:
                    scale_change = -.1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    scale_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pX_direction = -2
                elif event.key == pygame.K_RIGHT:
                    pX_direction = 2

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pY_direction = -2
                elif event.key == pygame.K_DOWN:
                    pY_direction = 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    pX_direction = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    pY_direction = 0
            if event.type == pygame.DROPFILE:
                file_extension = os.path.splitext(event.file)[1]
                if file_extension in [".bmp", ".jpg", ".png", ".PNG"]:
                    image = pygame.image.load(event.file)  # load the image given the file name.
                    print(event.file)


        pX_change = pX_change + pX_direction
        pY_change = pY_change + pY_direction
        screen.fill(white)

        screen.blit(image, (50, 50))
        eclipseButton.draw(screen, (0, 0, 0))
        lineButton.draw(screen, (0, 0, 0))
        bezierButton.draw(screen, (0, 0, 0))
        triangleButton.draw(screen, (0, 0, 0))
        circleButton.draw(screen, (0, 0, 0))
        rectangleButton.draw(screen, (0, 0, 0))
        captureButton.draw(screen, (0, 0, 0))
        insertButton.draw(screen, (0,0,0))
        freeLineButton.draw(screen, (0, 0, 0))

        if scale + scale_change > 1:
            scale = scale + scale_change
        r = int(800 / scale)

        i = 0
        pxm = [0, 0, 0, 0]
        pym = [0, 0, 0, 0]
        pxms = []
        pyms = []

        for c in arrayForPoints:
            if c[0] == 5:
                while i < 4:
                    j = 0
                    while j < 4:
                        print(c[1][j])
                        pxm[i] = pxm[i] + c[1][j] * m[j][i]
                        pym[i] = pym[i] + c[2][j] * m[j][i]
                        j = j + 1
                    i = i + 1
                pxms.append(pxm)
                pyms.append(pym)
        t_begin = 0
        t_end = 2 * math.pi * scale
        sT_begin = t_begin * scale
        sT_end = t_end * scale
        sT = sT_begin
        while sT <= sT_end:
            #line segments = 1, triangles = 2, rectangles = 3, ellipse = 6 circles= 4, and Bezier curves = 5.
            for a in arrayForPoints:
                if (a[0] == 2):
                    if sT <= 1:
                        t = sT
                        xQ0 = (1 - t) * a[1] + t * a[3]
                        yQ0 = (1 - t) * a[2] + t * a[4]
                        pX = (xQ0 * scale) + pX_change
                        pY = (yQ0 * scale) + pY_change
                        point(pX, pY, 3, 3, a[len(a)-1])

                        xQ1 = (1 - t) * a[3] + t * a[5]
                        yQ1 = (1 - t) * a[4] + t * a[6]
                        pX = (xQ1 * scale) + pX_change
                        pY = (yQ1 * scale) + pY_change
                        point(pX, pY, 3, 3, a[len(a)-1])

                        xQ2 = (1 - t) * a[5] + t * a[1]
                        yQ2 = (1 - t) * a[6] + t * a[2]
                        pX = (xQ2 * scale) + pX_change
                        pY = (yQ2 * scale) + pY_change
                        point(pX, pY, 3, 3, a[len(a)-1])
                if (a[0]== 1):
                    if sT <= 1:
                        t = sT
                        xQ0 = (1 - t) * a[1] + t * a[3]
                        yQ0 = (1 - t) * a[2] + t * a[4]
                        pX = (xQ0 * scale) + pX_change
                        pY = (yQ0 * scale) + pY_change
                        point(pX, pY, 3, 3, a[len(a)-1])

                if (a[0] == 3):
                    if sT <= 1:
                        t = sT
                        xQ0 = (1 - t) * a[1] + t * a[5]
                        yQ0 = (1 - t) * a[2] + t * a[6]
                        pX = (xQ0 * scale) + pX_change
                        pY = (yQ0 * scale) + pY_change
                        point(pX, pY, 3, 3, a[len(a)-1])

                        xQ1 = (1 - t) * a[3] + t * a[5]
                        yQ1 = (1 - t) * a[4] + t * a[6]
                        pX = (xQ1 * scale) + pX_change
                        pY = (yQ1 * scale) + pY_change
                        point(pX, pY, 3, 3, a[len(a)-1])

                        xQ2 = (1 - t) * a[1] + t * a[7]
                        yQ2 = (1 - t) * a[2] + t * a[8]
                        pX = (xQ2 * scale) + pX_change
                        pY = (yQ2 * scale) + pY_change
                        point(pX, pY, 3, 3, a[len(a)-1])

                        xQ2 = (1 - t) * a[3] + t * a[7]
                        yQ2 = (1 - t) * a[4] + t * a[8]
                        pX = (xQ2 * scale) + pX_change
                        pY = (yQ2 * scale) + pY_change
                        point(pX, pY, 3, 3, a[len(a)-1])
                if(a[0] == 4 or a[0] == 6):
                    t = sT / scale
                    x = a[1] * math.cos(t)* scale
                    y = a[2] * math.sin(t)* scale
                    pX = x + a[3] + pX_change
                    pY = (y) + a[4] + pY_change
                    point(pX, pY, 3, 3, a[len(a)-1])
                if(a[0] == 5):
                    if sT <= 1:
                        t = sT
                        i = 0
                        while i < len(pxms):
                            X = 0
                            Y = 0
                            tm[3] = 1
                            k = 2
                            while k >= 0:
                                tm[k] = tm[k + 1] * t
                                k = k - 1

                            k = 0
                            while k < 4:
                                X = X + pxms[i][k] * tm[k]
                                Y = Y + pyms[i][k] * tm[k]
                                k = k + 1
                            pX = X * scale + pX_change
                            pY = Y * scale + pY_change
                            point(pX, pY, 3, 3, a[len(a)-1])
                            i= i+1

            sT = sT + 0.005

        for a in arrayForPoints:
            if (a[0] == 9):
                for u in a[1]:
                    pygame.draw.line(screen, a[2], u[0], u[1], u[2])

        pygame.event.get()

        slider.render(screen)
        slider.changeValue()
        slider_1.render(screen)
        slider_1.changeValue()
        slider_2.render(screen)
        slider_2.changeValue()

        current_color = (slider.getValue(), slider_1.getValue(), slider_2.getValue())

        pygame.draw.rect(screen,current_color, pygame.Rect(700, 90, 50, 50))

        pygame.display.update()

        old_pressed == pressed
        clock.tick(60)


game_loop()
print("Program ended")

pygame.quit()
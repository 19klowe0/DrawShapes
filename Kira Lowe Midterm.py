import pygame
from sys import exit
import math

width = 800
height = 700
pygame.init()

screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("Draw Some Shapes")
zoom = 1
screen1 = pygame.display.set_mode((int(width / zoom), int(height / zoom)), 0, 32)

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

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

def DrawBezier():
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

    m = [[-1, 3, -3, 1],
         [3, -6, 3, 0],
         [-3, 3, 0, 0],
         [1, 0, 0, 0]]

    pxm = [0, 0, 0, 0]
    pym = [0, 0, 0, 0]
    tm = [1, 1, 1, 1]

    i = 0
    pxm = [0, 0, 0, 0]
    pym = [0, 0, 0, 0]
    while i < 4:
        j = 0
        while j < 4:
            pxm[i] = pxm[i] + px[j] * m[j][i]
            pym[i] = pym[i] + py[j] * m[j][i]
            j = j + 1
        i = i + 1

    t_begin = 0
    t_end = 1
    while t_begin <= t_end:
        t = t_begin
        i = 0

        tm[3] = 1
        k = 2
        while k >= 0:
            tm[k] = tm[k + 1] * t
            k = k - 1

        k = 0
        X = 0
        Y = 0
        while k < 4:
            X = X + pxm[k] * tm[k]
            Y = Y + pym[k] * tm[k]
            k = k + 1
        pX = X
        pY = (Y)
        point(pX, pY, 3, 3, BLUE)

        t_begin = t_begin + 0.005
        pygame.display.update()
        clock.tick(60)



def drawRectangle():
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
    pygame.draw.line(screen, color, pt1, pt3, thick)
    pygame.draw.line(screen, color, pt3, pt2, thick)
    pygame.draw.line(screen, color, pt4, pt2, thick)
    pygame.draw.line(screen, color, pt1, pt4, thick)

def drawTriangle():
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
    pygame.draw.line(screen, color, pt1, pt2, thick)
    pygame.draw.line(screen, color, pt2, pt3, thick)
    pygame.draw.line(screen, color, pt1, pt3, thick)

def drawLine(color='GREEN', thick=3):
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
    pygame.draw.line(screen, color, pt1, pt2, thick)



def drawCircle():
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
    pygame.draw.circle(screen, color, pt1, r, thick)


def drawElipse():
    print("draw Elipse")
    color = BLACK
    thick = 3
    count1 = 0
    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, 150, 30))

    font = pygame.font.Font("freesansbold.ttf", 15)
    curveText = font.render("Draw a Elipse", True, BLACK)
    screen.blit(curveText, (5, 5))
    pygame.display.update()
    while count1 < 2:
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
                        pygame.draw.rect(screen, WHITE, (pt1[0] - margin, pt1[1] - margin, 2 * margin, 2 * margin), 5)
                        pygame.display.update()
                    count1 += 1
    left = pt1[0]
    top = pt1[1]
    width = abs(pt1[0] - pt2[0])
    height = abs(pt1[1] - pt2[1])
    pygame.draw.ellipse(screen, color, (left, top, width, height), thick)


#Button Class
class button():
    def __init__(self, color, x, y, width, height, text=''):
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
            font = pygame.font.SysFont('comicsans', 20)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, ( self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

def Capture(display,name,pos,size):
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
eclipseButton = button((255,165,165),650,10,120,70,"Eclipse")
lineButton = button((255,165,0),650,100,120,70,"Line")
bezierButton = button((0,255,0),650,200,120,70,"Bezier")
triangleButton = button((255,255,0),650,300,120,70,"Triangle")
circleButton = button((255,255,255),650,400,120,70,"Circle")
rectangleButton = button((255,0,255),650,500,120,70,"Rectangle")
captureButton = button((255,0,255),650,600,120,70,"Save")


buttonCheck = -1
while not done:
    eclipseButton.draw(screen, (0, 0, 0))
    lineButton.draw(screen, (0, 0, 0))
    bezierButton.draw(screen, (0, 0, 0))
    triangleButton.draw(screen, (0, 0, 0))
    circleButton.draw(screen, (0, 0, 0))
    rectangleButton.draw(screen, (0, 0, 0))
    captureButton.draw(screen, (0, 0, 0))

    time_passed = clock.tick(30)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = -1
            if lineButton.isOver(pos):
                buttonCheck = 1
                drawLine()
            elif bezierButton.isOver(pos):
                buttonCheck = 2
                DrawBezier()
            elif triangleButton.isOver(pos):
                buttonCheck = 3
                drawTriangle()
            elif circleButton.isOver(pos):
                buttonCheck = 4
                drawCircle()
            elif rectangleButton.isOver(pos):
                buttonCheck = 5
                drawRectangle()
            elif eclipseButton.isOver(pos):
                buttonCheck = 6
                drawElipse()
            elif captureButton.isOver(pos):
                buttonCheck = 7
                Capture(screen, "ArtWork.png", (0,0), (600, 700))

        elif event.type == pygame.MOUSEBUTTONUP:
            pressed = 1
        elif event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                zoom += 0.2
                print('ZOOMING IN')
            if event.key == pygame.K_DOWN:
                zoom -= 0.2
                print('ZOOMING OUT')
            if event.key == pygame.K_0:
                zoom = 2
                print('RESET')
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                zoom += 0
                print('ZOOMING IN')
            if event.key == pygame.K_DOWN:
                zoom -= 0
                print('ZOOMING OUT')
            if event.key == pygame.K_0:
                zoom = 2
                print('RESET')
        else:
            pressed = 0

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.update()
    old_pressed == pressed

pygame.quit()
#Name: Colin Wei
#Date: Jun 17th 2024
#Course: ICS3U1-01
#Description: Game

#importing
from pygame import*
import random

#canvas setup
init()
canvasX = 1000
canvasY = 700
SIZE = (canvasX,canvasY)
screen = display.set_mode(SIZE)

title = Rect(300,10,400,100)
#establishing buttons
buttonPlay = Rect(300,110,400,100)
buttonInstructions = Rect(300,220,400,100)
buttonQuit = Rect(300,590,400,100)

buttonNext = Rect(100,500,150,100)
buttonMenu = Rect(275,500,150,100)
buttonRetry = Rect(450,500,150,100)

buttonBack = Rect(0,0,100,50)
buttonLvl1 = Rect(100,100,100,100)
buttonLvl2 = Rect(210,100,100,100)
buttonLvl3 = Rect(100,210,100,100)
buttonLvl4 = Rect(210,210,100,100)
buttonLvl5 = Rect(100,320,100,100)
buttonLvl6 = Rect(210,320,100,100)
buttonLvl7 = Rect(160,430,100,100)

#some Ui stuff
itemBox = Rect(300,0,300,50)
hpBox = Rect(900,0,100,50)
pToPickUp = (650,0,100,50)

#general icons
keyIcon = image.load("general\\key.png")
doorIcon = image.load("general\\door.png")
codeIcon = image.load("general\\codeIcon.png")

#mouse
mx = 0
my = 0
button = 0
move = 0

#progression across levels
progression = 1

#colors
DBROWN = (101,67,33)
CONCRETE = (185,180,171)
METAL = (179,169,173)
GRASS =(86,125,70)
BLACK = (0,0,0)

#for describing stuff
descriptor = 0

fps = time.Clock()

def makeButton(screen,dimensions,mx,my, text): #makes a button
    if dimensions.collidepoint(mx,my):
            draw.rect(screen, (150,0,0), dimensions)
    else:
            draw.rect(screen, (255,0,0), dimensions)
    centre(fontRegular, dimensions, text)

def centre(font,rectangle,text): #centres text
    
    output = font.render(text, 1, (0,0,0))
    fontSize = font.size(text)
    
    startX = (rectangle[2]-fontSize[0])//2 + rectangle[0]
    
    startY = (rectangle[3]-fontSize[1])//2 + rectangle[1]
    
    centeredRect = (startX, startY, fontSize[0], fontSize[1])
    screen.blit(output, centeredRect)
    
def drawLevels(descriptor): #level menu
    lock = image.load("general\\locked.png")
    
    
    makeButton(screen,buttonBack, mx, my, "Back")
    #levels
    makeButton(screen,buttonLvl1, mx, my, "1")
    makeButton(screen,buttonLvl2, mx, my, "2")
    makeButton(screen,buttonLvl3, mx, my, "3")
    makeButton(screen,buttonLvl4, mx, my, "4")
    makeButton(screen,buttonLvl5, mx, my, "5")
    makeButton(screen,buttonLvl6, mx, my, "6")
    makeButton(screen,buttonLvl7, mx, my, "7")
    #makes levels available depending on progression
    if progression < 7:
        screen.blit(lock, buttonLvl7)
        if progression < 6:
            screen.blit(lock, buttonLvl6)
            if progression < 5:
                screen.blit(lock, buttonLvl5)
                if progression < 4:
                    screen.blit(lock, buttonLvl4)
                    if progression < 3:
                        screen.blit(lock, buttonLvl3)
                        if progression < 2:
                            screen.blit(lock,buttonLvl2)
    
    
    
    
    draw.rect(screen,(200,200,200), (500,0,500,700))
    
    if descriptor == 1: #1880s
        centre(fontSmall,(500,50,500,50),"We start in the 1880s.")
        centre(fontSmall,(500,100,500,50),"It's the start of the phenomenon of global warming.")
        centre(fontSmall,(500,150,500,50),"This is a period of technological progress.")
        centre(fontSmall,(500,200,500,50),"Small problem: the temperature is starting to rise.")
        centre(fontSmall,(500,250,500,50),"Your journey should be an easy one.")
        centre(fontSmall,(500,300,500,50),"Just avoid the wagons and the heat.")
    if descriptor == 2 and progression >= 2: #WW1
        centre(fontSmall,(500,50,500,50),"This is now the 1910s.")
        centre(fontSmall,(500,100,500,50),"You find yourself in a period of war.")
        centre(fontSmall,(500,150,500,50),"Specifically, a British Trench.")
        centre(fontSmall,(500,200,500,50),"Small problem: the object is in the German Trench.")
        centre(fontSmall,(500,250,500,50),"You will be shot at, and you will die to bullets.")
        centre(fontSmall,(500,300,500,50),"There should be some weapons you can use.")
        #centre(fontSmall,(500,350,500,50),"")
    if descriptor == 3 and progression >= 3: #Prohibition
        centre(fontSmall,(500,50,500,50),"It is the 1920s, a period of prosperity.")
        centre(fontSmall,(500,100,500,50),"It is also the time of illegal alcohol.")
        centre(fontSmall,(500,150,500,50),"Your object lies in an illegal drinking establishment.")
        centre(fontSmall,(500,200,500,50),"They're called speakeasys and require a password to enter.")
        centre(fontSmall,(500,250,500,50),"The owners of nearby buildings should provide parts of it.")
        centre(fontSmall,(500,300,500,50),"Bring them to the speakeasy door for access.")        
        centre(fontSmall,(500,350,500,50),"Just beware of the gangsters, who shoot indiscriminately.")
        centre(fontSmall,(500,400,500,50),"They come down the road every now and then in cars.")
        centre(fontSmall,(500,450,500,50),"These car things are also interesting.")
        centre(fontSmall,(500,500,500,50),"Hopefully they don't cause an increase in temperature.")        
    if descriptor == 4 and progression >= 4: #WW2
        centre(fontSmall,(500,50,500,50),"This is now the 1940s.")
        centre(fontSmall,(500,100,500,50),"The world is at war again.")
        centre(fontSmall,(500,150,500,50),"Now you find yourself in the middle of a beach landing.")
        centre(fontSmall,(500,200,500,50),"The object is also with the Germans this time.")
        centre(fontSmall,(500,250,500,50),"This time, they are armed to the teeth.")
        centre(fontSmall,(500,300,500,50),"You will still be shot at, and you will die to bullets.")
        centre(fontSmall,(500,350,500,50),"Sadly, there are no weapons that you personally control.")
        centre(fontSmall,(500,400,500,50),"However, you do have access to a radio.")        
        centre(fontSmall,(500,450,500,50),"Find the frequencies, then radio in to destroy them.")
    if descriptor == 5 and progression >= 5: #Space race
        centre(fontSmall,(500,50,500,50),"The 1960s are here, and a race is ongoing.")
        centre(fontSmall,(500,100,500,50),"The goal? Be the first to reach the moon!")
        centre(fontSmall,(500,150,500,50),"A lot of infrastructure has be constructed for this.")
        centre(fontSmall,(500,200,500,50),"Unfortunately, one of these launch pads is above the object.")
        centre(fontSmall,(500,250,500,50),"Worse, there's a launch scheduled for today.")
        centre(fontSmall,(500,300,500,50),"You should probably help with the launch process.")
        centre(fontSmall,(500,350,500,50),"There is a right way to do this, so follow the instructions.")
        centre(fontSmall,(500,400,500,50),"Or the launch will be cancelled.")
        centre(fontSmall,(500,450,500,50),"The instructions are on a bulletin board in the supply room.")        
        centre(fontSmall,(500,500,500,50),"After the rocket takes off, you can collect the object.")
        centre(fontSmall,(500,550,500,50),"Oh, and now the heat is now actually starting to hurt.")
    if descriptor == 6 and progression >= 6: #Berlin Wall
        centre(fontSmall,(500,50,500,50),"The 1980s is in its last years.")
        centre(fontSmall,(500,100,500,50),"A major power is collapsing at this very moment.")
        centre(fontSmall,(500,150,500,50),"Its sphere of influence is declining, where you find yourself.")
        centre(fontSmall,(500,200,500,50),"A country split into two is now reuniting.")
        centre(fontSmall,(500,250,500,50),"Among the celebrations, your object lays.")
        centre(fontSmall,(500,300,500,50),"You have to negotiate your way through the crowds.")
        centre(fontSmall,(500,350,500,50),"However, your largest obstacle is the wall.")
        centre(fontSmall,(500,400,500,50),"Find your own way across it, and collect the object.")        
    if descriptor == 7 and progression == 7: #Modern day
        centre(fontSmall,(500,50,500,50),"A new millenium has dawned. The 2000s.")
        centre(fontSmall,(500,100,500,50),"While the world gets adjusted, you have to do the same.")
        centre(fontSmall,(500,150,500,50),"Even brief exposure to heat can now be fatal.")
        centre(fontSmall,(500,200,500,50),"This time, obtaining the object is more crucial than ever.")
        centre(fontSmall,(500,250,500,50),"It is also more difficult than ever.")
        centre(fontSmall,(500,300,500,50),"It is in a vault, with instructions nearby.")
        centre(fontSmall,(500,350,500,50),"All the required information can be found there.")
        centre(fontSmall,(500,400,500,50),"You've been through a lot and have come out on top.")
        centre(fontSmall,(500,450,500,50),"Recall what you have learned, and channel that knowledge.")

def drawMenu(): #main menu
    centre(fontRegular,title,"Global Warming: Eras")
    makeButton(screen,buttonPlay,mx,my,"Play")
    makeButton(screen,buttonInstructions, mx, my, "Instructions")
    makeButton(screen,buttonQuit, mx, my, "Quit")

def drawInstructions(): #instruction page
    #title
    centre(fontRegular,(0,0,1000,50),"Instructions")
    #images
    char = image.load("instructions\\instructCharacter.png")
    #images
    key = image.load("instructions\\instructKey.png")
    wall = image.load("instructions\\instructWall.png")
    door = image.load("instructions\\instructDoor.png")
    interact = image.load("instructions\\instructInteract.png")
    interactable = image.load("instructions\\instructInteractable.png")
    heat = image.load("instructions\\instructHeat.png")
    shade = image.load("instructions\\instructShade.png")
    finalObject = image.load("instructions\\instructObject.png")
    bulletinboard = image.load("instructions\\bulletin.png")
    button = image.load("instructions\\instructButton.png")
    #display character
    centre(fontRegular,(350,80,100,50),"your character:")
    screen.blit(char,(500,80))
    #display images
    screen.blit(key,(500,340,50,50))
    screen.blit(door,(500,400,50,50))
    screen.blit(heat,(480,460,50,50))
    screen.blit(shade,(480,570,50,50))
    screen.blit(finalObject,(500,640,50,50))
    
    screen.blit(interact,(930,340,50,50))
    screen.blit(interactable,(930,395))
    screen.blit(wall,(930,460,50,50))
    screen.blit(bulletinboard,(930,530,50,50))
    screen.blit(button,(930,610,50,50))
    
    makeButton(screen,buttonBack, mx, my, "Back")
    #lore
    centre(fontSmall,(100,40,800,50),"You control an organism that has lived a long time.")
    centre(fontSmall,(100,125,800,50),"Unfortunately, ever since 1880, this pesky thing called \"global warming\" is occuring.")
    centre(fontSmall,(100,150,800,50),"You aren't surviving this rise in temperature, unless...")
    centre(fontSmall,(100,175,800,50),"Some mysterious object, if you obtain it, shall allow you to withstand the rise.")
    #controls
    centre(fontSmall,(100,200,800,50),"You shall face challenges. Here are the controls:")
    centre(fontSmall,(50,225,400,50),"Move up: W")
    centre(fontSmall,(50,250,400,50),"Move down: S")
    centre(fontSmall,(550,225,400,50),"Move left: A")
    centre(fontSmall,(550,250,400,50),"Move right: D")
    centre(fontSmall,(50,275,400,50),"Pick up/put down items: P")
    centre(fontSmall,(550,275,400,50),"Press a button: I")
    
    #items
    centre(fontRegular,(50,300,900,50),"Items You Will Encounter")
    centre(fontSmall,(50,340,400,50),"Keys: They will help you unlock doors.")
    centre(fontSmall,(50,390,400,50),"Doors: Obstacles to pass.")
    centre(fontSmall,(50,415,400,50),"Not all have a corresponding key.")
    centre(fontSmall,(50,455,400,50),"Heat tiles: They are red, and will decrease your health.")
    centre(fontSmall,(50,480,400,50),"The further you progress, the more deadly they are.")
    centre(fontSmall,(50,505,400,50),"Effect can be mitigated by shade tiles.")
    centre(fontSmall,(50,550,400,50),"Shade tiles (left): Block heat tiles (see right for effect).")
    centre(fontSmall,(50,575,400,50),"Note that they will be placed down on the")
    centre(fontSmall,(50,600,400,50),"first heat tile you go on with it.")
    centre(fontSmall,(50,640,400,50),"Green tile: The object. Reach it to complete the level.")
    #column 2
    centre(fontSmall,(550,325,400,50),"Interactables: Function similar to keys.")
    centre(fontSmall,(550,350,400,50),"Made distinct by rounded corners.")
    centre(fontSmall,(550,375,400,50),"Specifics depend on level.")
    centre(fontSmall,(550,400,400,50),"Bring them to the larger tiles.")    
    centre(fontSmall,(550,450,400,50),"Walls: You cannot pass them.")
    centre(fontSmall,(550,475,400,50),"Don't even bother trying.")
    centre(fontSmall,(550,525,400,50),"Bulletin board: provides instructions.")
    centre(fontSmall,(550,580,400,50),"Buttons: Pushing them does stuff.")
    centre(fontSmall,(550,600,400,50),"Specifics vary per button.")
    centre(fontSmall,(550,620,400,50),"They are circular.")


def levels(charX,charY, item): #setup for levels
    makeButton(screen,buttonBack, mx, my, "Back")

    #walls
    for i in range(0,len(wallPos), 2):
        draw.rect(screen, (0,0,0), ((wallPos[i] - 1)*40+25,(wallPos[i+1] - 1)*40 + 55, 40,40))
    
    #heat tiles
    for i in range(0,len(heatTiles),4):
        if heatTiles[i+3] == True:
            color = (255-heatTiles[i+2]*10,0,0)
        else:
            color = (50,50,50)
        draw.rect(screen, color, ((heatTiles[i] - 1)*40+25,(heatTiles[i+1] - 1)*40 + 55, 40,40))
        if heatTiles[i+3] == False:
            draw.rect(screen, (255,255,255), ((heatTiles[i] - 1)*40+26,(heatTiles[i+1] - 1)*40 + 56, 39,39),2)
    #shade
    for i in range(0,len(shadeTiles),3):
        if shadeTiles[i+2] == True:
            draw.rect(screen,(50,50,50), ((shadeTiles[i] - 1)*40+30,(shadeTiles[i+1] - 1)*40 + 60, 30,30))
        if charX == shadeTiles[i] and charY == shadeTiles[i+1] and item == "none" and shadeTiles[i+2] == True:
            centre(fontRegular,pToPickUp,"Pick up")
    
    #interactable items        
    for i in range(0,len(interactItem),6):        
        if interacTile[i+3] == True:
            draw.rect(screen, interacTile[i+4], ((interacTile[i] - 1)*40+25,(interacTile[i+1] - 1)*40 + 55, 40,40),0,10)
            screen.blit(interacTile[i+5],((interacTile[i] - 1)*40 + 35,(interacTile[i+1] - 1)*40 + 65, 30,30))
        if interactItem[i+3] == True:
            draw.rect(screen, interactItem[i+4], ((interactItem[i] - 1)*40 + 30,(interactItem[i+1] - 1)*40 + 60, 30,30),0,10)
            screen.blit(interactItem[i+5],((interactItem[i] - 1)*40 + 35,(interactItem[i+1] - 1)*40 + 65, 30,30))
        if charX == interactItem[i] and charY == interactItem[i+1] and item == "none" and interactItem[i+3] == True:
            centre(fontRegular,pToPickUp,"Pick up")
        
    #lock and key mechanic
    for i in range(0,len(doorPos), 5):#door
        if doorPos[i+3] == True:
            draw.rect(screen, doorPos[i+4],((doorPos[i] - 1)*40+25,(doorPos[i+1] - 1)*40 + 55, 40,40))
            screen.blit(doorIcon,((doorPos[i] - 1)*40+35,(doorPos[i+1] - 1)*40 + 60, 40,40))

    for i in range(0,len(keyPos),5):#key
        if keyPos[i+3] == True:
            draw.rect(screen, keyPos[i+4], ((keyPos[i] - 1)*40+30,(keyPos[i+1] - 1)*40 + 60, 30,30))
            screen.blit(keyIcon,((keyPos[i] - 1)*40+40,(keyPos[i+1] - 1)*40 + 65, 30,30))
            if charX == keyPos[i] and charY == keyPos[i+1] and item == "none":
                centre(fontRegular,pToPickUp,"Pick up")
    
    #buttons
    for i in range(0,len(buttonTile),6):
        if buttonTile[i+3] == True:
            draw.ellipse(screen, buttonTile[i+4], ((buttonTile[i] - 1)*40+30,(buttonTile[i+1] - 1)*40 + 60, 30,30))
            centre(fontSmall,((buttonTile[i] - 1)*40+30,(buttonTile[i+1] - 1)*40 + 60, 30,30),buttonTile[i+5])
            if charX == buttonTile[i] and charY == buttonTile[i+1] and item == "none":
                centre(fontRegular,pToPickUp,buttonTile[i+2])
    #grid
    for i in range(25,996,40):
        draw.line(screen,(0,0,0), (i,55),(i,695))
    for i in range(55,696,40):
        draw.line(screen,(0,0,0), (25,i),(985,i))

def collision(rectPlayer, rectObstacle): #colliding with an obstacle that could kill
    for i in (rectObstacle):
        if rectPlayer.colliderect(i):
            return True
    return False

def lvl1(horseX, horseX2): #level 1 related quirks
#    if horseX == 
    draw.rect(screen, (179,179,179), (25,255,960,160))
    if horseX <= -160:
        horseX = random.randint(985,1500)
    horseRect = Rect(horseX,265, 160,60)
    screen.blit(horsePic2, horseRect)
    horseX -= 5
    
    if horseX2 >= 985:
        horseX2 = random.randint(-1000,-140)
    horseRect2 = Rect(horseX2, 345, 160,60)
    screen.blit(horsePic1, horseRect2)

    horseX2 += 5
    
    horsePos = []
    horsePos.append(horseRect)
    horsePos.append(horseRect2)
    
    return horsePos, horseX, horseX2

def lvl2(count): #level 2 related stuff
    counting = True
    draw.rect(screen, DBROWN, (25,55,240,280))
    draw.rect(screen, DBROWN, (265,135,80,200))
    draw.rect(screen, DBROWN, (185,335,80,80))
    draw.rect(screen, DBROWN, (25,415,320,280))
    
    draw.rect(screen, DBROWN, (745,375, 240,360))
    draw.rect(screen, DBROWN, (905,135, 80,240))
    draw.rect(screen, DBROWN, (825,55, 80,160))
    boolet = []
    if shooting1 == False and shooting2 == False and count > 0:
        counting = False
    if shooting1 == True:
        draw.circle(screen, (150,150,150), (845,195),15)
        draw.circle(screen, (150,150,150), (925,235),15)
        draw.circle(screen, (150,150,150), (925,275),15)
        if count % 3 == 0:
            draw.rect(screen, (255,255,0), boolet2Rect)
            boolet.append(boolet2Rect)
        if count % 50 == 0:
            draw.rect(screen, (255,255,0), boolet1Rect)
            boolet.append(boolet1Rect)
        if count % 50 == 20:
            draw.rect(screen, (255,255,0), boolet3Rect)
            boolet.append(boolet3Rect)
    else:
        if count <= 0 and count >= -50:
            draw.rect(screen, (255,0,0), (850,210, 40,40))
            
    if shooting2 == True:
        if count % 50 == 10:
            draw.rect(screen, (255,255,0), boolet4Rect)
            boolet.append(boolet4Rect)
        if count % 50 == 40:
            draw.rect(screen, (255,255,0), boolet5Rect)
            boolet.append(boolet5Rect)

        draw.circle(screen, (150,150,150), (765,435),15)
        draw.circle(screen, (150,150,150), (765,475),15)
    else:
        if count <= -100:
            draw.rect(screen, (255,0,0), (780,430, 40,40))
        if count == -100:
            count = 0
    
    if counting == True:
        count += 1
    return count, boolet

def lvl3(count, carY, gangster, carY2, gangster2, code): #level3 related stuff
    collideBox = []
    if carY >= 700: #first car
        gangster = False
        carY = random.randint(-1500, -700)
        isGangster = random.randint(1,5)
        if isGangster == 2:
            gangster = True
            shooting1 = True
    carRect = Rect(435,carY,60,160)
    if gangster == False:
        screen.blit(car1,carRect)
    else:
        screen.blit(car1g,carRect)
        if count % 10 == 0:
            booletRect = Rect(495,carY+30,80,3)
            draw.rect(screen,(255,255,0),(booletRect))
            collideBox.append(booletRect)
    collideBox.append(carRect)
    carY += 5
    
    if carY2 <= -200: #second car
        gangster2 = False
        carY2 = random.randint(1200, 2000)
        isGangster2 = random.randint(1,5)
        if isGangster2 == 2:
            gangster2 = True
            shooting2 = True
    carRect2 = Rect(515,carY2,60,120)
    if gangster2 == False:
        screen.blit(car2,carRect2)
    else:
        screen.blit(car2g,carRect2)
        if count % 10 == 5:
            if carY2+90 > carRect[1] and carY2+90 < carRect[1]+carRect[3]:
                booletRect2 = Rect(495,carY2+90, 20,3)
            else:
                booletRect2 = Rect(435,carY2+90,80,3)
            draw.rect(screen,(255,255,0),(booletRect2))
            collideBox.append(booletRect2)
    collideBox.append(carRect2)
    carY2 -= 5
    
    if code == 3: #gaining speakeasy access
        for i in range(0,len(keyPos),5):
            if keyPos[i+2] == "speakeasy key":
                keyPos[i+3] = True
                break
        code = 4
    
    count += 1
    return count, carY, gangster, carY2, gangster2, collideBox, code

def lvl4(count): #level 4 related stuff
    boolet = []
    if shooting1 == True: #top bunker
        if count % 3 == 0:
            draw.rect(screen, (255,255,0), booletOneRect)
            boolet.append(booletOneRect)
        if count % 4 == 1:
            draw.rect(screen, (255,255,0), booletTwoRect)
            boolet.append(booletTwoRect)
        if count % 3 == 2:
            draw.rect(screen, (255,255,0), booletThreeRect)
            boolet.append(booletThreeRect)
    else:
        if count > -50 and count < 0:
            draw.rect(screen,(255,0,0),(760,120,60,60))

    if shooting2 == True: #middle bunker
        if count % 3 == 0:
            draw.rect(screen, (255,255,0), booletFourRect)
            boolet.append(booletFourRect)
        if count % 4 == 1:
            draw.rect(screen, (255,255,0), booletFiveRect)
            boolet.append(booletFiveRect)
        if count % 3 == 2:
            draw.rect(screen, (255,255,0), booletSixRect)
            boolet.append(booletSixRect)
    else:
        if count > -150 and count <= -100:
            draw.rect(screen,(255,0,0),(760,320,60,60))
            if count == -100:
                count = 0


    if shooting3 == True: #lower bunker
        if count % 3 == 0:
            draw.rect(screen, (255,255,0), booletSevenRect)
            boolet.append(booletSevenRect)
        if count % 4 == 1:
            draw.rect(screen, (255,255,0), booletEightRect)
            boolet.append(booletEightRect)
        if count % 3 == 2:
            draw.rect(screen, (255,255,0), booletNineRect)
            boolet.append(booletNineRect)
    else:
        if count > -250 and count <= -200:
            draw.rect(screen,(255,0,0),(760,560,60,60))
            if count == -200:
                count = 0

    count += 1
    return count, boolet

def lvl5(bulletin): #level 5 related stuff
    screen.blit(bulletin,(106,416))

def lvl6(count, peopleY, repair, wrecker, ball, wreckBallRect): #level 6 related stuff
    collidePeople = []
    if peopleY <= -100: #Crowd
        peopleY = random.randint(750, 1050)
    peopleRect = Rect(306,peopleY,79,79)
    screen.blit(people2,peopleRect)
    #screen.blit(car1g,carRect)
    collidePeople.append(peopleRect)
    peopleY -= 5
    
    if repair == 3: #activating wrecking ball
        for i in range(0,len(buttonTile),6):
            if buttonTile[i+2] == "activate":
                buttonTile[i+3] = True
                break
        repair = 4

    if tnt == 3: #blowing up a hole
        for i in range(0,len(doorPos),5):
            if doorPos[i+2] == "Blownup":
                doorPos[i+3] = False
                break
    if count == -1: #wrecking ball "animation"
        wrecker = transform.rotate(wrecker,90)
        ball = transform.rotate(ball,90)
        wreckBallRect = (626,96,119,79)

    count += 1
    return count, peopleY, collidePeople, wrecker, ball, wreckBallRect

def lvl7(cards, codes, carPos, carPos2, moveState, combo1, combo2): #level 7 related stuff
    if cards == 3: #unlocking button r
        for i in range(0,len(doorPos),5):
            if doorPos[i+2] == "keycards":
                doorPos[i+3] = False
                break
    if codes == 3: #unlocking button b
        for i in range(0,len(keyPos),5):
            if keyPos[i+2] == "keycard":
                keyPos[i+3] = True
                codes = 4
                break

    if carPos <= -160 and carPos2 > 985: #deciding whether the car moves vertically or horizontally 
        moveState = random.randint(1,2)
        carPos = random.randint(985,1500)
        carPos2 = random.randint(-1000,-140)

    if moveState == 1: #Horizontal
        carRect = Rect(carPos,305, 160,60)
        carRect2 = Rect(carPos2, 385, 160,60)
        screen.blit(car2, carRect)
        screen.blit(car4, carRect2)    
    else: #Vertical
        carRect = Rect(435,carPos, 60,160)
        carRect2 = Rect(515,carPos2, 60,160)
        screen.blit(car, carRect)
        screen.blit(car3, carRect2)

    carPos -= 5
    carPos2 += 5
    
    cars = []
    cars.append(carRect)
    cars.append(carRect2)

    #Unlock button g
    draw.rect(screen,(255,255,255),(26,456,119,39))
    if combo1 == "":
        centre(fontSmall,(26,456,119,39),"code")
    else:
        centre(fontSmall,(26,456,119,39),combo1)

    #Unlock vault
    draw.rect(screen,(255,255,255),(266,256,119,39))
    if combo2 == "":
        centre(fontSmall,(266,256,119,39),"code")
    else:
        centre(fontSmall,(266,256,119,39),combo2)

    return codes, carPos, carPos2, cars, moveState

def character(charX,charY, move, state): #your character
    #position
    posX = (charX-1)*40 + 25
    posY = (charY-1)*40 + 55
    
    characterPHUp = Rect(posX + 5 , posY + 5 , 30 , 20)
    characterPHDown = Rect(posX + 5,posY + 15 , 30 , 20)
    characterPHRight = Rect(posX + 15,posY + 5, 20 , 30)
    characterPHLeft = Rect(posX + 5,posY + 5, 20 , 30)
    
    characterRect = characterPHDown

    if move == 1:
        characterRect = characterPHUp
    elif move == 2:
        characterRect = characterPHDown
    elif move == 3:
        characterRect = characterPHLeft
    elif move == 4:
        characterRect = characterPHRight
    draw.rect(screen,(0,0,255), characterRect)
    
    draw.rect(screen, (255,200,200), itemBox)
    centre(fontRegular,itemBox,item)
    
    draw.rect(screen, (255,255,255), hpBox)
    
    if state == stateLvl5 or state == stateLvl6:
        hpBar = (900,0,hp*2,50)
    elif state == stateLvl7:
        hpBar = (900,0,hp*4,50)
    else:
        hpBar = (900,0,hp,50)
        
    draw.rect(screen,(255,0,0), hpBar)
    centre(fontSmall,(900,0,100,50),"Health")
    
    return characterRect

#!!!!!
def willCollide(x, y): #collide with walls, closed doors, or interactable tiles
    collide = False
    global item
    for i in range(0,len(wallPos),2): #walls
        if x == wallPos[i] and y == wallPos[i+1]:
            collide = True
            return collide
        
    for i in range(0,len(doorPos),5): #doors
        if x == doorPos[i] and y == doorPos[i+1]:
            if doorPos[i+3] == True:
                if item == doorPos[i+2]:
                    doorPos[i+3] = False
                    item = "none"
                    break
                else:
                    collide = True
                    return collide
                
    for i in range(0, len(interacTile),6): #interactables
        if x == interacTile[i] and y == interacTile[i+1]:
            if interacTile[i+3] == True and item == interacTile[i+2]:
                global state
                global count
                global shooting1
                global shooting2
                global shooting3
                if state == stateLvl2: #shooting at soldiers
                    if item == "Tank Shell":
                        shooting1 = False
                        item = "none"
                        count = -50
                        break
                    
                    if item == "Artillery Shell":
                        global shooting2
                        shooting2 = False
                        item = "none"
                        count = -150
                        break
                    
                if state == stateLvl3: #speakeasy code
                    global code
                    if item.count("code") > 0:
                        code += 1
                        item = "none"
                        
                if state == stateLvl4: #frequency dial in
                    if item == "frequency1":
                        shooting1 = False
                        item = "none"
                        count = -50
                    if item == "frequency2":
                        shooting2 = False
                        item = "none"
                        count = -150
                    if item == "frequency3":
                        shooting3 = False
                        item = "none"
                        count = -250
                        
                if state == stateLvl5: #rocket launching
                    global hp
                    global steps
                    global message
                    global success
                    if item == "Toolbox": #toolbox
                        steps += 1
                        item = "none"
                    elif item == "Fuel1" or item == "Fuel2" or item == "Fuel3" or item == "Fuel4": #fueling
                        if steps == 1 or steps == 2 or steps == 4 or steps == 5:
                            steps += 1
                            item = "none"
                        else:
                            stateGame = False
                            state = stateGameOver
                            success = False
                            message = "Launch delayed"
                    elif item == "frequency": #mission control
                        if steps == 3:
                            steps += 1
                            item = "none"
                        else:
                            stateGame = False
                            state = stateGameOver
                            success = False
                            message = "Launch delayed"
                    elif item == "Toolbox2": #toolbox
                        if steps == 7:
                            steps += 1
                            item = "none"
                        else: 
                            stateGame = False
                            state = stateGameOver
                            success = False
                            message = "Launch delayed"
                    elif item == "Siren key": #clearing the launch area
                        if steps == 8:
                            steps += 1
                            item = "none"
                        else: 
                            stateGame = False
                            state = stateGameOver
                            success = False
                            message = "Launch delayed"
                        for i in range(0,len(doorPos),5):
                            if doorPos[i+2] == "clear":
                                doorPos[i+3] = False
                            
                if state == stateLvl6: #getting past barriers
                    global repair
                    global tnt
                    if item.count("parts") > 0:
                        repair += 1
                        item = "none"
                    elif item.count("TNT") > 0:
                        tnt += 1
                        item = "none"
                
                if state == stateLvl7: #codes
                    global codes
                    global cards
                    if item.count("code") > 0:
                        codes += 1
                        item = "none"
                    elif item.count("card") > 0:
                        cards += 1
                        item = "none"

    return collide

def endGoal(x,y): #objective
    draw.rect(screen, (0,200,0), ((x - 1)*40+26,(y - 1)*40 + 56, 39,39))
    if charX == x and charY == y:
        clear = True
        return clear

def heatTileTouch(charX,charY,hp): #touching a heat tile
    global item
    for i in range(0,len(heatTiles),4):
        if charX == heatTiles[i] and charY == heatTiles[i+1] and heatTiles[i+3] == True:
            #if heatTiles[i+3] == True:
            if item == "shade":
                heatTiles[i+3] = False
                item = "none"
            else:
                hp -= heatTiles[i+2]
                if hp < 0:
                    hp = 0
            break
    
    return hp

def gameOver(success,message): #level end
    if success == True:
        centre(fontRegular,(0,0,1000,100),"SUCCESS")
        centre(fontSmall,(0,200,1000,50),message)
    else:
        centre(fontRegular,(0,0,1000,100),"FALIURE")
        centre(fontSmall,(0,200,1000,50),message)
    makeButton(screen,buttonMenu,mx,my,"Menu")
            
#fonts
fontRegular = font.SysFont("Times New Roman", 30)
fontSmall = font.SysFont("Times New Roman",20)

#states
state = 0
stateMenu = 0
stateLevels = 1
stateInstructions = 2
stateGameOver = 3
#game states
stateGame = False
stateLvl1 = 10
stateLvl2 = 11
stateLvl3 = 12
stateLvl4 = 13
stateLvl5 = 14
stateLvl6 = 15
stateLvl7 = 16

#setup
item = "none"
hp = 100

running = True
while running:
    for e in event.get():             # checks all events that happen
        if e.type == QUIT: #quit?
            running = False

        if e.type == MOUSEBUTTONDOWN: #clicking buttons
            mx, my = e.pos
            button = e.button
            if button == 1:
                if buttonPlay.collidepoint(mx,my) and state == stateMenu: #heading to menu
                    state = stateLevels
                if state == stateLevels: #heading to a level
                    if buttonLvl1.collidepoint(mx,my):
                        state = stateLvl1
                        setup = True
                        stateGame = True
                    if buttonLvl2.collidepoint(mx,my) and progression >= 2:
                        state = stateLvl2
                        setup = True
                        stateGame = True
                    if buttonLvl3.collidepoint(mx,my) and progression >= 3:
                        state = stateLvl3
                        setup = True
                        stateGame = True
                    if buttonLvl4.collidepoint(mx,my) and progression >= 4:
                        state = stateLvl4
                        setup = True
                        stateGame = True
                    if buttonLvl5.collidepoint(mx,my) and progression >= 5:
                        state = stateLvl5
                        setup = True
                        stateGame = True
                    if buttonLvl6.collidepoint(mx,my) and progression >= 6:
                        state = stateLvl6
                        setup = True
                        stateGame = True
                    if buttonLvl7.collidepoint(mx,my) and progression == 7:
                        state = stateLvl7
                        setup = True
                        stateGame = True

                if buttonBack.collidepoint(mx,my):#heading back
                    if stateGame == True:
                        state = stateLevels
                        stateGame = False
                    else:
                        state = stateMenu
                        
                if buttonInstructions.collidepoint(mx,my) and state == stateMenu: #instructions
                    state = stateInstructions
                if buttonQuit.collidepoint(mx,my) and state == stateMenu: #quitting game
                    running = False
                if buttonMenu.collidepoint(mx,my) and state == stateGameOver: #game ended
                    state = stateLevels
                    
        if e.type == MOUSEMOTION:
            mx, my = e.pos
            if state == stateLevels: #giving level descriptions
                if buttonLvl1.collidepoint(mx,my):
                    descriptor = 1
                if buttonLvl2.collidepoint(mx,my):
                    descriptor = 2
                if buttonLvl3.collidepoint(mx,my):
                    descriptor = 3
                if buttonLvl4.collidepoint(mx,my):
                    descriptor = 4
                if buttonLvl5.collidepoint(mx,my):
                    descriptor = 5
                if buttonLvl6.collidepoint(mx,my):
                    descriptor = 6
                if buttonLvl7.collidepoint(mx,my):
                    descriptor = 7
                    
        if e.type == KEYDOWN: #interacting with the keyboard
            if stateGame == True:
                #movement
                if e.key == K_w and charY > 1:
                    move = 1
                    if willCollide(charX, charY-1) == False:
                        charY -= 1
                if e.key == K_s and charY < 16:
                    move = 2
                    if willCollide(charX, charY+1) == False:
                        charY += 1
                if e.key == K_a and charX > 1:
                    move = 3
                    if willCollide(charX - 1, charY) == False:
                        charX -= 1
                if e.key == K_d and charX < 24:
                    move = 4
                    if willCollide(charX + 1, charY) == False:
                        charX += 1
                hp = heatTileTouch(charX,charY,hp)
                
                if e.key == K_p: #picking up stuff and button interaction
                    tobreak = False
                    for i in range(0,len(keyPos),5): #picking up a key
                        if charX == keyPos[i] and charY == keyPos[i+1] and item == "none":
                            item = keyPos[i + 2]
                            keyPos [i+3] = False
                            break
                        elif item == keyPos[i+2]:
                            keyPos[i] = charX
                            keyPos[i+1] = charY
                            item = "none"
                            keyPos[i+3] = True
                            tobreak = True
                            break
                        if tobreak == True:
                            break
                    
                    for i in range(0,len(interactItem),6): #picking up interactables
                        if charX == interactItem[i] and charY == interactItem[i+1] and item == "none" and interactItem[i+3] == True:
                            item = interactItem[i+2]
                            interactItem[i+3] = False
                            break
                        elif item == interactItem[i+2]:
                            interactItem[i] = charX
                            interactItem[i+1] = charY
                            interactItem[i+3] = True
                            item = "none"
                            break
                        
                    for i in range(0,len(shadeTiles),3): #picking up shade tiles
                        if charX == shadeTiles[i] and charY == shadeTiles[i+1] and item == "none" and shadeTiles[i+2] == True:
                            item = "shade"
                            shadeTiles[i+2] = False
                            break
                        if item.count('shade') > 0:
                            for i in range(0,len(shadeTiles),3):
                                if shadeTiles[i+2] == False:
                                    shadeTiles[i] = charX
                                    shadeTiles[i+1] = charY
                                    shadeTiles[i+2] = True
                                    item = "none"
                                    tobreak = True
                                    break
                            if tobreak == True:
                                break
                        if tobreak == True:
                            break

                if e.key == K_i: #button interaction
                    for i in range(0,len(buttonTile),6):
                        if charX == buttonTile[i] and charY == buttonTile[i+1] and item == "none" and buttonTile[i+3] == True:
                            if state != stateLvl7:
                                buttonTile[i+3] = False
                            if state == stateLvl5: #Launching the rocket
                                global steps
                                if buttonTile[i+2] == "Check systems":
                                    if steps == 6:
                                        steps += 1
                                    else:
                                        stateGame = False
                                        state = stateGameOver
                                        success = False
                                        message = "Launch delayed"
                                    break
                                elif buttonTile[i+2] == "Send all clear":
                                    if steps == 9:
                                        steps += 1
                                        for i in range(0,len(doorPos),5):
                                            if doorPos[i+2] == "launch":
                                                doorPos[i+3] = False
                                    else:
                                        stateGame = False
                                        state = stateGameOver
                                        success = False
                                        message = "Launch delayed"
                                    break
                            
                            #level 6
                            if state == stateLvl6: #wrecking ball
                                if buttonTile[i+2] == "activate":
                                    global wrecker
                                    global ball
                                    global wreckBallRect
                                    global count
                                    for i in range(0,len(doorPos),5):
                                        if doorPos[i+2] == "wreckingball":
                                            doorPos[i+3] = False
                                        
                                    wrecker = transform.rotate(wrecker,270)
                                    ball = transform.rotate(ball,270)
                                    wreckBallRect = (506,175,79,79)
                                    count = -100
                                        
                            #level 7
                            if state == stateLvl7: #combinations
                                global combination1
                                global combination2
                                global combo1
                                global combo2
                                if buttonTile[i+2] == "1":
                                    if combination1 == 3 or combination1 == 4:
                                        combination1 += 1
                                        combo1 += "1"
                                    else:
                                        combination1 = 0
                                        combo1 = ""
                                elif buttonTile[i+2] == "2":
                                    if combination1 == 0 or combination1 == 2:
                                        combination1 += 1
                                        combo1 += "2"
                                    else:
                                        combination1 = 0
                                        combo1 = ""
                                elif buttonTile[i+2] == "3":
                                    if combination1 == 1 or combination1 == 5:
                                        combination1 += 1
                                        combo1 += "3"
                                    else:
                                        combination1 = 0
                                        combo1 = ""
                                    if combination1 == 6:
                                        for i in range(0,len(doorPos),5):
                                            if doorPos[i+2] == "passcode":
                                                doorPos[i+3] = False
                                        combo1 = "unlocked"

                                elif buttonTile[i+2] == "r":
                                    if combination2 == 0 or combination2 == 1:
                                        combination2 += 1
                                        combo2 += "r"
                                    else:
                                        combination1 = 0
                                        combo2 = ""
                                elif buttonTile[i+2] == "g":
                                    if combination2 == 2 or combination2 == 5:
                                        combination2 += 1
                                        combo2 += "g"
                                    else:
                                        combination2 = 0
                                        combo2 = ""
                                    if combination2 == 6:
                                        for i in range(0,len(doorPos),5):
                                            if doorPos[i+2] == "password":
                                                doorPos[i+3] = False
                                elif buttonTile[i+2] == "b":
                                    if combination2 == 3 or combination2 == 4:
                                        combination2 += 1
                                        combo2 += "b"
                                    else:
                                        combination2 = 0
                                        combo2 = ""
            
    screen.fill((255,255,255))
            
    if state == stateMenu: #main menu
        drawMenu()
    if state == stateLevels: #level menu
        drawLevels(descriptor)
    if state == stateInstructions: #instructions page
        drawInstructions()
    if state == stateGameOver: #level's end
        gameOver(success,message)
        
    if state == stateLvl1: #level 1
        if setup == True: #setting up
            #images
            horsePic1 = image.load("level1//horse1.png")
            horsePic2 = image.load("level1//horse2.png")
            railPic = image.load("level1//rails.png")
            trainPic = image.load("level1//railswithtrain.png")

            hp = 100
            
            #starting place
            charX = 1
            charY = 1
            
            #walls: x,y
            wallPos = [5,1, 5,2, 5,4, 5,5, 6,5, 7,5, 8,5, 9,5, 10,5, 11,5, 12,5, 13,5, 14,5, 15,5, 16,5, 17,5, 18,5, 19,5, 20,5, 21,5, 22,5, 23,5, 24,5, #factory walls
                       12,10, 13,10, 14,10, 15,10, 16,10, 17,10, 18,10, 19,10, 20,10, 21,10, 22,10, 23,10, 24,10, #walls of other building
                       12,11, 12,12, 12,13, 12,15, 12,16, #also walls of other building
                       1,11, 2,11, 3,11, 4,11, 5,11, 6,11, 7,11, 1,12, 2,12, 3,12, 4,12, 5,12, 6,12, 7,12, #rails
                       7,1, 8,1, 9,1, 10,1, 11,1,  #machine1
                       14,2, 15,2, 16,2, 17,2, 18,2, 14,3, 15,3, 16,3, 17,3, 18,3, #machine2
                       22,1, 23,1, 24,1, 22,2, 23,2, 24,2 #machine3
                       ]

            #doorPos: x,y, key# to open, open or not, rgb
            doorPos = [5,3,"key1",True,(200,200,200), 12,14,"key2",True,(200,100,100)]
            #keyPos: x,y, key#, picked or placed, rgb
            keyPos = [3,2,"key1",True,(200,200,200), 20,3,"key2",True,(200,100,100)]
            
            #heatTiles: x,y, intensity, shaded or not
            heatTiles = [1,10,3,True, 2,10,4,True, 3,10,2,True, 4,10,2,True, 5,10,3,True, 6,10,4,True, 7,10,3,True, 8,11,4,True, #near the rails
                         1,4,3,True, 2,4,3,True, 2,5,4,True, 3,5,3,True, 4,5,3,True #starting area
                         ]
            
            #shade tiles: x,y, picked or placed
            shadeTiles = [7,4,True, 8,4,True, 7,3,True, 9,3,True]
            
            #have not been introduced yet
            interactItem = []
            interacTile = []
            buttonTile = []
            
            item = "none"
            
            horseX = 985
            horseX2 = -140
            setup = False
            
        screen.fill((200,200,255))
        
        horsePos, horseX, horseX2 = lvl1(horseX, horseX2)
        levels(charX, charY, item)
        
        #drawing
        draw.rect(screen, (200,200,255), (0,55, 25, 645))
        draw.rect(screen, (200,200,255), (986,55, 15,645))
        screen.blit(trainPic,(25,455,280,80))
        screen.blit(railPic,(25,575,280,80))

        characterRect = character(charX,charY, move, state)

        clear = endGoal(20,15) #ending the level
        if clear == True or hp <= 0 or collision(characterRect, horsePos):
            state = stateGameOver
            if clear == True:   
                success = True
                message = "congrats"
                if progression == 1:
                    progression += 1
            else:
                success = False
                if hp <= 0:
                    message = "you died to the heat"
                else:
                    message = "Couldn't even avoid horses"
            stateGame = False
            state = stateGameOver

    if state == stateLvl2: # level 2
        if setup == True: #setting up
            #initial position
            charX = 2
            charY = 4 
            
            hp = 100

            #bullets
            boolet1Rect = Rect(585,195,240,1)
            boolet2Rect = Rect(585,235,320,1)
            boolet3Rect = Rect(545,275,360,1)
            boolet4Rect = Rect(425,435, 320,1)
            boolet5Rect = Rect(425,475, 320,1)            
            #images
            crater = image.load("level2\\crater.png")
            tankCrater = image.load("level2\\craterfortank.png")
            tank = image.load("level2\\tank.png")
            smallCrater = image.load("level2\\cratersmall.png")
            artillery = image.load("level2\\arty.png")
            ammo = image.load("level2\\ammunitionIcon.png")

            #walls
            wallPos = [1,7, 2,7, 3,7, 4,7, 4,1, 4,2, 4,3, 4,4, 4,5, #spawn
                       4,8, 1,9, 2,9, 3,9, 4,9, 1,12, 2,12, 3,12, 4,12, 6,12, 6,13, 6,14, 6,15, 6,16, 5,5, 6,5, 3,10, 3,11, #trench walls
                       11,3, 12,3, 13,3, 11,4, 14,4, 11,5, 12,5, 13,5, 14,5, #crater + tank
                       11,12, 12,12, 13,12, 11,13, 12,13, 13,13, #crater
                       14,13, 15,13, 16,13, 14,14, 16,14, 14,15, 15,15, 16,15, #crater
                       18,7, 19,7, 20,7, 18,8, 19,8, 20,8, #crater
                       17,1, 17,2, 17,3, 18,3, 19,1, 19,2, 19,3, #crater
                       14,7, 15,7, 16,7, 14,8, 16,8, 14,9, 15,9, 16,9, #crater
                       21,11, 22,11, 24,11, 21,12, 21,13, 21,14, 21,15, 21,16 #enemy trench
                       ]

            #doors and keys
            doorPos = [4,6, "key1", True, (0,255,0), 5,12,"key2",True,(255,100,150), 23,11,"key3", True, (100,255,200)]
            keyPos = [1,1, "key1", True, (0,255,0), 3,2,"key2",True,(255,100,150), 24,1,"key3",True,(100,255,200)]
            
            #interactable items and tiles
            interactItem = [5,1,"Tank Shell",True,(200,223,125),ammo ,7,10,"Artillery Shell",True,(42,236,120),ammo]
            interacTile = [12,6,"Tank Shell",True,(200,223,125),ammo, 4,10,"Artillery Shell",True,(42,236,120),ammo]
            
            #heat and shade tiles
            heatTiles = [14,16, 4, True, 13,16, 3, True, 13,15, 5,True, 13,14,4, True, 12,14,3, True, 12,15, 5, True, 11,16,5,True,
                         21,7,4,True, 22,7,5,True, 22,8,3, True, 23,8,6,True ,24,8,6,True, 17,7,7,True, 17,8,6,True]
            shadeTiles = [21,1,True, 22,1,True, 22,2,True, 23,2,True,
                          2,14,True, 1,14,True, 3,15,True, 2,16,True, 4,13,True, 4,16,True]
            
            #not yet introduced
            buttonTile = []
            
            count = 0
            
            shooting1 = True
            shooting2 = True
            item = "none"
            
            setup = False

        screen.fill((155,118,83))

        count, boolet = lvl2(count)
        levels(charX, charY, item)
        characterRect = character(charX,charY, move, state)

        #drawings
        screen.blit(crater,(666,56,120,120))
        screen.blit(tankCrater,(426,136,120,120))
        screen.blit(tank,(466,176,119,119))
        screen.blit(crater,(546,296,119,119))
        screen.blit(crater,(546,536,119,119))
        screen.blit(smallCrater,(426,496,119,119))
        screen.blit(smallCrater,(706,296,119,119))
        screen.blit(artillery,(25,415,119,79))

        clear = endGoal(23,15) #end of level
        if clear == True or hp <= 0 or collision(characterRect, boolet):
            state = stateGameOver
            if clear == True:   
                success = True
                message = "congrats"
                if progression == 2:
                    progression += 1
            else:
                success = False
                if hp <= 0:
                    message = "you died to the heat"
                else:
                    message = "Couldn't outsmart a bullet"
            stateGame = False
            state = stateGameOver

    if state == stateLvl3: # level 3
        if setup == True:
            #initial position
            charX = 10
            charY = 2
            
            hp = 100
            codes = image.load("general\\codeIcon.png")
            
            wallPos = [9,1, 9,2, 9,3, 9,5, 9,6, 9,7, 10,8, 10,9, 10,10, 10,11, 10,13, 10,14, 9,14, 9,15, 9,16 #next to road
                       ,15,1, 15,2, 15,3, 15,4, 15,6, 15,7, 15,8, 15,9, 15,10, 16,10, 17,10, 17,11, 17,12, 17,13, 17,15, 17,16 #next to road
                       ,1,8, 2,8, 3,8, 4,8, 5,8, 6,8, 7,8, 8,8, 9,8, 18,10, 19,10, 20,10, 21,10, 22,10, 23,10, 24,10 #inner walls
                       ,17,1, 18,1, 19,1, 20,1, 17,2, 18,2, 19,2, 20,2 #factory machines
                       ,20,4, 21,4, 22,4, 23,4, 20,5, 21,5, 22,5, 23,5
                       ,18,7, 19,7, 20,7, 21,7, 18,8, 19,8, 20,8, 21,8
                       ,6,3, 6,4, 6,5
                       ,1,1, 2,1, 3,1, 4,1
                       ,1,7, 2,7, 3,7, 4,7
                       ,6,10, 7,10, 8,10]

            #door and key postitions
            doorPos = [9,4,"key1",True,(200,133,218), 15,5,"key2",True,(61,250,210), 10,12,"key3",True,(239,152,8), 17,14,"speakeasy key",True,(206,48,53)]
            keyPos = [10,16,"key1",True,(200,133,218), 2,3,"key2",True,(61,250,210), 23,7,"key3",True,(239,152,8), 16,12,"speakeasy key",False,(206,48,53)]
            
            #interactable items and tiles
            interactItem = [3,5,"code (part 1)",True,(187,207,109),codes, 23,2,"code (part 2)",True,(187,207,109),codes, 6,9,"code (part 3)",True,(187,207,109),codes]
            interacTile = [16,11,"code (part 1)",True,(187,207,109),codes, 16,11,"code (part 2)",True,(187,207,109),codes, 16,11,"code (part 3)",True,(187,207,109),codes]
            
            #heat and shade tiles
            heatTiles = [12,4,9,True, 14,10,6,True, 11,7,8,True, 11,2,7,True, 13,15,8,True, 13,11,6,True, 14,12,8,True, 14,13,10,True, 11,11,7,True
                         ,14,14,11,True, 13,5,12,True, 12,8,13,True, 14,3,9,True, 13,4,6,True]
            shadeTiles = [1,3,True, 3,3,True, 4,3,True, 1,5,True, 2,5,True, 4,5,True]
            
            #not yet introduced
            buttonTile = []
            
            count = 0
            
            #stuff with the cars
            shooting1 = True
            shooting2 = True
            shooting3 = True
            
            gangster = False
            carY = -200
            
            gangster2 = False
            carY2 = 700

            item = "none"
            
            code = 0

            #images
            car2 = image.load("level3\\car1.png")
            car2g = image.load("level3\\cargangster.png")
            
            car1 = transform.rotate(car2,180)
            car1g = transform.rotate(car2g,180)
            
            setup = False
         
        screen.fill((194,178,128))
        draw.rect(screen,(CONCRETE),(425,55,160,640))

        levels(charX, charY, item)
        count, carY, gangster, carY2, gangster2, collideBox, code = lvl3(count, carY, gangster, carY2, gangster2, code)
        characterRect = character(charX,charY, move, state)

        clear = endGoal(23,14) #end of level
        if clear == True or hp <= 0 or collision(characterRect, collideBox):
            state = stateGameOver
            if clear == True:   
                success = True
                message = "congrats"
                if progression == 3:
                    progression += 1
            else:
                success = False
                if hp <= 0:
                    message = "you died to the heat"
                else:
                    message = "Cars and guns are as good for your health as heat is"
            stateGame = False
            state = stateGameOver

    if state == stateLvl4: # level 4
        if setup == True: #setting up
            #starting postition
            charX = 3
            charY = 2 

            hp = 100
            #images
            frequency = image.load("general\\radioIcon.png")
            wallLower = image.load("level4\\wallthing2.png")
            wallUpper = image.load("level4\\wallthing.png")
            bunker = image.load("level4\\bunker.png")
            bunker2 = image.load("level4\\bunker2.png")
            hedgehog = image.load("level4\\Hedgehog.png")
            crater = image.load("level4\\crater.png")
            
            #bullets
            booletOneRect = Rect(385,115, 360,1)
            booletTwoRect = Rect(385,155, 360,1)
            booletThreeRect = Rect(385,195, 360,1)
            
            booletFourRect = Rect(385,315, 360,1)
            booletFiveRect = Rect(425,355, 320,1)
            booletSixRect = Rect(425,395, 320,1)
            
            booletSevenRect = Rect(385,555, 360,1)
            booletEightRect = Rect(425,595, 320,1)
            booletNineRect = Rect(385,635, 360,1)

            shooting1 = True
            shooting2 = True
            shooting3 = True

            #walls
            wallPos = [12,1, 12,2, 12,4, 12,7, 12,8, 12,9, 12,10, 12,11, 12,12, 12,13, 12,14, 12,15, 12,16 #initial wall
                       ,1,1, 2,1, 3,1, 4,1, 5,1 ,1,3, 2,3, 3,3, 4,3, 5,3, 1,4, 2,4, 3,4, 4,4, 5,4, 1,7, 2,7, 3,7, 4,7, 5,7 #landing craft
                       ,1,10, 2,10, 3,10, 4,10, 5,10, 1,13, 2,13, 3,13, 4,13, 5,13
                       ,21,1, 21,2, 21,3, 21,4, 21,5, 21,6, 21,7, 21,8, 21,9, 21,10, 21,12, 21,13, 21,14, 21,15, 21,16 #fort
                       ,19,2, 20,2, 19,3, 19,4, 20,4, 19,7, 20,7, 19,8, 19,9, 20,9, 19,13, 20,13, 19,14, 19,15, 22,13, 23,13, 24,13 #some wall stuff
                       ,9,8, 9,14, 8,3, 8,10, 7,13 #obstacles
                       ]
            #door and key positions
            doorPos = [12,3,"breacher",True,(150,150,150), 21,11,"explosive",True,(100,100,100)]
            keyPos = [1,2,"breacher",True,(150,150,150), 20,14,"explosive",True,(100,100,100)]

            #interactable items and tiles
            interactItem = [8,12,"frequency1", True, (36,143,20),frequency, 18,5,"frequency2", True, (36,143,20),frequency, 16,10,"frequency3",True, (36,143,20),frequency]
            interacTile = [2,5,"frequency1", True, (36,143,20),frequency, 2,5,"frequency2", True, (36,143,20),frequency, 2,5,"frequency3",True, (36,143,20),frequency]
            
            #heat and shade tiles
            heatTiles = [10,6,5,True, 11,5,8,True, 11,6,5,True, 12,5, 5,True, 12,6, 7,True, 13,6,10,True, 14,5,8,True, #alternate path through the wall
                         13,11, 6, True, 14,10, 6, True, 14,11, 5, True, 15,10, 5,True, 15,12, 9, True, 16,11, 7,True #between bunkers
                         ,18,10,8,True, 17,12,7,True, 17,11,4,True, 18,12,10,True, 19,10,8,True, 19,11,5,True] #also between bunkers
            shadeTiles = [1,11,True, 2,11,True, 2,12,True, 3,11,True, 4,12,True, 7,5,True, 7,9,True, 8,11,True, 9,2,True, 9,14,True, 10,12,True]
            
            #not yet introduced
            buttonTile = []
            
            count = 0
            item = "none"
            
            setup = False
         
        screen.fill((194,178,128))
        #rectangles
        draw.rect(screen,(79,66,181),(25,55,200,640))#ocean
        
        draw.rect(screen,CONCRETE,(825,55,160,640))
        draw.rect(screen,CONCRETE,(745,95,80,120))
        draw.rect(screen,CONCRETE,(745,295,80,120))
        draw.rect(screen,CONCRETE,(745,535,80,120))
    
        draw.rect(screen,(METAL),(25,55,200,280))#landing craft
        draw.rect(screen,(METAL),(25,455,200,80))

        levels(charX, charY, item)
        characterRect = character(charX,charY, move, state)

        
        #various images
        screen.blit(bunker,(746,96,97,119))#bunkers
        screen.blit(bunker,(746,296,97,119))
        screen.blit(bunker2,(746,536,97,119))

        count,boolet = lvl4(count)
        
        screen.blit(wallUpper,(26,56,200,40))
        screen.blit(wallUpper,(26,176,200,40))
        screen.blit(wallUpper,(26,416,200,40))

        screen.blit(wallLower,(26,136,200,40))
        screen.blit(wallLower,(26,296,200,40))
        screen.blit(wallLower,(26,536,200,40))
        
        screen.blit(hedgehog,(306,136))
        screen.blit(hedgehog,(346,336))
        screen.blit(hedgehog,(306,416))
        screen.blit(hedgehog,(266,536))
        screen.blit(hedgehog,(346,576))

        screen.blit(crater,(866,536))
        
        clear = endGoal(23,2) #end of level
        if clear == True or hp <= 0 or collision(characterRect, boolet):
            state = stateGameOver
            if clear == True:   
                success = True
                message = "congrats"
                if progression == 4:
                    progression += 1
            else:
                success = False
                if hp <= 0:
                    message = "you died to the heat"
                else:
                    message = "when will you learn that you can't outsmart a bullet"
            stateGame = False
            state = stateGameOver


    if state == stateLvl5: # level 5
        if setup == True: #initial setup
            #starting position
            charX = 2
            charY = 7 
            
            hp = 50 #hp halves so that heat tiles appear to do more damage
            #images
            fuel = image.load("level5\\fuelIcon.png")
            siren = image.load("level5\\sirenIcon.png")
            toolBox = image.load("general\\toolboxIcon.png")
            frequency = image.load("general\\radioIcon.png")
            bulletin = image.load("general\\bulletin.png")
            tower = image.load("level5\\tower.png")
            rocket = image.load("level5\\rocket.png")
            checkmark = image.load("level5\\checkmark.png")
            car = image.load("level5\\car.png")
            car2 = transform.rotate(car,90)
            
            #walls
            wallPos = [1,5, 3,5, 4,5, 5,5, 6,5, 7,5, 8,5, 8,4, 8,3, 8,2, 8,1 #Fuel depot
                       ,1,9, 2,9, 3,9, 4,9, 5,9, 6,9, 8,9, 8,10, 8,11, 8,12, 8,13, 8,14, 8,15, 8,16 #Supply warehouse
                       ,9,11, 11,11, 11,12, 11,13, 11,14, 11,15, 11,16 #the technical stuff room
                       ,15,1, 15,2, 15,3, 16,3, 17,3, 18,3, 19,3, 20,3, 21,3, 21,2, 21,1] #launch tower

            #door and key positions
            doorPos = [2,5,"key1",True,(164,98,172), 7,9,"key2",True,(178,215,205), 10,11,"key3",True,(175,121,111),
                       15,4,"launch",True,(200,50,50), 15,5,"launch",True,(200,50,50), 15,6,"launch",True,(200,50,50), 15,7,"launch",True,(200,50,50), 
                       15,8,"launch",True,(200,50,50), 15,9,"launch",True,(200,50,50), 16,9,"launch",True,(200,50,50), 17,9,"launch",True,(200,50,50), 
                       18,9,"launch",True,(200,50,50), 19,9,"launch",True,(200,50,50), 20,9,"launch",True,(200,50,50), 21,9,"launch",True,(200,50,50), 
                       21,8,"launch",True,(200,50,50), 21,7,"launch",True,(200,50,50), 21,6,"launch",True,(200,50,50), 21,5,"launch",True,(200,50,50), 
                       21,4,"launch",True,(200,50,50), #rocket
                       
                       #car
                       14,12,"clear",True,BLACK, 14,13,"clear",True,BLACK, 14,14,"clear",True,BLACK,
                       15,12,"clear",True,BLACK, 15,13,"clear",True,BLACK, 15,14,"clear",True,BLACK,
                       #car
                       9,6,"clear",True,BLACK, 10,6,"clear",True,BLACK, 11,6,"clear",True,BLACK,
                       9,7,"clear",True,BLACK, 10,7,"clear",True,BLACK, 11,7,"clear",True,BLACK]
            keyPos = [6,13,"key1",True,(164,98,172), 1,8,"key2",True,(178,215,205), 6,15,"key3",True,(175,121,111)]
            
            #interactable items and tiles
            interactItem = [2,3,"Fuel1",True,(50,50,50),fuel, 5,2,"Fuel2",True,(50,50,50),fuel, 4,3,"Fuel3",True,(50,50,50),fuel, 3,1,"Fuel4",True,(50,50,50),fuel,
                            2,14,"Toolbox",True,(100,100,255),toolBox, 4,12,"Toolbox2",True,(100,255,100),toolBox, 2,13,"frequency",True,(214,125,117),frequency
                            ,4,13,"Siren key",True,(195,80,8),siren]
            interacTile = [14,4,"Fuel1",True,(50,50,50),fuel, 14,4,"Fuel2",True,(50,50,50),fuel, 14,4,"Fuel3",True,(50,50,50),fuel, 14,4,"Fuel4",True,(50,50,50),fuel
                           ,14,6,"Toolbox",True,(100,100,255),toolBox, 14,7,"Toolbox2",True,(100,255,100),toolBox, 9,13,"frequency",True,(214,125,117),frequency
                           ,9,14,"Siren key",True,(195,80,8),siren]
            
            #button tiles
            buttonTile = [14,5,"Check systems",True, (57,197,131),"I", 9,15,"Send all clear",True,(119,24,102),"C"]
            
            #heat and shade tiles
            heatTiles = [16,3,13,True, 17,7,11,True, 19,4,12,True, 17,5,10,True, 20,6,15,True, 18,6,14,True, 18,2,12,True, 20,3,10,True, 16,6,12,True,
                         17,4,10,True, 19,7,13,True, 16,4,13,True, 19,5,16,True, 20,5,14,True, 17,1,14,True, 16,1,16,True, 19,1,14,True, 20,2,13,True,
                         17,6,11,True, 18,3,17,True, 17,2,15,True, 16,5,10,True, 18,7,11,True,
                         7,6,11,True, 8,6,11,True, 8,7,11,True, 9,8,11,True, 10,8,11,True, 9,7,11,True, 10,5,11,True, 12,7,11,True, 10,6,11,True, 11,6,11,True]
            shadeTiles = [2,15,True, 2,12,True, 2,11,True, 4,11,True, 4,15,True, 6,14,True, 6,12,True]
            
            count = 0
            item = "none"
            steps = 0
            
            #bulleting board instructions
            line1 = fontSmall.render("- Preliminary inspection (blue toolbox)", 1, (0,0,0))
            line2 = fontSmall.render("- First fueling stage takes place (2 tanks)", 1, (0,0,0))
            line3 = fontSmall.render("- Establish communication to mission control", 1, (0,0,0))
            line4 = fontSmall.render("- Second fueling stage (2 tanks)", 1, (0,0,0))
            line5 = fontSmall.render("- Check all systems (button)", 1, (0,0,0))
            line6 = fontSmall.render("- Final inspection (green toolbox)", 1, (0,0,0))
            line7 = fontSmall.render("- Clear pad with siren", 1, (0,0,0))
            line8 = fontSmall.render("- Send all clear", 1, (0,0,0))
            line9 = fontSmall.render("- Watch the spectacle", 1, (0,0,0))
                                                                   
            setup = False
         
        screen.fill(CONCRETE)
        
        levels(charX, charY, item)
        lvl5(bulletin)
        characterRect = character(charX,charY, move, state)
        
        clear = endGoal(18,4) #end of level
        if clear == True or hp <= 0:
            state = stateGameOver
            if clear == True:   
                success = True
                message = "congrats"
                if progression == 5:
                    progression += 1
            else:
                success = False
                if hp <= 0:
                    message = "you died to the heat"
            stateGame = False
            state = stateGameOver

        screen.blit(tower, (586,56))
        
        #stuff that will clear at some point
        if steps != 10:
            screen.blit(rocket, (586,175))
        if steps < 9:
            screen.blit(car,(546,496))
            screen.blit(car2,(346,256))
                        
        
        if charX == 3 and charY == 10: #bulletin board (it's position here ensures that it is above everything else)
            draw.rect(screen,(255,255,255),(260,50,480,600))
            
            centre(fontSmall,(50,50,900,50),"Launching the Rocket (To-do list IN THIS ORDER)")
            screen.blit(line1, (280,150))
            screen.blit(line2, (280,200))
            screen.blit(line3, (280,250))
            screen.blit(line4, (280,300))
            screen.blit(line5, (280,350))
            screen.blit(line6, (280,400))
            screen.blit(line7, (280,450))
            screen.blit(line8, (280,500))
            screen.blit(line9, (280,550))
            
            count = 0
            for i in range(11): #checkmarks
                if steps > i and i != 1 and i != 4:
                    screen.blit(checkmark,(690,130+count*50))
                    count += 1


    if state == stateLvl6: # level 6
        if setup == True: #inital setup
            #starting position
            charX = 23
            charY = 13
            
            hp = 50
            #images
            parts = image.load("general\\toolboxIcon.png")
            kaboom = image.load("general\\tntIcon.png")
            people = image.load("level6\\people.png")
            people2 = image.load("level6\\people2.png")
            wrecker = image.load("level6\\wreckingball.png")
            ball = image.load("level6\\ball.png")
            wreckBallRect = (625,96,119,79)
            
            #walls
            wallPos = [12,1, 12,2, 12,3, 12,7, 12,8, 12,12, 12,13, 12,16 #wall
                       ,18,16, 18,15, 18,14, 18,13, 18,12, 18,11, 19,11, 21,11, 22,11, 23,11, 24,11 #building
                       ,11,14, 12,14, 13,14, 14,14, 11,15, 12,15, 13,15, 14,15, 13,13, 14,13, 13,16, 14,16 #crowd
                       ,1,7, 3,7, 4,7, 5,7, 6,7, 6,6, 6,5, 6,4, 6,3, 6,2, 6,1, #building2
                       4,8, 4,9, 4,10, 4,11, 4,12, 4,13, 4,15, 4,16 #building2 part2
                       ,11,8, 11,9, 11,10, 13,8, 13,9, 13,10, 13,11 #guard tower
                       ,2,9, 3,9, 2,10, 3,10, 1,12, 2,12, 1,13, 2,13,
                       13,3, 14,3, 15,3, 15,2, 15,1]
            #door and key positions
            doorPos = [20,11,"key1",True,(134,115,161), 4,14,"key2",True,(57,176,221), 2,7,"key3",True,(212,72,196),
                       12,11,"Blownup",True,(121,85,61),
                       12,4,"wreckingball",True,(174,160,75), 12,5,"wreckingball",True,(174,160,75), 12,6,"wreckingball",True,(174,160,75)] #wall section
            keyPos = [22,13,"key1",True,(134,115,161), 12,9,"key2",True,(57,176,221), 2,16,"key3",True,(212,72,196)]
            
            #interactable items and tiles
            interactItem = [24,16,"parts1",True,(156,88,31),parts, 22,4,"parts2",True,(156,88,31),parts, 14,10,"parts3",True,(156,88,31),parts, 
                            19,15,"TNT1",True,(165,32,25),kaboom, 5,8,"TNT2",True,(165,32,25),kaboom, 11,1,"TNT3",True,(165,32,25),kaboom]
            interacTile = [16,4,"parts1",True,(156,88,31),parts, 16,4,"parts2",True,(156,88,31),parts, 16,4,"parts3",True,(156,88,31),parts, 
                           11,11,"TNT1",True,(165,32,25),kaboom, 11,11,"TNT2",True,(165,32,25),kaboom, 11,11,"TNT3",True,(165,32,25),kaboom]
            
            #buttons
            buttonTile = [15,4,"activate",False,(2,86,105),"A"]
            
            #heat and shade tiles
            heatTiles = [15,7,14,True, 14,8,10,True, 15,8,13,True, 16,9,11,True, 16,10,12,True, 16,11,13,True,
                         18,6,13,True, 19,6,9,True, 20,6,9,True, 20,7,13,True, 21,7,14,True, 21,8,12,True, 22,9,10,True, 22,10,13,True,
                         7,7,10,True, 7,8,13,True, 8,8,9,True, 8,9,13,True, 10,8,11,True, 10,9,12,True, 
                         7,4,11,True, 9,4,12,True, 10,4,11,True, 11,4,11,True, 
                         7,10,10,True, 7,11,9,True, 8,11,10,True, 8,12,13,True, 9,14,11,True, 10,13,13,True, 
                         1,9,10,True, 1,10,12,True, 2,11,9,True, 3,12,11,True]
            shadeTiles = [24,15,True, 24,13,True, 24,12,True, 22,12,True, 22,15,True, 22,16,True, 19,12,True, 19,13,True, 19,14,True, 19,16,True,
                          1,15,True, 1,16,True, 3,15,True, 3,16,True]
            
            count = 0
            item = "none"

            #various stuff 
            peopleY = 0            
            repair = 0
            tnt = 0
            
            setup = False
        
        #drawing
        screen.fill(GRASS)
        draw.rect(screen,(87,87,86),(265,55,160,640))

        draw.rect(screen,(87,87,86),(545,255,160,480))
        draw.rect(screen,(87,87,86),(705,255,280,160))
        draw.rect(screen,(87,87,86),(425,535,160,160))

        draw.rect(screen,CONCRETE,(25,335,120,360))
        draw.rect(screen,CONCRETE,(25,55,200,280))
        draw.rect(screen,CONCRETE,(745,495,240,200)) 

        levels(charX, charY, item)
        count, peopleY, collidePeople, wrecker, ball, wreckBallRect = lvl6(count, peopleY, repair, wrecker, ball, wreckBallRect)
        characterRect = character(charX,charY, move, state)

        #images
        screen.blit(people,(66,376))
        screen.blit(people,(26,496))
        
        screen.blit(people2,(426,576))
        screen.blit(people2,(506,536))
        screen.blit(people2,(506,616))
                                
        screen.blit(wrecker,(506,56))
        screen.blit(ball,wreckBallRect)
        
        clear = endGoal(3,4) #end of level
        if clear == True or hp <= 0 or collision(characterRect, collidePeople):
            state = stateGameOver
            if clear == True:   
                success = True
                message = "congrats"
                if progression == 6:
                    progression += 1
            else:
                success = False
                if hp <= 0:
                    message = "you died to the heat"
                else:
                    message = "Trampled by a crowd"
            stateGame = False
            state = stateGameOver

                        
    if state == stateLvl7: # level 7
        if setup == True: #initial setup
            #starting position
            charX = 22
            charY = 13
            
            hp = 25
            
            #images
            keycard = image.load("level7\\keycard.png")
            bulletin = image.load("general\\bulletin.png")
            car = image.load("level7\\car.png")
            car2 = transform.rotate(car,90)            
            car3 = transform.rotate(car,180)
            car4 = transform.rotate(car,270)
                        
            #wall
            wallPos = [10,1, 10,2, 10,3, 10,4, 10,5, 10,6, 9,6, 8,6, 7,6, 6,6, 5,6, 3,6, 2,6, 1,6, #top left building
                       3,1, 3,2, 3,3, 3,4,  1,4
                       ,1,11, 2,11, 3,11, 4,11, 5,11, 6,11, 7,11, 8,11, 9,11, 10,11, 10,12, 10,14, 10,15, 10,16 #bottom left building
                       ,15,11, 15,12, 15,13, 15,14, 15,15, 15,16, 16,11, 17,11, 18,11, 19,11, 21,11, 22,11, 23,11, 24,11 #bottom right building 
                       ,1,14, 3,14, 3,15, 3,16
                       ,7,2, 8,2, 9,2, 7,4, 8,4, 9,4
                       ,16,1, 16,2, 16,3, 16,4, 17,1, 18,1, 18,2, 18,3, 18,4 #shipping container
                       ]
            #door and key positions
            doorPos = [17,4,"hammer",True,(241,84,118), 7,3,"key1",True,(77,47,14), 7,5,"keycard",True,(236,163,118), 
                       2,14,"passcode",True,(177,126,249), 7,1,"keycards",True,(38,238,124), 2,4,"password",True,(255,255,255)]
            keyPos = [21,2,"hammer",True,(241,84,118), 2,16,"key1",True,(77,47,14), 24,14,"keycard",False,(236,163,118)]
            
            #interactable items and tiles
            interactItem = [17,2,"card1",True,(38,238,124),keycard, 17,13,"card2",True,(38,238,124),keycard, 5,16,"card3",True,(38,238,124),keycard, 
                            17,3,"code1",True,(236,163,118),codeIcon, 7,16,"code2",True,(236,163,118),codeIcon, 4,3,"code3",True,(236,163,118),codeIcon]
            interacTile = [4,1,"card1",True,(38,238,124),keycard, 4,1,"card2",True,(38,238,124),keycard, 4,1,"card3",True,(38,238,124),keycard,
                           24,13,"code1",True,(236,163,118),codeIcon, 24,13,"code2",True,(236,163,118),codeIcon, 24,13,"code3",True,(236,163,118),codeIcon]
            
            #buttons
            buttonTile = [1,12,"1",True,(177,126,249),"1", 2,12,"2",True,(177,126,249),"2", 3,12,"3",True,(177,126,249),"3", 
                          9,1,"r",True,(255,0,0),"r", 9,3,"g",True,(0,255,0),"g", 9,5,"b",True,(0,0,255),"b"]
            
            #heat and shade tiles
            heatTiles = [2,9,10,True, 3,9,11,True, 3,8,10,True, 4,8,13,True, 5,7,12,True, 6,9,10,True, 1,10,12,True, 7,10,10,True, 8,8,11,True, 9,7,10,True #left stretch
                         ,12,5,10,True, 11,4,10,True, 14,4,10,True, 13,7,10,True, 13,3,10,True, 12,8,10,True, #up stretch 
                         15,9,10,True, 17,8,10,True, 21,10,10,True, 19,8,10,True, 20,7,10,True, 18,7,10,True, 16,10,10,True, 16,8,10,True, 14,7,10,True,
                         12,14,10,True, 14,11,10,True, 12,13,10,True, 11,11,10,True, 11,12,10,True, 13,14,10,True, 12,14,10,True]
            shadeTiles = [17,14,True, 17,15,True, 17,16,True, 19,12,True, 19,14,True, 19,15,True, 19,16,True, 21,13,True, 21,14,True, 21,15,True, 21,16,True]
            
            count = 0
            item = "none"
            
            #interactables progression
            codes = 0
            cards = 0
            
            #combination codes
            combination2 = 0
            combination1 = 0
            combo1 = ""
            combo2 = ""
            
            #cars
            carPos = 100
            carPos2 = 100
            moveState = 1

            #bulletin board
            line1 = fontSmall.render("- Red button: 3 cards", 1, (0,0,0))
            line2 = fontSmall.render("- One is missing. Last seen at the construction site", 1, (0,0,0))
            line3 = fontSmall.render("- Green button: Room locked behind passcode", 1, (0,0,0))
            line4 = fontSmall.render("- 232113", 1, (0,0,0))
            line5 = fontSmall.render("- Blue button: keycard", 1, (0,0,0))
            line6 = fontSmall.render("- Access is locked behind a code (3 parts)", 1, (0,0,0))
            line7 = fontSmall.render("- Someone lost one of the parts.", 1, (0,0,0))
            line8 = fontSmall.render("- It was reported missing after a tri the", 1, (0,0,0))
            line9 = fontSmall.render("construction site... again?", 1, (0,0,0))            
            line10 = fontSmall.render("- rrgbbg", 1, (0,0,0))

            setup = False
         
        #drawings
        screen.fill(CONCRETE)
        draw.rect(screen,(87,87,86),(425,55,160,640))
        draw.rect(screen,(87,87,86),(25,295,960,160))
        draw.rect(screen,(208,188,162),(585,55,400,240))
        screen.blit(bulletin,(26,216))

        levels(charX, charY, item)
        codes,carPos,carPos2,cars,moveState = lvl7(cards,codes,carPos,carPos2,moveState, combo1, combo2)
        characterRect = character(charX,charY, move, state)
        
        clear = endGoal(1,1) #end of level
        if clear == True or hp <= 0 or collision(characterRect, cars):
            state = stateGameOver
            if clear == True:   
                success = True
                message = "congrats"
            else:
                success = False
                if hp <= 0:
                    message = "you died to the heat"
                else:
                    message = "Cars. Deadly then, deadly now"
            stateGame = False
            state = stateGameOver
        
        if charX == 1 and charY == 5: #bulletin board
            draw.rect(screen,(255,255,255),(260,50,480,600))
            
            centre(fontSmall,(50,50,900,50),"Vault Opening")
            
            screen.blit(line1, (280,150))
            screen.blit(line2, (280,200))
            screen.blit(line3, (280,250))
            screen.blit(line4, (280,300))
            screen.blit(line5, (280,350))
            screen.blit(line6, (280,400))
            screen.blit(line7, (280,450))
            screen.blit(line8, (280,500))
            screen.blit(line9, (280,550))
            screen.blit(line10, (280,600))
    fps.tick(60)
    display.update()
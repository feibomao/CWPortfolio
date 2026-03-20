#Name: Colin Wei
#Date: whendue
#Course: ICS3U1-01
#Description: Playlist generator

#importing stuff
from pygame import * 
import random

#pygame initialization
init()
canvasX = 800
canvasY = 600
SIZE = (canvasX,canvasY)
screen = display.set_mode(SIZE)


def makeButton(screen,dimensions,mx,my, text, color, hover): #buttons
    if dimensions.collidepoint(mx,my):
            draw.rect(screen, (hover), dimensions)
    else:
            draw.rect(screen, (color), dimensions)
    centre(fontSmall, dimensions, text)

def displaySongs(yList, xList, theList): #the songlist
    yPos = yList
    for i in (theList):
        centre(fontSmall,(xList,yPos,canvasX/2,100),i)
        yPos += 20

def updateList(): #updates list
    songs = []
    genres = []
    artists = []
    playList = open("playlist.txt","r")
    while True:
        songInfo = playList.readline()
        songInfo = songInfo.rstrip("\n")
        if songInfo == "":
            break
        canAdd, genre, artist = meetsFormat(songInfo)
        if  canAdd == True:
            songs.append(songInfo)

            if genres.count(genre) == 0:
                genres += [genre]
            if artists.count(artist) == 0:
                artists += [artist]
            moreThanOne(artist, artists)
            moreThanOne(genre, genres)

        
    playList.close()
    #genres, artists, addOrNot = artistsAndGenres(songs)
    return songs, genres, artists

def centre(font,rectangle,text):
    
    output = font.render(text, 1, (0,0,0))
    fontSize = font.size(text)

    startX = (rectangle[2]-fontSize[0])//2 + rectangle[0]
    
    startY = (rectangle[3]-fontSize[1])//2 + rectangle[1]
    
    centeredRect = (startX, startY, fontSize[0], fontSize[1])
    screen.blit(output, centeredRect)
'''
def makeList():
    genList = []
    library = songs
'''
def meetsFormat(songInfo): 
    canAdd = False
    closeGenre = 0
    openGenre = 0
    dash = 0
    for j in range(len(songInfo)):
        pos = -(j+1)
        if songInfo[pos] == ")":
            closeGenre = pos
        if songInfo[pos] == "(":
            openGenre = pos
        if songInfo[pos] == "-":
            dash = pos
            break
    if closeGenre != 0 and openGenre != 0 and dash != 0:
        canAdd = True
        genre = songInfo[openGenre+1:closeGenre]
        artist = (songInfo[dash+1:openGenre]).strip(" ")
    else:
        genre = ""
        artist = ""
        
    return canAdd, genre, artist

def moreThanOne(category, addTo):
    if category.count(",") > 0:
        word = ""
        for i in (category):
            if i == ",":
                word = word.strip(" ")
                if addTo.count(word) == 0:
                    addTo += [word]
                word = ""
            else:
                word += i
        word = word.strip(" ")
        if addTo.count(word) == 0:
            addTo += [word]
                

#reset all shenanigans
playList = open("playlist.txt","w")

playList.write("song1 - artist1 (genre1) \n")
playList.write("song2 - artist2 (genre2) \n")
playList.write("song3 - artist3 (genre1, genre5) \n")
playList.write("song4 - artist2 (genre2) \n")
playList.write("song5 - artist3 (genre1) \n")
playList.write("song6 - artist1 (genre3, genre5) \n")
playList.write("song7 - artist2 (genre1) \n")
playList.write("song8 - artist4 (genre4) \n")
playList.write("song9 - artist3 (genre1) \n")
playList.write("song10 - artist2 (genre4) \n")
playList.write("song11 - artist5 (genre2, genre4) \n")
playList.write("song12 - artist4 (genre1, genre4) \n")
playList.write("song13 - artist1 (genre2) \n")
playList.write("song14 - artist3 (genre6) \n")
playList.write("song15 - artist2 (genre1, genre6) \n")

playList.close()

RED = (255,50,50)
DRED = (255,0,0)
BLUE = (0,0,255)
LBLUE = (100,100,255)

songs, genres, artists = updateList()#generates list
genList = []
#fps
fps = time.Clock()

#some fonts setup
fontRegular = font.SysFont("Times New Roman", 30)
fontSmall = font.SysFont("Times New Roman", 15)

#mouse stuff
mx = 0
my = 0
button = 0

addSongRect = Rect(10, 110, 100, 50)
removeSongRect = Rect(120,110, 100,50)
noDupesRect = Rect(240, 110, 120,50)
generateList = Rect(410,110,120,50)
isRandList = Rect(550, 110, 120, 50)

textBoxRect = Rect(410,215, (canvasX)/2-20,30)
textBoxRect2 = Rect(690,110, 100, 50)

libraryRect = Rect(0,280,400,320)
playlistRect = Rect(400,280,400,320)

'''
for i in range(len(songs)):
    fullSong = songs[i]
    dash = fullSong.find()
'''

y = 290
listPosL = y
listPosP = y

#setup for typing
sentence = ""
sentence2 = ""
placeholder = fontSmall.render("...", 1, (0,0,0))
placeholder2 = fontSmall.render("filter songs for playlist", 1, (100,100,100))
text = fontSmall.render(sentence, 1, (0))


inputText = 0

textPos = (20,220)


directions = (10,170)
directions2 = (10,250)

directions3 = (410,170)
directions4 = (410,250)
directions5 = (410,190)

toDo = 0
displayTime = 60
tick = 60
status = 0
#typeField = 1

song = fontRegular.render("Playlist", 1, (0,0,0))
add = fontSmall.render("Enter song to add in the following format: ", 1, (0,0,0))
add2 = fontSmall.render("Enter the genre/artist you want.", 1, (0))
add3 = fontSmall.render("Leave empty if you want a mix", 1, (0))
theFormat = fontSmall.render("Song Title - Artist (Genre)", 1, (0))
instructions = fontSmall.render("Press enter to submit, press escape to cancel", 1, (0))
steps = fontSmall.render("enter to submit", 1, (0))
steps2 = fontSmall.render("escape to cancel", 1, (0))
remove = fontSmall.render("Enter song to remove", 1, (0,0,0))

#more setup
typing = False
running = True
retain = False
retain2 = False
randSong = True
toKeep = fontSmall.render("...", 1, (0))
randOn = fontSmall.render("Random (ON)", 1, (0))
randOff = fontSmall.render("Random (OFF)", 1, (0))
sortBy = ""
numSongs = 0


#Known bugs:
# toKeep gets in the way of text input (patched)
# you can filter by song name (patched)

#main loop
while running:
    for e in event.get(): # checks all events that happen
        if e.type == QUIT: #quit?
            running = False
            
        if e.type == MOUSEBUTTONDOWN: #mouse click
            mx, my = e.pos          
            button = e.button
            if button == 1: #The buttons
                if inputText == 0: #makes sure that nothing else is being done
                    if addSongRect.collidepoint(mx,my): #add
                        inputText = 1
                        sentence = ""
                        toDo = 1
                        tick = displayTime
                        text = fontSmall.render(sentence, 1, (0,0,0))
                    
                    if removeSongRect.collidepoint(mx,my): #remove
                        inputText = 1
                        sentence = ""
                        toDo = 2
                        tick = displayTime
                        text = fontSmall.render(sentence, 1, (0,0,0))                    
            
                    if generateList.collidepoint(mx,my): #generates playlist
                        genList = []
                        if sortBy == "": #mix
                            if randSong == True: #random num of songs from 5-10
                                num = random.randint(5,10)
                                for i in range(num):
                                    if len(songs) == 0:
                                        break                                
                                    elements = len(songs)
                                    toAdd = random.randint(0,elements-1)
                                    genList += [songs[toAdd]]
                                    del songs[toAdd]
                                    
                            else:
                                for i in range(numSongs):
                                    if len(songs) == 0:
                                        break                                
                                    elements = len(songs)
                                    toAdd = random.randint(0,elements-1)
                                    genList += [songs[toAdd]]
                                    del songs[toAdd]
                        else: #filtered
                            sortedList = []
                            if genres.count(sortBy) > 0 or artists.count(sortBy) > 0: #ensures that genre exsists
                                for i in songs:
                                    if i.count(sortBy) != 0:
                                        sortedList.append(i)
                                if randSong == True: #random songs from 5-10
                                    num = random.randint(5,10)
                                    for i in range(num):
                                        if len(sortedList) == 0:
                                            break
                                        elements = len(sortedList)
                                        toAdd = random.randint(0,elements-1)
                                        genList += [sortedList[toAdd]]
                                        del sortedList[toAdd]
                                else: #random # of songs of user's choosing
                                    for i in range(numSongs):
                                        if len(sortedList) == 0:
                                            break                                
                                        elements = len(sortedList)
                                        toAdd = random.randint(0,elements-1)
                                        genList += [sortedList[toAdd]]
                                        del sortedList[toAdd]
                            if len(genList) == 0: #no songs match category
                                genList += ["no songs match that category"]
                            songs, genres, artists = updateList()
                        songs, genres, arists = updateList()
                        
                    if noDupesRect.collidepoint(mx,my): #eliminates duplicates
                        #setup
                        sentence = ""
                        newFile = ""
                        count = 1
                        status = 6
    
                        while True:
                            playList = open("playlist.txt","r")
                            isDupe = False
                            for i in range(0,count): #finds line to be checked
                                dupe = playList.readline()
                            if dupe.rstrip(" \n") == "":
                                break
                            while True: #checks for duplicates
                                maybeDupe = playList.readline()
                                if maybeDupe.rstrip(" \n") == "":
                                    break
                                if maybeDupe == dupe:
                                    isDupe = True
                                    status = 5
                                    break
                            if isDupe == False: #adds if not a duplicate
                                newFile += dupe
                            count += 1
                            playList.close()
                        playList.close()
                        
                        playList = open("playlist.txt","w")
                        playList.write(newFile)
                        playList.close()
                        songs, genres, artists = updateList()
                        textPos = (20,220)
                        tick = 0
                        inputText = 0
                        
                    if textBoxRect.collidepoint(mx,my): #filter
                        retain = False
                        inputText = 2
                    if textBoxRect2.collidepoint(mx,my) and randSong == False: #not random amount of songs
                        
                        retain2 = False
                        inputText = 3
    
                    if isRandList.collidepoint(mx,my): #random toggle
                        if randSong == True:
                            randSong = False
                        else:
                            randSong = True

            if button == 5: #scroll up
                if libraryRect.collidepoint(mx,my) and listPosL > canvasY - (len(songs))*23:
                    listPosL -= 5
                if playlistRect.collidepoint(mx,my) and listPosP > canvasY - (len(genList))*23:
                    listPosP -= 5
            if button == 4: #scroll down
                if libraryRect.collidepoint(mx,my) and listPosL < y:
                    listPosL += 5
                if playlistRect.collidepoint(mx,my) and listPosP < y:
                    listPosP += 5

        if e.type == MOUSEMOTION: #hover
            mx, my = e.pos

        if e.type == KEYDOWN:
            if inputText != 0: #type type type

                if e.key == K_BACKSPACE:
                    if len(sentence)>0:
                        sentence = sentence[:-1]
                elif e.key == K_ESCAPE: #cancel operation
                    toDo = 0
                    #displays previously held info 
                    if inputText == 3:
                        retain2 = True
                    if inputText == 2:
                        retain = True
                    
                    inputText = 0
                    sentence = ""

                elif e.key == K_RETURN: # process final input
                    if inputText == 1:
                        if toDo == 1:
                            playList = open("playlist.txt","r")
                            
                            canAdd, artist, genre = meetsFormat(sentence)
                            if canAdd == False: #can it be added in the first place?
                                status = 8
                            else:
                                while True:
                                    songInfo = playList.readline()
                                    songInfo = songInfo.rstrip(" \n")
                                    
                                    if songInfo == sentence: #checks duplicates
                                        status = 2
                                        break
                                    
                                    if songInfo == "": #adding the song
                                        final = sentence + " \n"
                                        playList.close()
                                        
                                        playList = open("playlist.txt",("a"))
                                        playList.write(final)
                                        playList.close()  
                                        status = 1
                                        break
        
                            playList.close()
                            
                            songs, genres, artists = updateList()
                            #inputText = 0
                            tick = 0
                            
                        if toDo == 2: #removes
                            #sets up the song to add
                            newFile = ""
                            playList = open("playlist.txt","r")
                            status = 4
                            while True:
                                songInfo = playList.readline()
                                if songInfo == "":
                                    break
                                if songInfo.rstrip(" \n") != sentence: #checks for the file to be removed
                                    newFile += songInfo
                                else:
                                    status = 3
                            playList.close()
                            
                            #rewrites file
                            playList = open("playlist.txt","w")
                            playList.write(newFile)
                            playList.close()
                            
                            typing = False
                            tick = 0
                            songs, genres, artists = updateList()
                        toDo = 0
                    
                    if inputText == 2: #sorting
                        #toKeep = sentence
                        sortBy = sentence
                        toKeep = fontSmall.render(sortBy, 1, (0))
                        retain = True

                    if inputText == 3: #number of songs
                        if sentence.isdigit():
                            numSongs = int(sentence)
                            keep3 = fontSmall.render(str(numSongs), 1, (0))
                            retain2 = True
                        else:
                            status = 7
                            tick = 0
                    inputText = 0

                else: #generic text
                    sentence += e.unicode 
                text = fontSmall.render(sentence, 1, (0,0,0))

    screen.fill((255,255,255))
    
    #list of songs
    displaySongs(listPosL, 0, songs)
    displaySongs(listPosP, 400, genList)
    
    
    draw.rect(screen,(175,175,175), (0,0,canvasX,280))
    
    #where typing will be
    if inputText == 1:
        textPos = (20,220)
    elif inputText == 2:
        textPos = (420,220)
    elif inputText == 3:
        textPos = (695,125)
    
    #instructions
    if inputText == 1:
        if toDo == 1:
            screen.blit(add, (directions))
            screen.blit(theFormat, (10,190))
            screen.blit(instructions, (directions2))
        if toDo == 2:
            screen.blit(remove, (directions))
            screen.blit(instructions, (directions2))
    if inputText == 2:
        screen.blit(add2, (directions3))
        screen.blit(add3, (410,190))
        screen.blit(instructions, (directions4))
    if inputText == 3:
        screen.blit(steps, (690, 160))
        screen.blit(steps2, (690,170))
        
    if inputText == 0: #various messages
        if tick < displayTime:
            if status == 1:
                sentence = "Song added"
            if status == 2:
                sentence = "Duplicate. Not added"
            if status == 3:
                sentence = "Song removed"
            if status == 4:
                sentence = "Song not found"
            if status == 5:
                sentence = "Duplicates removed"
            if status == 6:
                sentence = "No duplicates found"
            if status == 7:
                sentence = "Not a number"
            if status == 8:
                sentence = "Does not meet format. Not added"
            text = fontSmall.render(sentence, 1, (0,0,0))
            tick += 1
        else:
            sentence = ""
            text = fontSmall.render(sentence, 1, (0,0,0))

    draw.rect(screen,(0,255,0),(50,20,700,60))
    centre(fontRegular,(0,0,canvasX,100),"Playlist")
    
    #buttons
    makeButton(screen, (addSongRect), mx, my, "add a song", RED, DRED)
    makeButton(screen, (removeSongRect), mx, my, "remove a song", RED, DRED)
    makeButton(screen, (noDupesRect), mx, my, "remove duplicates", RED, DRED)
    makeButton(screen, (generateList), mx, my, "Generate Playlist", RED, DRED)
    
    #left side text box
    draw.rect(screen, (200,200,200), (10,215, (canvasX)/2-20,30))
    draw.rect(screen, (0,0,0), (10,215, (canvasX)/2-20,30),2)

    
    #right side text boxes
    makeButton(screen, (textBoxRect), mx, my, "", (200,200,200), (150,150,150)) 
    makeButton(screen, (textBoxRect2), mx, my, "", (200,200,200), (150,150,150))
    
    #outlines
    draw.rect(screen, (0,0,0), (0,100, 400,180),2)
    draw.rect(screen, (0,0,0), (400,100, 400,180),2)    
    draw.rect(screen, (0,0,0), (textBoxRect2),2)
    draw.rect(screen, (0,0,0), (410,215, (canvasX)/2-20,30),2)
    
    if sentence == "" or inputText != 1: #placeholder text
        screen.blit(placeholder, (20,220))
    if (sentence == "" or inputText != 2) and retain == False:
        screen.blit(placeholder2, (420,220))
    if (sentence == "" or inputText != 3) and retain2 == False:
        screen.blit(placeholder, (700,125))

    makeButton(screen, (isRandList), mx, my, "", LBLUE, BLUE) #is random song?
    if randSong == True:
        centre(fontSmall,(isRandList),"Random (ON)")
        draw.rect(screen, (200,200,200), (textBoxRect2))
        centre(fontSmall,(690,115,100,25),"Disable random")
        centre(fontSmall,(690,130,100,25),"to interact")
    if randSong == False:
        centre(fontSmall,(isRandList),"Random (OFF)")
        if retain2 == True:
            screen.blit(keep3, (700,125))
            
    if retain == True: #prevents loss of previously held information
        screen.blit(toKeep, (420,220))

    #headers
    draw.rect(screen, (0,255,0), (0,280,800,50))
    centre(fontRegular, (0,280,400,50), "Library")
    centre(fontRegular, (400,280, 400,50),"Playlist")
    
    #more outlines
    draw.rect(screen,(0), (0,280,400,320),2)
    draw.rect(screen,(0), (400,280,400,320),2)
    
    screen.blit(text, (textPos))
    display.update()
    fps.tick(60)

playList.close()
quit()

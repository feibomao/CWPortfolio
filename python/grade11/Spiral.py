#Spiral
#The commented print statements served as guides and info display
import math

#prompts input and (because why not) does input handling
while True:
    beg = input("enter start number: ")
    if beg.isdigit():
        beg = int(beg)
        if 0 < beg < 100:
            break
        else:
            print("invalid")
    else:
        print("invalid")
while True:
    end = input("enter end number: ")
    if end.isdigit():
        end = int(end)
        if 0 < beg < 100 and end >= beg:
            break
        else:
            print("invalid")
    else:
        print("invalid")

#Setup for determining dimensions
nums = end - beg + 1
count = 0

while True: #Determines the rectangular portion
    for x in range(1, nums+1):
        if nums % x == 0:
            y = int(nums/x)
            if y-x == 1 or y-x == 0:
                #print("here")
                break
    if y-x == 1 or y-x == 0:
        #print("here2")
        break
    nums -= 1
    count += 1

#print(nums)
#print(count)

#vertical will be >= horizontal
#y >= i

#How up and left the top-leftmost point is
xaxis = (math.ceil(x/2)-1)
yaxis = (math.ceil(y/2)-1)

#Adjusts dimensions of box
if x == y:
    if x % 2 == 1:
        #print("bottom left")
        if count > 0:
            y += 1
    else:
        #print("top right")
        if count > 0:
            yaxis += 1
            y += 1
elif y % 2 == 1:
    #print("left up")
    if count > 0:
        xaxis += 1
        x += 1
else:
    #print("right bottom")
    if count > 0:
        x += 1

#Position (subject to change throughout the spiral)
upby = yaxis
leftby = xaxis

#print("Horizontal:", x)
#print("Vertical:", y)
#print("Left by =", leftby)
#print("Up by =", upby)

for k in range(1,y+1): #Makes the sprial (manages rows)
    for l in range(1,x+1): #Manages the individual numbers
        #Setup
        vert = 0
        hori = 0
        moveby = 1
        downRight = True
        num = beg

        while True: #Spiraling out to the target location
            for a in range(1,moveby+1): #Vertical aspect
                if vert == upby and hori == leftby:
                    break
                if downRight == True:
                    vert -= 1
                else:
                    vert += 1
                num += 1
            if vert == upby and hori == leftby:
                break

            for b in range(1,moveby+1): #Horizontal aspect
                if vert == upby and hori == leftby:
                    break
                if downRight == True:
                    hori -= 1
                else:
                    hori += 1
                num += 1
            if vert == upby and hori == leftby:
                break

            #Expanding scope
            moveby += 1
            if downRight == True:
                downRight = False
            else:
                downRight = True

        if num <= end: #Print number or print placeholder
            print("%2i" %num, end = ' ')
        else:
            print("  ", end = ' ')
        leftby -= 1
    
    #Preparations for the next row
    print()
    upby -= 1
    leftby = xaxis
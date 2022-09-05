from sense_hat import SenseHat
from random import randint
from time import sleep
import time

sense = SenseHat()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
black = (0,0,0)

colourList = [red,green,blue,yellow,black]

# Coding Exercise 5a

# sense.set_pixel(0,0,red)
# sense.set_pixel(7,0,green)
# sense.set_pixel(0,7,blue)
# sense.set_pixel(7,7,yellow)

# def setCornerColours(colourList, counter=3):
#     for i in range(1,counter+1):
#         posList = []

#         while True:
#             intTuple = (randint(0,7),randint(0,7))
#             if intTuple in posList:
#                 continue
#             posList.append(intTuple)
#             if len(posList) == len(colourList):
#                 break
        
#         posCounter = 0
#         for colour in colourList:
#             sense.set_pixel(posList[posCounter], colour)
#             posCounter+=1

#         sleep(3)
# setCornerColours(colourList)

# Coding exercise 5b,5c

defaultImage = [black, black, black, black, black, black, black, black,
                black, black, black, yellow, black, black, black, black,
                black, black, yellow, yellow, yellow, black, black, black,
                black, yellow, black, yellow, black, yellow, black, black,
                black, black, black, yellow, black, black, black, black,
                black, black, black, black, yellow, black, black, black,
                black, black, black, yellow, black, black, black, black, 
                black, black, black, black, black, black, black, green]

# sense.set_pixels(defaultImage)

flipColourDict = {black:green,green:black} 

def flipColour(imagePixel, random=False):
    flipColourDict2 = dict(flipColourDict)

    if random:
        newColourDict = {}
        colourListCopy = list(colourList)
        usedColours = []
        for i in colourList:
            colourListCopy.remove(i)
            while True:
                randColour = colourListCopy[randint(0,len(colourListCopy)-1)]
                if randColour not in usedColours:
                    break
            
            colourListCopy.insert(i)

            usedColours.append(randColour)
            
            newColourDict[i] = randColour
        flipColourDict2 = newColourDict


    for i in range(len(imagePixel)):
        if imagePixel[i] in flipColourDict2.keys():
            imagePixel[i] = flipColourDict2[imagePixel[i]]
    return imagePixel

def rotateImage():
    rotation = [0,90,180,270]
    sense.set_rotation(rotation[randint(0,3)])

def flipImage(imagePixel, flipColourDict):
    while True:
        sense.set_pixels(imagePixel)
        imagePixel = flipColour(imagePixel,True)
        rotateImage()
        sleep(1)

flipImage(defaultImage,flipColourDict)

sense.clear()
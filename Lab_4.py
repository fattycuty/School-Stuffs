# Hazim Khoiruddin 

from sense_hat import SenseHat
from random import randint,choice
from time import sleep

sense = SenseHat()
sense.clear()

r = (255,0,0)
g = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
b = (0,0,0)
w = (255,255,255)

#####################################################################

# Coding Exercise 5a

# sense.set_pixel(0,0,r)
# sense.set_pixel(7,0,g)
# sense.set_pixel(0,7,blue)
# sense.set_pixel(7,7,yellow)
# sleep(2)
# sense.clear()

# def setRandomColours(colours, counter=3):
#     for i in range(1,counter+1):
#         posList = []

#         while True:
#             intTuple = (randint(0,7),randint(0,7))
#             if intTuple in posList:
#                 continue
#             posList.append(intTuple)
#             if len(posList) == len(colours):
#                 break
        
#         posCounter = 0
#         for colour in colours:
#             sense.set_pixel(posList[posCounter][0], posList[posCounter][1], colour)
#             posCounter+=1
            
#         sleep(1)
#         sense.clear()           
        
# setRandomColours([r,g,blue,yellow], 50)

#####################################################################

# Coding exercise 5b,5c

# colourList = [r,g,blue,yellow,b,w] # ONLY EVEN NUMBER OF COLOURS
# defaultImage = [b, b, b, b, b, b, b, b,
#                 b, b, b, yellow, b, b, b, b,
#                 b, b, yellow, yellow, yellow, b, b, b,
#                 b, yellow, b, yellow, b, yellow, b, b,
#                 b, b, b, yellow, b, b, b, b,
#                 b, b, b, yellow, b, b, b, b,
#                 b, b, b, yellow, b, b, b, b, 
#                 b, b, b, b, b, b, b, g]

# sense.set_pixels(defaultImage)

# flipColourDict = {b:yellow, yellow:b} # must come in pairs e.g b:yellow AND yellow:b | replaced colour must not be repeated

# def flipColour(imagePixel, random=False):
#     flipColourDict2 = dict(flipColourDict)
#     if random:
#         flipColourDict2 = {}
#         newColourDict = {}
#         colourListCopy = list(colourList) #[r,g,blue,yellow,b,w]
#         usedColours = list(colourList)
#         for i in colourList:
#             colourListCopy.remove(i)

#             randColour = choice(usedColours)
#             if i == randColour:
#               randColour = choice(usedColours)
            
#             colourListCopy.insert(0,i)
            
#             newColourDict[i] = randColour
            
#             usedColours.remove(randColour)
            
#         flipColourDict2 = dict(newColourDict)
        
#     for i in range(len(imagePixel)):
#         if imagePixel[i] in flipColourDict2.keys():
#             imagePixel[i] = flipColourDict2[imagePixel[i]]

#     return imagePixel

# def rotateImage():
#     sense.set_rotation(choice([0,90,180,270]))

# def flipImage(imagePixel, flipColourDict):
#     counter = 0
#     while True:
#         sense.set_pixels(imagePixel)
#         imagePixel = flipColour(imagePixel,True)
#         rotateImage()
#         sleep(1)
#         counter+=1
#         print("Image has been flipped {} time(s).".format(counter))
        

# flipImage(defaultImage,flipColourDict)


#####################################################################

# Coding exercise 5d Challenge

arrow_red=[
  b,b,b,b,b,b,b,b,
  b,b,b,r,b,b,b,b,
  b,b,r,r,r,b,b,b,
  b,r,b,r,b,r,b,b,
  b,b,b,r,b,b,b,b,
  b,b,b,r,b,b,b,b,
  b,b,b,r,b,b,b,b,
  b,b,b,b,b,b,b,b]

arrow_green=[
  b,b,b,b,b,b,b,b,
  b,b,b,g,b,b,b,b,
  b,b,g,g,g,b,b,b,
  b,g,b,g,b,g,b,b,
  b,b,b,g,b,b,b,b,
  b,b,b,g,b,b,b,b,
  b,b,b,g,b,b,b,b,
  b,b,b,b,b,b,b,b]

def game(score=0, angle=0, delay=3):
    while True:
        last_angle = angle
        while angle == last_angle:
            angle = choice([0, 90, 180, 270])

        sense.set_rotation(angle)
        sense.set_pixels(arrow_green)

        sleep(delay)

        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']

        x = round(x, 0)
        y = round(y, 0)

        if x == -1 and angle == 180:
            sense.set_pixels(arrow_green)
            score += 1
        elif x == 1 and angle == 0:
            sense.set_pixels(arrow_green)
            score += 1
        elif y == -1 and angle == 90:
            sense.set_pixels(arrow_green)
            score += 1
        elif y == 1 and angle == 270:
            sense.set_pixels(arrow_green)
            score += 1
        else:
            sense.set_pixels(arrow_red)
            break

        delay = delay * 0.95
        sleep(0.5)

    sense.show_message("Score is {}".format(score))
    return

game()

#####################################################################

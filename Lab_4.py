# Hazim Khoiruddin 

from sense_hat import SenseHat
from random import randint,choice
from time import sleep

sense = SenseHat()
sense.clear()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
black = (0,0,0)
white = (255,255,255)

#####################################################################

# Coding Exercise 5a

# sense.set_pixel(0,0,red)
# sense.set_pixel(7,0,green)
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
        
# setRandomColours([red,green,blue,yellow], 50)

#####################################################################

# Coding exercise 5b,5c

# colourList = [red,green,blue,yellow,black,white] # ONLY EVEN NUMBER OF COLOURS
# defaultImage = [black, black, black, black, black, black, black, black,
#                 black, black, black, yellow, black, black, black, black,
#                 black, black, yellow, yellow, yellow, black, black, black,
#                 black, yellow, black, yellow, black, yellow, black, black,
#                 black, black, black, yellow, black, black, black, black,
#                 black, black, black, yellow, black, black, black, black,
#                 black, black, black, yellow, black, black, black, black, 
#                 black, black, black, black, black, black, black, green]

# sense.set_pixels(defaultImage)

# flipColourDict = {black:yellow, yellow:black} # must come in pairs e.g black:yellow AND yellow:black | replaced colour must not be repeated

# def flipColour(imagePixel, random=False):
#     flipColourDict2 = dict(flipColourDict)
#     if random:
#         flipColourDict2 = {}
#         newColourDict = {}
#         colourListCopy = list(colourList) #[red,green,blue,yellow,black,white]
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

# Coding exercise 5d Challenge | not done/not working


# gameImage = [black, black, black, black, black, black, black, black,
#                 black, black, black, green, black, black, black, black,
#                 black, black, green, green, green, black, black, black,
#                 black, green, black, green, black, green, black, black,
#                 black, black, black, green, black, black, black, black,
#                 black, black, black, green, black, black, black, black,
#                 black, black, black, green, black, black, black, black, 
#                 black, black, black, black, black, black, black, black]

# failImage = [black, black, black, black, black, black, black, black,
#                 black, black, black, red, black, black, black, black,
#                 black, black, red, red, red, black, black, black,
#                 black, red, black, red, black, red, black, black,
#                 black, black, black, red, black, black, black, black,
#                 black, black, black, red, black, black, black, black,
#                 black, black, black, red, black, black, black, black, 
#                 black, black, black, black, black, black, black, black]

# def game():
#     while True:
#         sense.set_pixels(gameImage)
        
#         angle = 0
        
#         new_angle = choice([0,90,180,270])
#         while angle == new_angle:
#             new_angle = choice([0,90,180,270])
        
#         accel = sense.get_accelerometer_raw()
#         x = round(accel['x'],0)
#         y = round(accel['y'],0)
        
#         if angle == 0 and y == 1:
#             angle = choice([0,90,180,270])
#             sense.set_rotation(angle)
#         elif angle == 270 and y == -1:
#             angle = choice([0,90,180,270])
#             sense.set_rotation(angle)
#         elif angle == 180 and x == 1:
#             angle = choice([0,90,180,270])
#             sense.set_rotation(angle)
#         elif angle == 90 and x == -1:
#             angle = choice([0,90,180,270])
#             sense.set_rotation(angle)

#         delay = 2
#         # delay = delay * 0.95
#         sleep(delay)

# game()

#####################################################################

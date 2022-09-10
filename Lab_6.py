# Hazim Khoiruddin

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

b = (0,0,0)
w = (255,255,255)
r = (255,0,0)
g = (0,255,0)

board_no_walls =  [[b,b,b,b,b,b,b,b], 
                   [b,b,b,b,b,b,b,b],
                   [b,b,b,b,b,b,b,b],
                   [b,b,b,b,b,b,b,b],
                   [b,b,b,b,b,b,b,b],
                   [b,b,b,b,b,b,b,b],
                   [b,b,b,b,b,b,b,b], 
                   [b,b,b,b,b,b,b,b] ]
                   
board_walls = [[r,r,r,b,b,b,b,r], 
               [r,b,b,b,b,b,b,r],
               [b,b,b,b,g,r,b,r],
               [b,r,r,b,r,r,b,r],
               [b,b,b,b,b,b,b,b],
               [b,r,b,r,r,b,b,b],
               [b,b,b,r,b,b,b,r], 
               [r,r,b,b,b,r,r,r] ]



# y=2				# y coordinate of marble
# x=2				# x coordinate of marble
# board[y][x]=w		# a white marble

# board_1D=sum(board,[])        # convert to 1-dimension list
# print(board_1D)               # for code debugging
# sense.set_pixels(board_1D)    # display it

# This function checks the pitch value and the x coordinate  
# to determine whether to move the marble in the x-direction.
# Similarly, it checks the roll value and y coordinate to
# determine whether to move the marble in the y-direction.

def move_marble(pitch,roll,x,y, board):
  new_x = x # assume not change to start with
  new_y = y # assume not change to start with
  
  if 1<pitch<179 and x!=0:
    new_x-=1 # move left
  elif 359>pitch>179 and x!=7:
    new_x+=1 # move right
  
  if 1<roll<179 and y!=7:
    new_y+=1 # move up
  elif 359>roll>179 and y!=0:
    new_y-=1 # move down
  
  new_x,new_y = check_wall(x,y,new_x,new_y, board) 
  return new_x, new_y

def check_wall(x,y,new_x,new_y, board): 
    if board[new_y][new_x] != r: 
        return new_x, new_y 
    elif board[new_y][x] != r: 
        return x, new_y 
    elif board[y][new_x] != r:
        return new_x, y 
    else:
      return x,y

def set_green_location(board):
  pass

def game(board,x,y):
  board[y][x]=w
  while True:
    board[y][x] = b
    pitch = sense.get_orientation()['pitch']
    roll = sense.get_orientation()['roll']
    x,y = move_marble(pitch,roll,x,y,board)
    if board[y][x] == g:
      board[y][x] = w
      break
    board[y][x] = w
    sense.set_pixels(sum(board,[]))
    # print("pitch {0} roll {1}".format(round(pitch,0), round(roll,0)))
    sleep(0.05)
  print("You won the game.")

game(board_walls,2,2)